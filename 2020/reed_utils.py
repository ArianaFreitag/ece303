import fieldmath, reed


def reed_encode(data,ecclen):
	msglen = len(data)
	field = fieldmath.BinaryField(0x11D)
	generator = 0x02
	rs = reed.ReedSolomon(field, generator, msglen, ecclen)

	encoded = rs.encode(data)
	return encoded

def reed_decode(data,ecclen):
	msglen = len(data) - ecclen
	field = fieldmath.BinaryField(0x11D)
	generator = 0x02
	rs = reed.ReedSolomon(field, generator, msglen, ecclen)

	decoded = rs.decode(data)
	return decoded





