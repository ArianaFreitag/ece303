import datetime
import logging
import hashlib


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
    flattened list containing num_pkt in index 1 and 2, hash in index #, and packet data till end
    '''

    string = str(pkt)+str(num_pkt)
    h = blake2b(digest_size=4)
    hash = h.update(string)

    hashed_pkt = num_pkt.extend(hash).extend(pkt)

    # ENCODE USING REED SOLOMAN
    encoded_pkt = rs.encode(hashed_pkt)
    return encoded_pkt

def rcvPacket(hashed_pkt):
    # DECODE PACKET USING REED SOLOMAN
    decoded_pkt = rs.decode(hashed_pkt)

    num_pkt = decoded_pkt[0:1]
    hash = decoded_pkt[2:5]
    pkt = decoded_pkt[6:]

    string = str(pkt)+str(num_pkt)
    h = blake2b(digest_size=4)
    hash_check = h.update(string)

    if hash == hash_check:
        sendAck(num)
        return true, num_pkt, pkt
    else
        sendNack()
        return false



def sendAck ():

    return

def sendNack(ack, num_pkt):

    return
