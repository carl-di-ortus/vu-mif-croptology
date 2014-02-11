#!/usr/bin/python3

abc = ['A','Ą','B','C','Č','D','E','Ę','Ė','F','G','H','I','Į','Y','J','K',
			'L','M','N','O','P','R','S','Š','T','U','Ų','Ū','V','Z','Ž']
cba = abc[:]


c = """VUČLŪ ŪGUDD NIGTŽ ŠKSUI FFILZ 
		TŽVIK HLŽĄN LŲIJG ALGPG PRCCA 
		ŽGAĮG UGLSV VTŽSE GCAČŽ SĄGLI 
		TDŽŲK NGSVV SIŽOĄ GLITD ŽŲKNG 
		EYČMT ŠIGRN CDSHO AČLRO REEDI 
		ĮUIID SVVSI DNKRS DHNCV IEPAY 
		JĖŠŽL ŽŽRŽŪ IFRNŽ DUĘHK NGACĄ 
		EGDKC GUKNT SČTĮL MVVAG NRSŪE 
		ČTDĮG MŽVKS ĄIHHS FMSKL SSĄMT 
		ŠAYŽE FGĖFU AŠLRĘ ZKŽŽJ CĄPNZ 
		SYGVT GEĘŲA FŽOKD RTDLC ĖMNŪS 
		CČRFH AĖRZD DSFZD TŲNSĄ PĘŪTF 
		ZDTŲN SĄECŪ PĮKSŽ TNCĖM NŪIFŽ 
		RTŪIH VILSA YRRID IICOČ LALŪE 
		ČTDĮG MNGEK KKINV SRIŠL LCTOG 
		GRSŪO GUAOK ICŪLS RIFYI ĖŪAŽL 
		ŠOKRG ZACĄV ŽGUĮR AŽŪIĮ RŠKDR 
		OMJĮŪ IHŪAC LMĮGU ŠTNHĄ BĮŲĖY 
		ŽRŽŠC SĄAEZ RSČSK TMVAS ĘDPHU 
		AČLPY MSMLR ĄGIDH LHJRN SAKGI 
		ŽVPSF IEZIY GTVDI ĖGPFL EĘGIH 
		ZACFM ĘŠIEG INŲTC ŪUŽLR GKTŠŲ 
		ALOUŽ DBYČR ŠLŠĘR TFTŠĘ RMNLI 
		ĮAEŽP AĖGVŽ SACEK ŽVKHĄ MNRDH 
		ĄAHDR HĄIFŪ NSAGČ LACŪE ČTDĮG 
		MN """

c = c.replace(' ', '')
c = c.replace('\n', '')
c = c.replace('\t', '')

key = ['G', 'A', 'N', 'D', 'A', 'S']

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

