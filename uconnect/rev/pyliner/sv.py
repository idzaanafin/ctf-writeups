from hashlib import md5
from string import printable

flag = '<REDACTED>'
cipher = lambda c: ''.join(list(map(lambda i, j: md5(str(j+i).encode()).hexdigest() if i % 2 == 0 else md5(str(j^i).encode()).hexdigest(), range(len(c)), [ord(j) ^ ord(c[i+1]) if i % 2 == 0 else ord(j) ^ 0xbf for i,j in enumerate(c)])))
#print(f"uconnect{{{cipher(flag)}}}")


#enc = open('challs.txt','r').read()
enc = 'c51ce410c124a10e0db5e4b97fc2af393b8a614226a953a8cd9526fca6fe9ba57f39f8317fbdb1988ef4c628eba02591705f2172834666788607efbfca35afb34e732ced3463d06de0ca9a15b6153677979d472a84804b9f647bc185a877a8b5642e92efb79421734881b53e1e1b18b69b04d152845ec0a378394003c96da594c16a5320fa475530d9583c34fd356ef5eb163727917cbba1eea208541a643e7437693cfc748049e45d87b8c7d8b9aacd45fbc6d3e05ebd93369ce542e8f2322d182be0c5cdcd5072bb1864cdee4d3d6ee2c0be24560d78c5e599c2a9c9d0bbd2093f65e080a295f8076b1c5722a46aa2a597e50502f5ff68e3e25b9114205d4a1c383cd30b7c298ab50293adfecb7b1845fbc6d3e05ebd93369ce542e8f2322d3416a75f4cea9109507cacd8e2f2aefcbcbe3365e6ac95ea2c0343a2395834dda1d0c6e83f027327d8461063f4ac58a669adc1e107f7f7d035d7baf04342e1cafc490ca45c00b1249bbe3554a4fdf6fbec8ce6abb3e952a85b8551ba726a12278e296a067a37563370ded05f5a3bf3ec69adc1e107f7f7d035d7baf04342e1ca7cbbc409ec990f19c78c75bd1e06f21519f3cd308f1455b3fa09a282e0d496f472b32a1f754ba1c09b3695e0cb6cde7f091d584fced301b442654dd8c23b3fc97cbbc409ec990f19c78c75bd1e06f2153b8a614226a953a8cd9526fca6fe9ba53416a75f4cea9109507cacd8e2f2aefcfe131d7f5a6b38b23cc967316c13dae22723d092b63885e0d7c260cc007e8b9d0777d5c17d4066b82ab86dff8a46af6f'

a='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_'
b='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_'
splited = []
for i in range(0,len(enc),64):
	splited.append(enc[i:i+64])
tmp = ''
for j in splited:
	for k in printable:
		for c in printable:
			#if cipher(k+c) == j:
			m = cipher(k+c)
		#	print(j)
			if m == j:
				print(k+c,j)
				enc = enc.replace(j,k+c)
#			else:
	enc=enc.replace(j,' ')
#			else:
#				print('mboh')
#	if m == j:	
#		tmp += k+c
	#print(j)
print(enc)
#print(splited)
for i,j in enumerate(enc):
	if i%2 == 0:
		try:
			print(ord(j) ^ ord(c[i+1]))
		except:
			pass
	else:
		print(ord(j)^ 191)
#print()


