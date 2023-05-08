from sympy import totient
from libnum import n2s

exec(open('chall.txt','r').read())

phi = totient(n)
d = pow(e,-1,int(phi))
print(n2s(pow(c,d,n)))
