#!/usr/bin/python3

abc = ['A','Ą','B','C','Č','D','E','Ę','Ė','F','G','H','I','Į','Y','J',
		'K','L','M','N','O','P','R','S','Š','T','U','Ų','Ū','V','Z','Ž']
cba = abc[:]


c = """PBŽFM ĄMPFK PŠŠHN PŠŽVU YŠIĄI 
		PŠRZJ PERVL SOŽVP ĄMRFN JCEJE 
		HŠRLN JCMNV ĄCUĮI JCRFT FŪMSS 
		ĮFIBU IBIFK ĄIRCL YŠVFR ŲŠŽMA 
		IŠŽFK HŠTRK RĄEOA DUVFT ŽUCCN 
		YAPVI ĄBVĮA ĄDORO ČIMBA JRIYI 
		IŽAOU DNTLS ĄCNPO ĖĮHVU ŽMSFS 
		HĖŲCS TŠĄFŠ MIKLT FZRVK YAŠBA 
		JRIYI FIRHS ĮZMNI ĖOPVP FĄEPA 
		EŠAOD PEKCL ĄCŽFE IŠUĘN ŲLŪVU 
		ŽŠTĘI ĖEZUI YEVFŲ MMMBŲ ĖMŠVT 
		CDUIE ĄŠŪMA IŠŽVI DACFE ĖIVĮI 
		YIVRA ĄRŪCI TŠESŠ ĄIMMB ŲĄŪLČ 
		ĄIMLN ŲDEUO ŽMŪLS ĄAVŪI ĖŠUOS 
		DIMRY YAPVI ŲCĘĘE HĮPZŽ ĄŽMZJ 
		ĄMPVU IMTFA JCMVI GMŪOK PŠŽČN 
		PEPVP FBEĮA EŠUPŲ ČEROV ĄMVRU 
		DAZDS ĖMŲVG PLMKS ĄYIRO ĄŽJLR 
		ĘIFFJ FCHCP ĄVMVC ĄŲUOI HĄUOT 
		ĘAHCR ĖŠČJO PZDFU ČMKCR FŲMŪI 
		ĖŠEĘA EŠĖTT ĄVEŽA ĄLŪVS YŠZĮO 
		IPUNM FCRVI GCEĮO PŽKYA ĄYSLG 
		PŠRUE GOŽFO PDŪLD CDMBA HYSLG 
		ĄIARO DŠIYA ĄŪEF """

c = c.replace(' ', '')
c = c.replace('\n', '')
c = c.replace('\t', '')

key = ['P', 'I', 'E', 'V', 'A']
def attack():
	ans = ""
	for i in range(len(c)):
		ch = abc[ (abc.index(c[i]) - abc.index(key[i%len(key)])) % 32 ]
		ans = ans + ch
		if (len(ans.replace('\n', '').replace(' ', ''))%5 == 0):
			ans = ans + " "
		if (len(ans.replace('\n', '').replace(' ', ''))%60 == 0):
			ans = ans + "\n"
	print(ans)

def fragment(l):
	for i in range(len(c)-l):
		delta = 0
		tmp = c
		cut = tmp[i:i+l]
		occur = tmp.count(cut)
		print(cut, end=" ")
		for j in range(occur-1):
			prevoccur = tmp.find(cut)
			nextoccur = tmp.find(cut, delta+1)
			print(nextoccur-prevoccur, end=" ")
			tmp = tmp[nextoccur:]
		print()

def frequencies():
	testcases = []
	for i in range(len(key)):
		cases = int( len(c) / len(key) )
		if ( cases*len(key)+i < len(c) ):
			cases = cases + 1
		division = ""
		for j in range(cases):
			division = division + c[j*len(key)+i]
		testcases.insert(i, division[:])
	cba = [[""]*32]*5
	for i in range(len(key)):
		print(testcases[i])
		for j in range(len(abc)):
			cba[i][j] = testcases[i].count(abc[j])
		print(cba[i])

#frequencies()
attack()

print("win")

