from ctypes import *
import pickle
from threading import Lock
from .FrameHandlerBase import *
from ...Generics import *
from .LiquidDspUtils import *
import numpy as np

mutex = Lock()

framers: FramerObjects = FramerObjects()

def flexframe_callback(header:POINTER(c_ubyte), header_valid:c_uint32, payload:POINTER(c_ubyte), payload_len:c_uint32, payload_valid:c_int32, stats:struct_c__SA_framesyncstats_s, userdata:POINTER(None)):
    mutex.acquire(1)
    try:
        framer = framers.get_framer_by_id(userdata)
        
        if payload_valid != 0:
            pload = string_at(payload, payload_len)
            phymsg = pickle.loads(pload)
            msg = GenericMessage(phymsg.header, phymsg.payload)
            framer.send_self(Event(framer, PhyEventTypes.RECV, msg))

    except Exception as ex:
        logger.critical(f"Exception configure: {ex}")
    mutex.release()
    return 0


  
class UsrpB210FlexFramePhy(FrameHandlerBase):

    def rx_callback(self, num_rx_samps, recv_buffer):
        try:
            flexframesync_execute(self.fs, recv_buffer, num_rx_samps)
        except Exception as ex:
            logger.critical(f"Exception rx_callback: {ex}")

    
    def transmit(self, _header, _payload, _payload_len, _mod, _fec0, _fec1):
        flexframegen_assemble(self.fg, _header, _payload, _payload_len)
        last_symbol = False
        while (last_symbol == 0):
            fgbuffer = np.zeros(self.fgbuffer_len, dtype=np.complex64)
            
            last_symbol = flexframegen_write_samples(self.fg, fgbuffer, self.fgbuffer_len)
            try:
                frm = PhyFrame(self.fgbuffer_len, self.fgbuffer)
                self.frame_out_queue.put(Event(None, PhyEventTypes.SEND, frm))
                #self.sdrdev.transmit_samples(fgbuffer)
                # self.rx_callback(self.fgbuffer_len, npfgbuffer) #loopback for trial
            except Exception as ex:
                logger.critical(f"Exception transmit: {ex}")
        frm = PhyFrame(0, None)
        self.frame_out_queue.put(Event(None, PhyEventTypes.SEND, frm))
        #self.sdrdev.finalize_transmit_samples()
            
   
        
    def configure(self):
        self.fgprops = flexframegenprops_s(LIQUID_CRC_32, LIQUID_FEC_NONE, LIQUID_FEC_HAMMING74, LIQUID_MODEM_QPSK)
        res = flexframegenprops_init_default(byref(self.fgprops))
        self.fgprops.check = LIQUID_CRC_32
        self.fgprops.fec0 = LIQUID_FEC_NONE
        self.fgprops.fec1 = LIQUID_FEC_HAMMING74
        self.fgprops.mod_scheme = LIQUID_MODEM_QPSK
        self.fgbuffer_len = 64
        self.fg = flexframegen_create(self.fgprops)

        res = flexframegen_print(self.fg)
        
        self.flexframe_callback = framesync_callback(flexframe_callback)
        

        try: 
            # WILL PASS ID of THIS OBJECT in userdata then will find the object in FramerObjects
            self.fs = flexframesync_create(self.flexframe_callback, id(self))
             
        except Exception as ex:
            logger.critical(f"Exception configure: {ex}")
        
        self.sdrdev.start_rx(self.rx_callback, self)
        flexframegen_reset(self.fg)
        flexframesync_reset(self.fs)
        
    # Callbacks have to be outside since the c library does not like "self"
    # Because of this reason will use userdata to get access back to the framer object 

    def __init__(self, componentname, componentinstancenumber, context=None, configurationparameters=None, usrpconfig=None, num_worker_threads=1, topology=None):
        self.framers = framers
        super().__init__(componentname, componentinstancenumber, context, configurationparameters, usrpconfig, num_worker_threads, topology, framers, SDRType="b200")
        
