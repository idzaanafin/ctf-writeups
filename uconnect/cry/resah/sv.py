from base64 import b64decode
from libnum import n2s
from random import choice
from Crypto.Util.number import *
from math import gcd
from math import lcm
dict = open('dicc.txt','r').readlines()
c = bytes_to_long(b64decode(open('flag.enc','r').read()))
dict = set(dict)
for p in dict:
	for q in dict:
		n= int(p)*int(q)
		phi= (int(p)-1)*(int(q)-1) 
		d = pow(65537,-1,phi)
		m = n2s(pow(c,d,n))
#		print(m)
#		print(p)
		if b'uconnect' in m:
			print(m)
			break
