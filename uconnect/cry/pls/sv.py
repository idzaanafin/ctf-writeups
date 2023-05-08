from Crypto.Util.number import *
from string import printable
from math import gcd
from math import lcm
c = open('cipher','rb').read()
n = bytes_to_long(c[-1031:][::-1])
known='uconnect{'
cipher = list(filter(bool, c.split(b"\x00")))
nebak = []
for i in range(len(known)):
	p = bytes_to_long(cipher[i][::-1])//ord(known[i])
#	q = n //p
	nebak.append(p)
p1 = nebak[1] #sum(nebak) // len(known)
p0 = nebak[0]
p2 = nebak[2]
p3 = nebak[3]
p4 = nebak[4]
p5= nebak[5]
p6= nebak[6]
p7= nebak[7]
ps0 = p0 *ord('u')
ps1 = p1*ord('c')
ps2= p2 *ord('o')
ps3=p3 *ord('n')
ps4= p4 *  ord('n')
ps5 = p5 * ord('e')
ps6 = p6 * ord('c')
ps7 = p7 * ord('t')
selisih0= bytes_to_long(cipher[0][::-1])- ps0
selisih1 =  bytes_to_long(cipher[1][::-1])- ps1
selisih2 =  bytes_to_long(cipher[2][::-1])- ps2
selisih3 =  bytes_to_long(cipher[3][::-1])- ps3
selisih4 =  bytes_to_long(cipher[4][::-1])- ps4
selisih5 = bytes_to_long(cipher[5][::-1])- ps5
selisih6 = bytes_to_long(cipher[6][::-1])- ps6
selisih7= bytes_to_long(cipher[7][::-1])- ps7
#p = gcd(selisih1,selisih2)
print(lcm(selisih3,selisih2,selisih1,selisih0,selisih4,selisih5,selisih6,selisih7))
q = n//p
#print(p*ord('c')+q)
#print(gcd(nebak[0],n))
#print(q)
#print(bytes_to_long(cipher[1][::-1])//nebak[1])
#p = (bytes_to_long(cipher[1][::-1])-q)//99
#q = n //p
for i in range(len(cipher)-1):
	#try:
	oi = bytes_to_long(cipher[i][::-1])
#	for j in range(28,32):
#	p = oi//ord(known[i])
#	p = 150664828362495218926779209316188369257490979018904711757372221976841738409800927003193193525537741946600138536979615049161657070393258591692187415220659322149280672984897167660124505908563051333231687784489617298486084276503193344368224013094950555419952154196263968907854575108823086699131490410198081445992
	#q = n // p
	m =(oi-q)//p+2
#	try:
#		print(chr(m),end='')
#	print(oi.bit_length())
#	print(cipher[i])
#	except:
#		oi = bytes_to_long(cipher[i][::-1].ljust(129,b'\x00'))
#		m=((oi-q)//p+2)
#		print(m)
#		pass
	
#	if m ==0 :
#		oi = bytes_to_long(cipher[i][::-1].ljust(129,b'\x00'))
#		m=((oi-q)//p+2)
#		print(oi//p)
#		if m <= 127:
#			print(chr(m),end='')

#print(n)
#	if m == 0:
#	except:
#		p = nebak[0]
#		q= n//p
#		print(long_to_bytes(oi))
#	else:
#		print(chr(m))
#	print(f'p {p}')
#	print((oi)//p+2)
#	print(f'q {q}')
	#kali= p*ord(known[i])
	#print(p)
#	q = oi-kali
#	fpb = gcd(kali,oi)
#	print(fpb)
#	print(chr((oi-q)//p))
#print(printable[30])
