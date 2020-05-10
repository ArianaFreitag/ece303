def flip_bit(bin,flips):
	bits = list(bin)
	l = len(bits)
	for n in flips:
		if n != 0:
			if bits[l-n] == '1':
				bits[l-n] = '0'
			else:
				bits[l-n] = '1'
	return ''.join(bits)

def remove_parity(bin,r):
	l = len(bin)
	bits = list(bin)
	for i in range(r):
		bits[l-2**i] = ''
	return ''.join(bits)

def asc2bit(data):
	bits = ""
	for i in data:
		bits = bits + format(i,'08b')
	return bits

def asc2int(data):
	print data
	print type(data)
	bits = ""
	for i in data:
		bits = bits + format(i,'08b')
	return int(bits,2)


def bit2asc(bits):
	s = ""
	for i in range(0,len(bits),8):
		byte = bits[i:i+8]
		s = s + chr((int(byte, 2)))
	return bytearray(s)

def data2asc(data):
	s = ""
	for i in data:
		s = s + chr(i)
	return s

def byte_error(data1, data2):
	l = len(data1)
	bits = 0
	for i in range(len(data1)):
		if data1[i] != data2[i]:
			bits += 1
	return [bits, bits/l]



def hex2asc(hexStr):
	bytes = []

	hexStr = ''.join( hexStr.split(" ") )

	for i in range(0, len(hexStr), 2):
		bytes.append( chr( int (hexStr[i:i+2], 16 ) ) )

	

