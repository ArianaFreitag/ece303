import datetime
import logging
import hashlib
import some_utils


class Logger(object):

    def __init__(self, name, debug_level):
        now = datetime.datetime.now()
        logging.basicConfig(filename='{}_{}.log'.format(name, datetime.datetime.strftime(now, "%Y_%m_%dT%H%M%S")),
                            level=debug_level)

    @staticmethod
    def info(message):
        logging.info(message)

    @staticmethod
    def debug(message):
        logging.debug(message)


def makePacket(pkt, num_pkt):
    '''
    num_pkt: list containing the packet number
    pkt: byte array at fixed length containing the packet data

    returns:
    [[number of packer], [packet], [hash of packet]] where all data is in a bytearray
    '''
    

    num = bytearray(some_utils.data2asc([num_pkt]))

    print ('num',num,type(num))

    string = str(pkt)+str(num)
    h = hashlib.md5()
    h.update(string)
    hash = h.digest()
    hash = bytearray(hash)

    

    hashed_pkt = num + hash + pkt

    # ENCODE USING REED SOLOMAN
    # encoded_pkt = rs.encode(hashed_pkt)
    return hashed_pkt

def rcvPacket(hashed_pkt):
    # DECODE PACKET USING REED SOLOMAN
    # decoded_pkt = rs.decode(hashed_pkt)

    num_pkt = decoded_pkt[0:1]
    hash = decoded_pkt[2:5]
    pkt = decoded_pkt[6:]

    string = str(pkt)+str(num_pkt)
    h = hashlib.sha224()
    hash_check = h.update(string)

    if hash == hash_check:
        sendAck(num)
        return True, num_pkt, pkt
    else:
        sendNack()
        return False, num_pkt, pkt



def sendAck ():

    return 

def sendNack(ack, num_pkt):

    return



def recieveAck(ack):

    return pkt_num, ack_or_nak
