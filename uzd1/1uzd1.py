#!/usr/bin/python3

# Skytalės šifro interaktyvus dešifravimas
# c - užšifruota žinutė
# Karolis Martinkus 2013-09-04

c="""NĖKUO NUPOS RSKUB ARPŪN OOUSS 
LTOJR VUOAI RŲUOK RUNAN ITAOČ 
ĘSERO UDINP RPKIR UOAEA SNĖOR 
MGSKT GSSAĖ IAVNN ŠTTDR AUAIY 
ĄŽŠKM IUTPI TAARR IAAAR SKPNV 
USUPA UUEGK SRILO ITAIO PIKKI 
DRNKA ASPNS OOILL RIKSK KNĄIE 
UĮSRO PGKBI DASAI OĖRUT AKMNJ 
GSĖUV TEAEU KLĖIL URLŪĘ PEASK 
YNIUS UKLSĄ ROGKU ĘSTPT RDBRL 
EOIAA ĖAĖČS GŽMJU GIARU AASĖA 
VYMSU """

c = c.replace(" ", "")
c = c.replace("\n", "")

solved = False

while not solved:
	iterations = int(input("įveskite rakto ilgį: "))
	
	for i in range(iterations):
		j=i
		while j<280:
			print(c[j], end='')
			j=j+iterations		
	
	query = input("\nar galite perskaityti? (y/n) ")
	if query=='y':
		solved=True

print("win")
