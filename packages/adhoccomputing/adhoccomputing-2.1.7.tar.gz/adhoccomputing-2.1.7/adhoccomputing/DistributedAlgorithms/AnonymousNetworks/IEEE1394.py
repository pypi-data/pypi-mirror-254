#!/usr/bin/env python

"""
Implementation of the "IEEE1394 (FireWire)" as described in the textbook
"Fokkink, Wan. Distributed algorithms: an intuitive approach. MIT Press,
2018.", first introduced in " IEEE 1394-1995 - IEEE Standard for a High
Performance Serial Bus"
"""

__author__ = "Yigit Sever"
__contact__ = "yigit@yigitsever.com"
__copyright__ = "Copyright 2021, WINSLAB"
__credits__ = ["Yigit Sever"]
__date__ = "2021-05-24"
__deprecated__ = False
__email__ = "yigit@yigitsever.com"
__license__ = "GPLv3"
__maintainer__ = "developer"
__status__ = "Production"
__version__ = "0.0.1"

import datetime
import random
from enum import Enum
from time import sleep

from ...Experimentation.Topology import Topology
from ...GenericModel import GenericModel, GenericMessageHeader, GenericMessagePayload, GenericMessage
from ...Generics import *

class FireWirePacketType(Enum):
    """Two types of FireWire requests:
    - Parent Request
    - Acknowledgement"""

    PARENT_REQ = "PARENT_REQ"
    ACKNOWLEDGEMENT = "ACKNOWLEDGEMENT"
    START_TIMER = "START_TIMER"
    CHECK_TIMER = "CHECK_TIMER"
    TIMEOUT = "TIMEOUT"
    ROOT_CONTENTION = "ROOT_CONTENTION"


class FireWireMessageHeader(GenericMessageHeader):
    def __init__(
        self,
        messagefrom,
        messageto,
        messagetype="FireWire Message",
        nexthop=float("inf"),
        interfaceid=float("inf"),
        sequencenumber=-1,
    ):
        super().__init__(
            messagetype, messagefrom, messageto, nexthop, interfaceid, sequencenumber
        )


class FireWireMessagePayload(GenericMessagePayload):
    def __init__(self):
        super().__init__(messagepayload="FireWire Message")


class FireWireNode(GenericModel):

    # For animation/plotting
    callback = None
    draw_delay = None

    def __init__(self, componentname, componentinstancenumber, context=None, configurationparameters=None, num_worker_threads=1, topology=None):
        super().__init__(componentname, componentinstancenumber, context, configurationparameters, num_worker_threads, topology)
        self.eventhandlers[FireWirePacketType.START_TIMER] = self.on_timer_initialize
        self.eventhandlers[FireWirePacketType.CHECK_TIMER] = self.check_timer
        self.eventhandlers[FireWirePacketType.TIMEOUT] = self.timeout
        self.eventhandlers[FireWirePacketType.ROOT_CONTENTION] = self.root_contention

        self.parent = None
        self.received = list()
        self.neighbours = set()
        self.is_leader = False
        self.in_root_contention = False
        self.is_waiting = False
        self.is_terminated = False

        self.waiting_since = None
        self.timeout_duration = 2

    def on_init(self, eventobj: Event):
        sleep(1)
        self.neighbours = set(self.topology.get_neighbors(self.componentinstancenumber))
        logger.debug(f"the neighbours of {self.componentinstancenumber} is {self.neighbours}")

        self.send_parent_req()

    def send_parent_req(self):
        """Send a parent request to the only eligible neighbour node. The
        neighbour node should not have sent this node a parent request and the
        number of such neighbours of this node should be 1.
        """
        # if there is *only* one possible parent then send them a parent request here

        result = self.neighbours - set(self.received)

        if len(result) == 1:
            par = result.pop()
            self.parent = par

            logger.debug(
                f"🤖 {self.componentinstancenumber} picked {self.parent} as it's parent"
            )

            next_hop_interface_id = f"{self.componentinstancenumber}-{self.parent}"

            header = FireWireMessageHeader(
                messagefrom=self.componentinstancenumber,
                messageto=self.parent,
                nexthop=self.parent,
                messagetype=FireWirePacketType.PARENT_REQ,
                interfaceid=next_hop_interface_id
            )
            payload = FireWireMessagePayload()

            message = GenericMessage(header, payload)
            self.send_down(Event(self, EventTypes.MFRT, message))
        else:
            # Cannot send a parent request, more than one possible parent
            return

    def root_contention(self, eventobj: Event):
        if self.is_leader:
            return
        logger.debug(f"🤖 {self.componentinstancenumber} is in ROOT CONTENTION")
        decision = random.choice([True, False])

        if decision:
            logger.debug(f"🤖 {self.componentinstancenumber} decides to YIELD")
            self.in_root_contention = True
            self.send_parent_req()
            self.is_waiting = False
            self.waiting_since = None
        else:
            logger.debug(f"🤖 {self.componentinstancenumber} decides to HOLD")
            self.is_waiting = True
            self.in_root_contention = False
            self.send_self(Event(self, FireWirePacketType.START_TIMER, "..."))

        # self.callback.set()
        # self.draw_delay.wait()
        # self.draw_delay.clear()

    def on_timer_initialize(self, eventobj: Event):
        start_time = eventobj.time
        self.waiting_since = start_time
        self.send_self(Event(self, FireWirePacketType.CHECK_TIMER, "..."))

    def check_timer(self, eventobj: Event):
        current_time = datetime.datetime.now()
        delta = current_time - self.waiting_since
        if delta.seconds > self.timeout_duration:
            self.send_self(Event(self, FireWirePacketType.TIMEOUT, "..."))
        else:
            sleep(0.2)
            self.send_self(Event(self, FireWirePacketType.CHECK_TIMER, "..."))

    def timeout(self, eventobj: Event):
        self.send_self(Event(self, FireWirePacketType.ROOT_CONTENTION, "..."))

    def on_message_from_bottom(self, eventobj: Event):
        """ New message from the link layer """
        header: FireWireMessageHeader = eventobj.eventcontent.header
        # paylaod is not important for FireWire

        if header.messagetype == FireWirePacketType.PARENT_REQ:
            if header.messagefrom is not self.parent:
                new_child = header.messagefrom

                self.received.append(new_child)

                next_hop_interface_id = f"{self.componentinstancenumber}-{new_child}"

                header = FireWireMessageHeader(
                    messagefrom=self.componentinstancenumber,
                    messageto=new_child,
                    nexthop=new_child,
                    messagetype=FireWirePacketType.ACKNOWLEDGEMENT,
                    interfaceid=next_hop_interface_id
                )
                payload = FireWireMessagePayload()

                ack = GenericMessage(header, payload)
                self.send_down(Event(self, EventTypes.MFRT, ack))

                self.send_parent_req()
            elif not self.is_waiting:
                self.send_self(Event(self, FireWirePacketType.ROOT_CONTENTION, "..."))
            else:
                logger.debug(f" 👑 {self.componentinstancenumber} is elected as the leader")
                self.is_leader = True
                self.is_terminated = True

        elif (
            header.messagetype == FireWirePacketType.ACKNOWLEDGEMENT
            and header.messagefrom == self.parent
        ):
            # This node's parent request got acknowledged, the process can
            # safely terminate
            logger.debug(
                f"🤖 {self.componentinstancenumber} received an ACK from {header.messagefrom}, terminating"
            )
            self.is_terminated = True
            self.in_root_contention = False

        self.callback.set()
        self.draw_delay.wait()
        self.draw_delay.clear()
