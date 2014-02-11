#!/usr/bin/python3

abc = ['A','Ą','B','C','Č','D','E','Ę','Ė','F','G','H','I','Į','Y','J','K',
			'L','M','N','O','P','R','S','Š','T','U','Ų','Ū','V','Z','Ž']
cba = abc[:]

# in this cypher (k1, k2) = (15, 25)
#c = """ŪŠĮNKŽ IĖJNČ ĮĘĮRD ŠTĮĄF ŽDMNF IĮNPĮ TĘĮĮĄ FĮKYF
#		 CTĄKY ŪITĮC VMTĘT KĮRĮR FTĮĘN ĮMKCT ĮMONE ĮTŠĮM
#		 KTĮTF ĘNRMF TŠČGĮ TĮĘTŠ VRĮRĮ RFTĮC TPĮTĮ STKMĮ
#		 ŽIĮTĮ MĮČTS CTFTŠ ĮTĮJĮ RFŠTČ ĮCSĮT ĮCĮKN CĮTĮJ
#		 ĮRFŠT RNĄĮT ĮGNĘČ ĮCSĮT ĮGINU TĮOĮC FŠĮTĮ JHČHK
#		 DUTĮU ĮNĘMJ TCTRK ŽDUTĘ TKĮFL UĮĘDŠ TĮMIL ĮCJNC
#		 DMČTC SDMĖŠ HJDMK TĮCDČ DFTČJ NČĮĘĮ RTMIH FČLOŠ
#		 TPĮĖŠ ĮNKŽI DMVFĮ RĮDFŽ ŠKVCĮ RĮDĮC FTCĮR ĮDŽJČ
#		 HĘDOC DJCTĘ Ė """

# in this cypher (k1, k2) = (21, 22)
#c = """YSODCR ŽMODM USRER ČRTTR ŠŲZRČ CMŲOM TODUT JŠYŪD
#		UYOYZ ŲMTMY CĘTFT ĘMŲĖĘ TMOEM RDOCE RMKŪD UTUŽŪ
#		AHSMČ YJŠYŪ DUEČR DEMRS RČDUT MOYEU ŽRKUT TRSUŲ
#		MIŽĮŽ RŠĖLĮ MYEČR JYCMD ZCRJO ČRMMY KŠYMD ZCMCR
#		MJRŽR ČZSRM ERMĖM ČŽZLF MYCZS ĮEMOE ĄRŲUT JČMŽR
#		ČRDGM UTSRČ DUT"""

# in this cyper (k1, k2) = (21, 26)
c = """PEĖUOR ĖĘRŠV RĖUFZ NUVUŪ ŽRZVR OČZŽR VŽURG UVYRU
		ŲRVUR GRĘUV RĖŽUR ŲUVPZ PŠOUD UIAŲA ČBVVU ŽŠŽBF
		UOURV ŪGŪĖR URVGU ĖĘŪŠR FRNŠĖ ĘUOVŪ OJPEĖ ZVGUR
		NGUCU RVŠNU VUGBZ ŲRCRP ŪVFŠD RFUŪG URNPE ĖUUĘĖ
		ZCZVĘ UĖĘUR GŪĖRV ĘURIU RMFRĖ ZRMUŪ MĖZVO RIŽLR
		ĖFŪĘE NBUFĘ NUVŲR ĖŪVRZ CŠFRZ PRIĖŠ RĘURČ BIRFB
		PUVŽB NCUOU VRFŪZ ČŽZMG RUFYR ZŲBPZ ŪDVĘZ ĖZVŲR
		ĖŲBVG UĖĘGU ĖĘBOR VŲRVD ŲRŽIĘ ŠŽBCU OUPŪZ CUČŽR
		KIUFY RUUGR ORHOU FŠRŠM GUŪGR MŠFBP ŠĘĖŪN RFRZĖ
		UFCŪĘ RGTŪG ĖUŪVI UČUŽR ŪGJFŪ ŠRYRU ŪHGUO ČŪKJR
		ĖFŠĘR GBĘUO VŲŠYR ŪRGŠŽ RUŪFR FGŪRU ĘFŠMY RUŪGJ
		FZĖVČ ŠĘFŠI UŽRŪN UŽŠRV ĘRĖŪO NŠŽRZ ŲBPUV GUCRĖ
		FŠVĘR NĖŪVĘ ŪZPNU ĘUNIĖ ĮDĘLŽ URŲJV ĘUĖĘU FŪČBI
		UHŽUR ŲZFZV HRĖNŪ ĖNĘŠŽ RHVGA VĘBPU FYRJĖ AĘZOR
		IŽJŽU RŲUVŠ RFUČŠ ŲŠRGN ĖRŠMŲ BPJĖŠ ĘGUĖY RURVN
		UGŠRV CUOUV ĄUŽVJ FUGĘH OUYRU ŪGURN CŠIBĘ ZŽRMR
		UŪĖRF RUOŠG ĖUFĘŠ VŪZOR PZVŪZ VĘLNU MŲURV ĘBVRM
		UŪMŪV ŲBPUV ĖROVĘ UĘRGG UĖĘUR VNUCŲ ŠŽGRU ŽŠFIŲ
		UVČĖR KUVFŪ ZVĘUR IUNĖR UĖĘBP ŪVRZG ĖUFĘZ ĘZŽŪO
		ZPŠĘR ŠVNUY RUĄZĖ RKZFĘ ZŽRFR PUVĘE GVZVU ĖIAČR
		FRZŽU RŲZVR ŽŪŠĘU VVŪVR IEDĮV NRŽGU VUĘVĘ ŪORUF
		ĘRVŲR VURFŠ ĖŠRGU ŽRFIU VRĖVŲ ŠĘROU VMRŠO VŲUFC
		ŠFROV NŽŠFC ĖUČŪĖ BFŪGU ĖZRĖM FUĖBP ROUVŽ URŲŪI
		UŽAPŠ ŽRZŲB VRNŽR ŠVGRU VUŪŽB ĘŪMYR UOŠŲU VUĖZV
		CUFIŪ PŠRĖM ŲAVYR ZCUOZ VVUŲZ VGBYR URVFŠ DRFRU
		GŪĖRĖ RUVRO ŠCEKZ V """

c = c.replace(' ', '')
c = c.replace('\n', '')
c = c.replace('\t', '')

mstart = ['Į','L']

solved = False

# k1 must be coprime to m=32
def affine(k1, k2):
    for i in range(32):
        cba[i] = abc[ (k1*i + k2) % 32 ]

#k1 = 0
#k2 = 0
#while not solved:
#	ans = ""
#	k1 = int(input("iveskite k1: "))
#	k1 = k1+2
#	if (k1 % 2 == 0):
#		print("k1 turi buti nelyginis!")
#		continue
#	k2 = int(input("iveskite k2: "))
#	print()
#	affine(k1, k2)
	
for i in range(16):
	for j in range(32):
		ans = ""
		print()
		k1 = 2*i+1
		k2 = j
		affine(k1, k2)
		print(k1, k2, sep=", ")
		for k in range(len(c)):
			d = abc[cba.index(c[k])]
			ans = ans+d
			if ((k+1)%5 == 0):
				ans = ans+" "
			if ((k+1)%60 == 0):
				ans = ans+"\n"
		
		print(ans)
#			if input("ar galite perskaityti? (y/n): ")=='y':
#				solved = True
	
print("win")

