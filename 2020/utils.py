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
    
    num_hex = format(num_pkt, '02x')
    
    
    pkt_and_num = num_hex + pkt


    h = hashlib.md5()
    h.update(pkt_and_num)
    hash = h.hexdigest()
    hash = bytearray.fromhex(hash)

    #print num_hex + hash + pkt
    #print 'hash: ' + hash

    # ENCODE USING REED SOLOMAN
    # encoded_pkt = rs.encode(hashed_pkt)
    return num_hex + hash + pkt

def rcvPacket(hashed_pkt):
    # DECODE PACKET USING REED SOLOMAN
    # decoded_pkt = rs.decode(hashed_pkt)


    num_pkt = hashed_pkt[0:2]
    hash = hashed_pkt[2:18] # 16byte digest (32 hex, 128 bit)
    pkt = hashed_pkt[18:]

    pkt_and_num = num_pkt + pkt

    h = hashlib.md5()
    h.update(pkt_and_num)
    hash_check = h.hexdigest()
    hash_check = bytearray.fromhex(hash_check)

    if hash == hash_check:
        return True, num_pkt, pkt
    else:
        return False, num_pkt, pkt



def makeAck(num_pkt):
    num_hex = format(num_pkt, '02x')
    return bytearray(num_hex) + chr(255) + chr(255) + chr(255) + chr(255)

def makeNack():
    num_hex = format(num_pkt, '02x')
    return bytearray(num_hex) + chr(0) + chr(0) + chr(0) + chr(0)



def recieveAck(ack):
    total = 0
    for i in range(1,len(ack)):
        total += ack[i]

    if total > 400:
        ack_or_nak = True
    else:
        ack_or_nak = False
    pkt_num = ack[0:2]

    return pkt_num, ack_or_nak
