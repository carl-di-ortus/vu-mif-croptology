#!/usr/bin/python3

abc = ['A','Ą','B','C','Č','D','E','Ę','Ė','F','G','H','I','Į','Y','J','K',
			'L','M','N','O','P','R','S','Š','T','U','Ų','Ū','V','Z','Ž']

c = """Z?æ??µ¼jÓ©"""
cbin = """01011010100010001110001101100111111000111010
			 00011010110100111101010101101100101110010101"""
mstart = """ge"""
keystart = """0011110111101101"""


cbin = cbin.replace(' ', '')
cbin = cbin.replace('\n', '')
cbin = cbin.replace('\t', '')

solved = False

binc = ' '.join(format(ord(x), 'b') for x in c)
binc = binc.replace(' ', '')

def srautas(pradzia, raktas):
	regs = []
	for c in pradzia:
		regs.append(c)
	key  = []
	for c in raktas:
		key.append(c)
	
	srt = ""
	for k in range(16):
		naujas = 0
		for l in range(len(key)-1):
			if (key[l] == '1'):
				naujas = int(regs[l]) ^ naujas
		for l in range(len(regs)-1):
			regs[l] = regs[l+1]
		srt = srt + regs[len(regs)-1]
		regs[len(regs)-1] = str(naujas)
	if (srt.startswith("0011110111101101")):
		return True
	else:
		return False
		

def generuoti(pradzia, raktas):
	regs = []
	for c in pradzia:
		regs.append(c)
	key  = []
	for c in raktas:
		key.append(c)
	
	srt = ""
	for k in range(len(cbin)):
		naujas = 0
		for l in range(len(key)-1):
			if (key[l] == '1'):
				naujas = int(regs[l]) ^ naujas
		for l in range(len(regs)-1):
			regs[l] = regs[l+1]
		srt = srt + regs[len(regs)-1]
		regs[len(regs)-1] = str(naujas)
	return srt

while not solved:
	reg = int(input("kiek yra registru: "))
	init = []
	for i in range(2**reg):
		for j in range(2**reg):
			if ( len('{:08b}'.format(int(i))[-reg:]) == reg):
				if ( len('{:08b}'.format(int(j))[-reg:]) == reg):
					if (srautas('{:08b}'.format(int(i))[-reg:], '{:08b}'.format(int(j))[-reg:]) ):
						stream = generuoti('{:08b}'.format(int(i))[-reg:], '{:08b}'.format(int(j))[-reg:])
						message = []
						for m in range(len(cbin)):
							message.append(str(int(cbin[m]) ^ int(stream[m])))	
						decr = ''.join(message)
						print(''.join(chr(int(decr[i:i+8], 2)) for i in range(0, len(decr), 8)), '{:08b}'.format(int(i))[-reg:], '{:08b}'.format(int(j))[-reg:])
#stream = generuoti("10111010100", "11011001100")
#stream = generuoti("11011000100", "11010001111")
	
	if input("ar galite perskaityti? (y/n): ")=='y':
		solved = True
	
print("win")

