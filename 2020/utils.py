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
    
    num_hex = format(num_pkt, '08x')

    num_byte = bytearray.fromhex(num_hex)
    
    
    
    pkt_and_num = num_byte + pkt


    h = hashlib.md5()
    h.update(pkt_and_num)
    hash = h.hexdigest()
    hash = bytearray.fromhex(hash)


    
    #print num_hex + hash + pkt
    #print 'hash: ' + hash

    # ENCODE USING REED SOLOMAN
    # encoded_pkt = rs.encode(hashed_pkt)
    return num_byte + hash + pkt



def rcvPacket(hashed_pkt):
    # DECODE PACKET USING REED SOLOMAN
    # decoded_pkt = rs.decode(hashed_pkt)


    num_pkt = hashed_pkt[0:4]
    hash = hashed_pkt[4:20] # 16byte digest (32 hex, 128 bit)
    pkt = hashed_pkt[20:]

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
    #num_hex = format(num_pkt, '08x')
    #num_byte = bytearray.fromhex(num_hex)

    pkt_and_num = num_pkt + chr(255)

    h = hashlib.md5()
    h.update(pkt_and_num)
    hash = h.hexdigest()
    hash = bytearray.fromhex(hash)


    return num_pkt + hash

def makeNack(num_pkt):
    #num_hex = format(num_pkt, '08x')
    #num_byte = bytearray.fromhex(num_hex)

    pkt_and_num = num_pkt + chr(0)

    h = hashlib.md5()
    h.update(pkt_and_num)
    hash = h.hexdigest()
    hash = bytearray.fromhex(hash)


    return num_pkt + hash

def rcvAck(ack):
    
    pkt_num = ack[0:4]
    hash = ack[4:]

    h = hashlib.md5()
    h.update(pkt_num + chr(255))
    ack_hash = h.hexdigest()
    ack_hash = bytearray.fromhex(ack_hash)


    if hash == ack_hash:
        return pkt_num, True
    else:
        return 0, False
