# Written by S. Mevawala, modified by D. Gitzel

import logging
import socket

import channelsimulator
import utils
import sys
import some_utils


class Sender(object):

    def __init__(self, inbound_port=50006, outbound_port=50005, timeout=10, debug_level=logging.INFO):
        self.logger = utils.Logger(self.__class__.__name__, debug_level)

        self.inbound_port = inbound_port
        self.outbound_port = outbound_port
        self.simulator = channelsimulator.ChannelSimulator(inbound_port=inbound_port, outbound_port=outbound_port,
                                                           debug_level=debug_level)
        self.simulator.sndr_setup(timeout)
        self.simulator.rcvr_setup(timeout)

    def send(self, data):
        # make list of all the packets
        list_packets = {}

        i = 0
        num_pkt = 1
        packet_size = 1000

        while i < len(DATA) - packet_size:
            new_data = utils.makePacket(data[i:i+packet_size], num_pkt)
            i += packet_size
            list_packets[num_pkt] = new_data
            num_pkt += 1
            

        # [[],[],[],...,[]]
        list_packets[num_pkt] = utils.makePacket(data[i:], num_pkt)

        #print(list_packets)


        #packet_numbers = range(len(list_packets))
        #print packet_numbers
        all_acks = False;

        while ~all_acks:
            for i in list_packets.values():
                try:
                    self.simulator.u_send(i)
                    response = self.simulator.u_receive()
                    [pkt_num, ack_or_nak] = utils.rcvAck(response)
                    if ack_or_nak:
                        num = some_utils.asc2int(pkt_num)
                        try:
                            list_packets.pop(num)
                        except KeyError:
                            pass
                except socket.timeout:
                    pass

            if list_packets == {}:
                all_acks = True
                break
            #print packet_numbers

        last_ack = False
        fin_pkt = utils.makePacket(bytearray('00000000'),0)
        while ~last_ack:
            try:
                self.simulator.u_send(fin_pkt)
                response = self.simulator.u_receive()
                [pkt_num, ack_or_nak] = utils.rcvAck(response)
                if pkt_num == 0 & ack_or_nak:
                    last_ack = True
                    break
            except socket.timeout:
                pass

class BogoSender(Sender):

    def __init__(self):
        super(BogoSender, self).__init__()

    def send(self, data):
        self.logger.info("Sending on port: {} and waiting for ACK on port: {}".format(self.outbound_port, self.inbound_port))
        while True:
            try:
                self.simulator.u_send(data)  # send data
                ack = self.simulator.u_receive()  # receive ACK
                self.logger.info("Got ACK from socket: {}".format(
                    ack.decode('ascii')))  # note that ASCII will only decode bytes in the range 0-127
                break
            except socket.timeout:
                pass


if __name__ == "__main__":
    # test out BogoSender
    DATA = bytearray(sys.stdin.read())
    #DATA = DATA[0:20000]



    sndr = Sender()
    sndr.send(DATA)

    # MAKE THIS SKIP

# print(msg[i:])
#     left_over = len(DATA)%20
#     while i < len(DATA)-20:
#         data = makePacket(DATA[i:i+20])
#         sndr.send(data)
#         i=i+20
