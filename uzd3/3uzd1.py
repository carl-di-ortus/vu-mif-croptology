#!/usr/bin/python3

abc = ['A','Ą','B','C','Č','D','E','Ę','Ė','F','G','H','I','Į','Y','J','K',
			'L','M','N','O','P','R','S','Š','T','U','Ų','Ū','V','Z','Ž']
cba = abc[:]


c = """RIHIE RIMYN SAVMA ŽERTD ĘISDA 
		SCMTI ĮŽOCO IMCDS VŽAFR CŠŲDA 
		JINTR FCŽĮT CVMĮL LRMFĄ RMMCI 
		VŽGDĄ JĖVOM ZCŽĘM LŠZRA BIHTŽ 
		KIMĖU LŪMIG VŽIKM ZCŽĘM VCŲTT 
		OCERE MITŽI ĘŠEYP VCŽTR LŲMFO 
		KMŽDK MIĖTI ĘAPŽĮ NIZĘT VŠZKA 
		JŠFDT VDEŲE IARDŲ MIŲDL BAŠOD 
		ĮIPĮK LTVDT CBŲDM ŠUŪTS RŠŲJI 
		FBŪŽI ĮČŠDN ĘIŽTR OŠEYG VEĖDA 
		KDMNŽ OŪSTN BOSĄV FCEKP VBEZO 
		ĮCEGU OFIJB VVMII OHEDS JIVFV 
		FMGDA JITĘT FŪEZT FMRJA PITMY 
		OŠVMI CŪVFA FDOMO IIVĘR VVEYĖ 
		OREND HDUĖA FŽUJS RŠIKA MŠŪHA 
		OŠVTT NAHĮJ VEŽJU OĄEMY NNVYĖ 
		BCIFY O"""

c = c.replace(' ', '')
c = c.replace('\n', '')
c = c.replace('\t', '')

key = ['V', 'I', 'E', 'T', 'A']

ans = ""

for i in range(len(c)):
	ch = abc[ (abc.index(c[i]) - abc.index(key[i % len(key)])) % 32 ]
	ans = ans + ch
	if (len(ans.replace('\n', '').replace(' ', ''))%5 == 0):
		ans = ans + " "
	if (len(ans.replace('\n', '').replace(' ', ''))%60 == 0):
		ans = ans + "\n"
	
print(ans)
	
print("win")

