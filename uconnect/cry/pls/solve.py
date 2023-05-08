from z3 import *

from math import ceil

from Crypto.Util.number import *
from string import printable
c = open('cipher','rb').read()
n = bytes_to_long(c[-1031:][::-1])
cipher = list(filter(bool, c.split(b"\x00\x00")))
#n = bytes_to_long(cipher[-1][::-1])
oi = cipher[1][::-1]
#cipher = []
#for i in range(0,len(c),1031):
#	p = bytes_to_long(c[i:i+1031][::-1])
#	print(p.bit_length())
#cipher = bytes_to_long(c[1031:1031+1031][::-1])
p = bytes_to_long(oi)//ord('c')
q = n // p 
for i in cipher:
#for i in range(len(cipher)-2):
#	m= ((bytes_to_long(list(filter(bool, c.split(b"\x00\x00")))[i][::-1])-q)//p+2)
#	print(chr(m),end=' ')
#print(bytes_to_long(oi))
#print(p)
#print(c)
#	try:
	if bytes_to_long(i[::-1]).bit_length() <= 1032:
		mboh = bytes_to_long(i.ljust(1032-bytes_to_long(i[::-1]).bit_length(),b'\x00')[::-1])
	elif len(i) >= 1031 :
		print(i)
		mboh = bytes_to_long(i[:1031][::-1])
#	print(mboh)
	try:
		print(chr((mboh-q)//p+2))
	except: 
		pass
#	else:
#		try:
#			print(chr((bytes_to_long(i[::-1])-q)//p+2),end='')
#		except:
#			print('a')
		#print(i)
#	except:
#		print(' ',end='')
#print(c)



