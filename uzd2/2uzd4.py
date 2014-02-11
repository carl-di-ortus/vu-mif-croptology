#!/usr/bin/python3

abc = ['A','Ą','B','C','Č','D','E','Ę','Ė','F','G','H','I','Į','Y','J','K',
			'L','M','N','O','P','R','S','Š','T','U','Ų','Ū','V','Z','Ž']
cba = abc[:]


c = """GU OŽ ŪO UA PŽ MO ŲA LA ŽA ĮŽ OG EP ĘL ŪB ĖK LL SO AC ŲL MR DO
		JL NŲ ČK RZ ŲL IO AZ OA RK ŲL MR LŠ JK PA ŲU PŽ ŲL ĘP NE BO
		IN NP KI VB ŲU DN ĘP UA DL BR LI FA LR ŪŽ ZL UG GĮ FA UK ŪO
		ŽA SĘ VŽ VP JR TK KK CĘ IA ČĖ FA BA AG FF ŪO LO ĘC LN OG ČR
		LŠ OŽ ŪK ĮO ZĖ ŽG EP ČĖ YĖ PĘ IA ĄŽ ŪK TŲ SC IA ZO ĖK YI ĮG
		PG GŠ IO LA ĮC GU ŽA SĘ VŽ EK IA ĘL ĮA MŲ NP ĖG EP ĘL OZ YE
		FA GU FR KŽ ŪK LN KA SK ŲL CG UŪ IA JK ČY VŽ ŽT MR MA YE IA
		ŲO PA ŽA EA PŽ MO VU ŲN VP KI LR ŲO LA ŪK ĖZ ŲL VA ĄL BĖ TĘ
		ĮO VA ĘC ŲL VN CO MR JŽ ĮC EA VB OŽ ĘP AO BE PĘ UI ĮA JK EO
		SA ĖU ŲN YI ĮA JK EO ŠA ZŽ CF UG BA KA PŲ ĘL KA UL DL YE OĖ
		LR OŽ NP PL ĮR ZO ĄL LA ĄL NP UG KA TO ĮP KY NŲ ŲP UG OI ĮO
		KA ŲZ NP ĮO KN PĘ KI AC EA ŲT DL ŲĮ KG AĮ KA FA DŠ SG UL LA
		DO CŠ IĘ AZ LI SĖ LO LL ĘT MO ĘC FA UK ŲO HE JL AG UA DO CŠ
		EP KK ĘB JK ŪO VĘ MR PB ŲO LL GU AF IA IE ŲO LL KA PĖ LO GC
		IA VŠ SA ŲO TT MO ĮA ŲO ĮG HL ĮF EP SL NP ŠE TĘ ZR ĮG ŲA UŲ
		CL ZO ŠE EO ĘC ŲL GU DN TL LA UK LN LA ĮC EA ŲT DL ŲĮ PA ŽA
		PĮ VŠ SA CI OO GZ ĘN CO IŲ GU ČČ CŠ ĮG ĮA SG ŪK CĘ ZR JK ĖU
		IA ĘL KA VA ĘL ZŠ SA DH LO DO ĘT ĘP GH FO TK ŲT ĘP GH PI ČL
		LA KŽ ČV MU MM ŲP YS"""

c = c.replace(' ', '')
c = c.replace('\n', '')
c = c.replace('\t', '')

key = [['T','A'], ['V', 'S']]
det = abc.index('T') * abc.index('S') - abc.index('A') * abc.index('V')
atv = [[9, 0], [29, 7]]

ans = ""

for i in range(int(len(c)/2)):
	ans = ans + abc[(abc.index(c[i*2]) * 9 + 
					 abc.index(c[i*2+1]) * 29) % 32]
	ans = ans + abc[(abc.index(c[i*2]) * 0 + 
					 abc.index(c[i*2+1]) * 7) % 32]
	ans = ans + " "
	if (len(ans.replace('\n', ''))%72 == 0):
		ans = ans + "\n"
	
print(ans)
	
print("win")

