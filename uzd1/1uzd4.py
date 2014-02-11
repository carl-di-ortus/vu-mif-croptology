#!/usr/bin/python3

# Geležinkelio tvorelės šifras su nežinomu aukščiu
# Karolis Martinkus 2013-09-07

c="""ESOMA NIPRU ESTGR LUIAM TGĖIM 
ČATČŲ IDSAN SKLUA ELROD AEAAD 
MISAV SAIUK RILYU UOASB MNUIE 
GETTU IAETP AEŠTD PITBI OK"""

c = c.replace(" ", "")
c = c.replace("\n", "")

solved = False

def fence(lst, numrails):
    fence = [[None] * len(lst) for n in range(numrails)]
    rails = list(range(numrails - 1)) + list(range(numrails - 1, 0, -1))
    for n, x in enumerate(lst):
        fence[rails[n % len(rails)]][n] = x

    if 0: # debug
        for rail in fence:
            print(''.join('.' if c is None else str(c) for c in rail))

    return [c for rail in fence for c in rail if c is not None]

def encode(text, n):
    return ''.join(fence(text, n))

def decode(text, n):
    rng = range(len(text))
    pos = fence(rng, n)
    return ''.join(text[pos.index(n)] for n in rng)

while not solved:
	h = int(input("koks tvorelės aukštis: "))
	print(decode(c, h))
	if input("ar galite perskaityti? (y/n): ")=='y':
		solved = True

print("win")
