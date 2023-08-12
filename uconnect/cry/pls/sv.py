from Crypto.Util.number import *
from string import printable
c = open('cipher','rb').read()
cipher = list(filter(bool, c.split(b"\x00\x00")))

n = bytes_to_long(cipher[-2][::-1])
c0= bytes_to_long(cipher[0][::-1])
c1 = bytes_to_long(cipher[1][::-1])
selisih_known= ord('u')-ord('c')

p = (c0-c1)//selisih_known
q= n // p
#xprint(cipher)
for i in range(len(cipher)-2):
	try:
		print(chr((bytes_to_long(cipher[i].replace(b'\x00',b'')[::-1])-q)//p),end='')
	except:
		print(' ',end='')
