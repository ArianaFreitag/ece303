from hashlib import sha224



import some_utils



def asc2bit(data):
	bits = ""
	for i in data:
		bits = bits + format(i,'08b')
	return bits


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


i = [43]

test = bytearray(data2asc(i))

print test
print type(test)


print str(test)



