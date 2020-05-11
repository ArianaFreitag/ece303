# Written by S. Mevawala, modified by D. Gitzel

import logging

import channelsimulator
import utils
import sys
import socket
import some_utils

class Receiver(object):

    def __init__(self, inbound_port=50005, outbound_port=50006, timeout=10, debug_level=logging.INFO):
        self.logger = utils.Logger(self.__class__.__name__, debug_level)

        self.inbound_port = inbound_port
        self.outbound_port = outbound_port
        self.simulator = channelsimulator.ChannelSimulator(inbound_port=inbound_port, outbound_port=outbound_port,
                                                           debug_level=debug_level)
        self.simulator.rcvr_setup(timeout)
        self.simulator.sndr_setup(timeout)

    def receive(self):
        all_data = {}

        while True:
            try:
                rx = self.simulator.u_receive()

                [not_corrupted, num_pkt, pkt] = utils.rcvPacket(rx)

                if not_corrupted:
                    num = some_utils.asc2int(num_pkt)
                    if num == 0:
                        break
                    all_data[num] = pkt
                    ack = utils.makeAck(num_pkt)
                    self.simulator.u_send(ack)
                else:
                    nack = utils.makeNack(num_pkt)
                    self.simulator.u_send(nack)
            except socket.timeout:
                pass
     
        #for i in all_data.values():
         #   sys.stdout.write(i)


        return(all_data)
        


class BogoReceiver(Receiver):

    def __init__(self):
        super(BogoReceiver, self).__init__()

    def sendAck(self):
        ACK_DATA = [255,255,255,255,255]
        self.simulator

    def receive(self):
        self.logger.info("Receiving on port: {} and replying with ACK on port: {}".format(self.inbound_port, self.outbound_port))
        while True:
            try:
                 data = self.simulator.u_receive()  # receive data
                 self.logger.info("Got data from socket: {}".format(
                     data.decode('ascii')))  # note that ASCII will only decode bytes in the range 0-127
                 rcvPacket(data)
                 sys.stdout.write(data)
                 self.simulator.u_send(BogoReceiver.ACK_DATA)  # send ACK
            except socket.timeout:
                sys.exit()

if __name__ == "__main__":
    # test out BogoReceiver
    rcvr = Receiver()
    test = rcvr.receive()

    rx = ""
    for i in test.values():
        rx = rx + i
    sys.stdout.write(rx)



