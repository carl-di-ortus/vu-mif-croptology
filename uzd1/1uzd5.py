#!/usr/bin/python3

# Fleissnerio šifras 4x4 su daliniu raktu (brute-force)
# Karolis Martinkus 2013-09-07

#c="""tage vntr eaoe tara"""
c="""IMII KĄAU ETAS ČTPA 
NILS IKEP YČVA DAĖI 
DAAP ĖUSU UUČK ASIŽ 
ILSI ŠIKO KLSP TLIA 
RIYS IDŪK IIČY SAAI"""

c = c.replace(" ", "")
c = c.replace("\n", "")

# key = [1, 5, 11]
# 4 possibilities for last hole - 2, 8, 9, 15
key = [ [[1, 2, 5, 11], [7, 9, 13, 14], [6, 12, 15, 16], [3, 4, 8, 10]],
	[[1, 5, 8, 11], [2, 7, 13, 14], [6, 9, 12, 16], [3, 4, 10, 15]],
	[[1, 5, 9, 11], [7, 13, 14, 15], [6, 8, 12, 16], [2, 3, 4, 10]],
	[[1, 5, 11, 15], [7, 8, 13, 14], [2, 6, 12, 16], [3, 4, 9, 10]] ]

solved = False
keyused = 0
while not solved:
	cube = ['','','','', '','','','', '','','','', '','','','']
	ans = []
	for i in range(int(len(c)/16)):
		for j in range(4):
			for k in range(4):
				cube[j*4+k] = c[i*16+key[keyused][j][k]-1]
		ans.insert(len(ans), cube[:])
	
	for i in range(int(len(c)/16)):
		print(ans[i])
	
	if input("ar galite perskaityti? (y/n): ")=='y':
		solved = True
	keyused = keyused+1
	if keyused==4:
		print("išnaudoti visi variantai")
		solved = True

print("win")
