#!/usr/bin/python3

# Perstatos šriftas su žinomu raktu
# Karolis Martinkus 2013-09-04

c="""ERAIA LSADA RSIAT IPMRŠ UONAA 
JAAAS ĄINNŪ NSOPT TUEKO KISNU 
YPGIŪ ROVĖI NĖMKS ĘTSOL ŠE"""

c = c.replace(" ", "")
c = c.replace("\n", "")

key = "laukas"
rows = int(len(c)/len(key))

for i in range(rows):
	print(c[rows*3+i], c[rows*0+i], c[rows*5+i], c[rows*2+i],
			c[rows*1+i], c[rows*4+i], sep="")

print("\nwin")
