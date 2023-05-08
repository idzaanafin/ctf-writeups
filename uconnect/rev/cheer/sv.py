from base64 import b64decode
from pwn import xor

known = b'uconnect{'
c = b64decode(open('encrypted.txt','r').read())

#print(xor(known,c[:len(known)]))
key = b'teman_lama'
#print(''.join([chr(c[i]^ord(key[i%len(key)])) for i in range(len(c))]))
print(xor(key,c))
