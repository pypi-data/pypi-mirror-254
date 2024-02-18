from ctypes import *
import pickle
from threading import Lock
from .FrameHandlerBase import *
from ...Generics import *
from .LiquidDspUtils import *
import numpy as np
import zlib 

mutex = Lock()


framers: FramerObjects = FramerObjects()

#def ofdm_callback(header:POINTER(c_ubyte), header_valid:c_uint32, payload:POINTER(c_ubyte), payload_len:c_uint32, payload_valid:c_int32, stats:struct_c__SA_framesyncstats_s, userdata:POINTER(None)):
def ofdm_callback(header:POINTER(c_ubyte), header_valid:c_int, payload:POINTER(c_ubyte), payload_len:c_uint, payload_valid:c_int, stats:struct_c__SA_framesyncstats_s, userdata:c_void_p ):
    mutex.acquire(1)
    try:
        framer = framers.get_framer_by_id(userdata)
        #logger.applog(f"{framer.componentname}-{framer.componentinstancenumber} RSSI {stats.rssi} {framer.sdrdev.rssi}")
        if payload_valid != 0:
            #ofdmflexframesync_print(framer.fs) 
            pload = string_at(payload, payload_len)
            phymsg = pickle.loads(zlib.decompress(pload))
            msg = GenericMessage(phymsg.header, phymsg.payload)
            framer.send_self(Event(framer, PhyEventTypes.RECV, msg))
            #logger.applog(f"{framer.componentname}-{framer.componentinstancenumber} Message= {str(msg)}   RSSI= {stats.rssi}")   
    except Exception as ex:
        logger.critical(f"Exception_ofdm_callback: {ex}")
    mutex.release()
    ofdmflexframesync_reset(framer.fs)
    return 0


  
class BladeRFOfdmFlexFramePhy(FrameHandlerBase):


    def cdb64_to_sc16q11(self, data):
        return bytearray(
            (
            np.frombuffer(
                memoryview(data), dtype=np.float32
                ).astype(np.float16) * 2048
            )
                    .astype(np.int16)
                    .tobytes()
        )

    def sc16q11_to_cdb64(self, data):
        return (
                np.frombuffer(data, dtype=np.int16)
                .astype(np.float32) / 2048
                )\
            .view(np.complex64)

    def rx_callback(self, num_rx_samps, recv_buffer):
        q = agc_crcf_create()
        agc_crcf_set_bandwidth(q,  0.25)#self.sdrdev.bandwidth/self.sdrdev.rx_rate)       
        #agc_crcf_set_rssi(q,0.01)
        #agc_crcf_squelch_enable_auto(q)
        agc_buffer = np.zeros(num_rx_samps, dtype=np.complex64) 
        try:
            agc_crcf_execute_block(q, self.sc16q11_to_cdb64(recv_buffer), num_rx_samps, agc_buffer)
            ofdmflexframesync_execute(self.fs, agc_buffer , num_rx_samps)
            #self.sdrdev.rssi = agc_crcf_get_rssi(q)
            #print( agc_crcf_get_rssi(q), agc_crcf_get_gain(q), agc_crcf_get_bandwidth(q), agc_crcf_get_signal_level(q))
            agc_crcf_destroy(q)
        except Exception as ex:
            logger.critical(f"Exception rx_callback: {ex}")
    
    def transmit(self, _header, _payload, _payload_len, _mod, _fec0, _fec1):   
        logger.debug(f"{self.componentname}-{self.componentinstancenumber} will send {_payload_len} bytes")
        ofdmflexframegen_assemble(self.fg, _header, _payload, c_uint32(_payload_len))
        last_symbol = 0
        self.fgbuffer[:] = 0
        while (last_symbol == 0):
            last_symbol = ofdmflexframegen_write_sc16q11(self.fg, self.fgbuffer, c_uint32(self.fgbuffer_len))
            #self.rx_callback( c_uint32(self.fgbuffer_len), self.fgbuffer.flatten (order="C"))  #loopback for trial
            frm = PhyFrame(self.fgbuffer_len, self.fgbuffer)
            self.frame_out_queue.put(Event(None, PhyEventTypes.SEND, frm))
            #self.sdrdev.transmit_samples(self.fgbuffer)

        frm = PhyFrame(0, None)
        self.frame_out_queue.put(Event(None, PhyEventTypes.SEND, frm))
        #self.sdrdev.finalize_transmit_samples()
        
    def configure(self):
        self.fgprops = ofdmflexframegenprops_s(LIQUID_CRC_32, LIQUID_FEC_NONE, LIQUID_FEC_HAMMING74, LIQUID_MODEM_QPSK)
        res = ofdmflexframegenprops_init_default(byref(self.fgprops))
        self.fgprops.check = LIQUID_CRC_32
        self.fgprops.fec0 = LIQUID_FEC_NONE
        self.fgprops.fec1 = LIQUID_FEC_HAMMING74
        self.fgprops.mod_scheme = LIQUID_MODEM_QPSK
        self.M = 2000
        self.cp_len = 64
        self.taper_len = 32
        self.fg = ofdmflexframegen_create(self.M, self.cp_len, self.taper_len, None, byref(self.fgprops))
       
        self.fgbuffer_len = 8192
        self.fgbuffer = np.zeros(self.fgbuffer_len*self.sdrdev.bytes_per_sample//sizeof(c_int16), dtype=np.int16) # sc16q1 samples
        
        #res = ofdmflexframegen_print(self.fg)
        
        self.ofdm_callback_function = framesync_callback(ofdm_callback)
        
        try: 
            # WILL PASS ID of THIS OBJECT in userdata then will find the object in FramerObjects
            self.fs :ofdmflexframesync = ofdmflexframesync_create(self.M, self.cp_len, self.taper_len, None, self.ofdm_callback_function, id(self))
        except Exception as ex:
            logger.critical(f"Exception configure: {ex}")

        ofdmflexframegen_reset(self.fg)
        ofdmflexframesync_reset(self.fs)
        
    # Callbacks have to be outside since the c library does not like "self"
    # Because of this reason will use userdata to get access back to the framer object 

    def __init__(self, componentname, componentinstancenumber, context=None, configurationparameters=None, usrpconfig=None, num_worker_threads=1, topology=None):
        self.framers = framers
        super().__init__(componentname, componentinstancenumber, context, configurationparameters, usrpconfig, num_worker_threads, topology, self.framers, SDRType="x115")
        
