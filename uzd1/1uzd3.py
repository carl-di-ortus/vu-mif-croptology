#!/usr/bin/python3

# Perstatos šifras su nežinomu raktu
# Karolis Martinkus 2013-09-07

c="""ČOASI TRNRV DEIUA DBLII AYDĖ"""

c = c.replace(" ", "")
c = c.replace("\n", "")

solved = False

while not solved:
	cols = int(input("kiek stulpeliu: "))
	rows = int(len(c)/cols)
	
	key = []
	for i in range(cols):
		key.insert(i, int(input("stulpelio tvarka: ")))
	
	for i in range(rows):
		for j in range(cols):
			print(c[rows*key.index(j+1)+i], end="")
		print()
	
	if input("ar galite perskaityti? (y/n): ")=='y':
		solved = True

print("win")
