import random
import time

from ...Generics import *
from ...GenericModel import GenericModel

# define your own message types
class ApplicationLayerMessageTypes(Enum):
    PROPOSE = "PROPOSE"
    ACCEPT = "ACCEPT"


# define your own message header structure
class ApplicationLayerMessageHeader(GenericMessageHeader):
    pass


# define your own message payload structure
class ApplicationLayerMessagePayload(GenericMessagePayload):
    pass


class GenericApplicationLayer(GenericModel):

    def __init__(self, componentname, componentinstancenumber, context=None, configurationparameters=None, num_worker_threads=1, topology=None):
        super().__init__(componentname, componentinstancenumber, context, configurationparameters, num_worker_threads, topology)
        
    def on_init(self, eventobj: Event):
        logger.debug(f"Initializing {self.componentname}.{self.componentinstancenumber}")

        if self.componentinstancenumber == 0:
            # destination = random.randint(len(Topology.G.nodes))
            destination = 1
            hdr = ApplicationLayerMessageHeader(ApplicationLayerMessageTypes.PROPOSE, self.componentinstancenumber,
                                                destination)
            payload = ApplicationLayerMessagePayload("23")
            proposalmessage = GenericMessage(hdr, payload)
            randdelay = random.randint(0, 5)
            time.sleep(randdelay)
            self.send_self(Event(self, "propose", proposalmessage))
        else:
            pass

    def on_message_from_bottom(self, eventobj: Event):
        try:
            applmessage = eventobj.eventcontent
            hdr = applmessage.header
            if hdr.messagetype == ApplicationLayerMessageTypes.ACCEPT:
                logger.debug(
                    f"Node-{self.componentinstancenumber} says Node-{hdr.messagefrom} has sent {hdr.messagetype} message")
            elif hdr.messagetype == ApplicationLayerMessageTypes.PROPOSE:
                logger.debug(
                    f"Node-{self.componentinstancenumber} says Node-{hdr.messagefrom} has sent {hdr.messagetype} message")
        except AttributeError:
            logger.error("Attribute Error")



