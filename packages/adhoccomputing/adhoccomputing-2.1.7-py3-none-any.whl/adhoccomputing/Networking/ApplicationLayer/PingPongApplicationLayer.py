import time

from ...Generics import *
from ...GenericModel import GenericModel
import random

# define your own message types
class PingPongApplicationLayerMessageTypes(Enum):
    BROADCAST = "BROADCAST"

# define your own message header structure
class PingPongApplicationLayerMessageHeader(GenericMessageHeader):
    def __init__(self, messagetype, messagefrom, messageto, nexthop=..., interfaceid=..., sequencenumber=-1, counter=0):
        super().__init__(messagetype, messagefrom, messageto, nexthop, interfaceid, sequencenumber)
    


class PingPongApplicationLayerEventTypes(Enum):
    STARTBROADCAST = "startbroadcast"


class PingPongApplicationLayer(GenericModel):
    def on_init(self, eventobj: Event):
        pass
    
    def __init__(self, componentname, componentinstancenumber, context=None, configurationparameters=None, num_worker_threads=1, topology=None):
        super().__init__(componentname, componentinstancenumber, context, configurationparameters, num_worker_threads, topology)
        self.eventhandlers[PingPongApplicationLayerEventTypes.STARTBROADCAST] = self.on_startbroadcast
        self.counter = 0

    def on_message_from_top(self, eventobj: Event):
        logger.info(f"{self.componentname}.{self.componentinstancenumber} RECEIVED {str(eventobj)}")
        self.send_down(Event(self, EventTypes.MFRT, eventobj.eventcontent))
    
    def on_message_from_bottom(self, eventobj: Event):
        evt = Event(self, EventTypes.MFRT, eventobj.eventcontent)
        logger.applog(f"{self.componentname}.{self.componentinstancenumber} RECEIVED {eventobj.eventcontent.header.sequencenumber}-{eventobj.eventcontent.header.counter} {eventobj.eventcontent.payload}")
        #logger.applog(f"{self.componentname}.{self.componentinstancenumber} RECEIVED message")
        evt.eventcontent.header.messageto = MessageDestinationIdentifiers.LINKLAYERBROADCAST
        evt.eventcontent.header.messagefrom = self.componentinstancenumber
        evt.eventcontent.payload = eventobj.eventcontent.payload + "-" + str(self.componentinstancenumber)
        evt.eventcontent.header.sequencenumber =  eventobj.eventcontent.header.sequencenumber
        evt.eventcontent.header.counter = eventobj.eventcontent.header.counter + 1
        #time.sleep(0.0000001) # TODO WHAT Should this be?
        time.sleep(random.uniform(0, 0.1))
        if evt.eventcontent.header.counter < 5:
            self.send_down(evt)  # PINGPONG
    
    def on_startbroadcast(self, eventobj: Event):
        hdr = PingPongApplicationLayerMessageHeader(PingPongApplicationLayerMessageTypes.BROADCAST, self.componentinstancenumber, MessageDestinationIdentifiers.LINKLAYERBROADCAST)
        self.counter = self.counter + 1
        hdr.sequencenumber = self.counter
        hdr.counter = 1
        payload = eventobj.eventcontent + str(self.counter) + ": " + str(self.componentinstancenumber) 
        broadcastmessage = GenericMessage(hdr, payload)
        #print(f"Payload length {len(payload)}")
        evt = Event(self, EventTypes.MFRT, broadcastmessage)
        logger.debug(f"{self.componentname}.{self.componentinstancenumber} WILL SEND {str(evt)}")
        self.send_down(evt)
    