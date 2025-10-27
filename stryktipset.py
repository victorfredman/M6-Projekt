import numpy as np

def hämtaData():
    tips = np.loadtxt("topp2.txt", delimiter=',')
    tipsOdds = np.loadtxt("topp2odds.txt", dtype=float, delimiter=',')
    tipsProcent = oddsTillProcent(tipsOdds)
    värdeBets = beräknaVärde(tipsProcent, tips)
    skrivUt(tipsOdds, tipsProcent, tips, värdeBets)

def oddsTillProcent(odds):
    oddsProcent = np.empty((odds.shape[0], 3))
    for i in range(0,odds.shape[0]):
        sportbookMarginal = 0
        for x in range(0,odds.shape[1]):
            oddsProcent[i, x] = (1/odds[i, x])*100
            sportbookMarginal += oddsProcent[i, x]
        konvertera = sportbookMarginal/100
        for x in range(0,odds.shape[1]):
            oddsProcent[i, x] = oddsProcent[i, x]/konvertera
    return oddsProcent

def beräknaVärde(odds, folket):
    total = 0.7
    sannorlikhet = 1
    värdeBets = np.empty((odds.shape[0], odds.shape[1]))
    högstaVärde = np.empty((odds.shape[0], 3))
    for i in range(0,odds.shape[0]):
        for x in range(0,odds.shape[1]):
            värdeBets[i, x] = odds[i, x]/folket[i, x]
            if x >= 1:
                if värdeBets[i, x-1] <= värdeBets[i, x]:
                    högstaVärde[i, 0] = värdeBets[i, x]
                    högstaVärde[i, 1] = x
                    högstaVärde[i, 2] = odds[i, x]
            else:
                högstaVärde[i, 0] = värdeBets[i, x]
                högstaVärde[i, 1] = x
                högstaVärde[i, 2] = odds[i, x]
    for i in range(0,odds.shape[0]):
        total = total*högstaVärde[i, 0]
        sannorlikhet = sannorlikhet*högstaVärde[i, 2]/100
    return värdeBets
    

def skrivUt(odds, oddsProcent, folkProcent, värdeBets):
    kupong = []
    
    for i in range(0, odds.shape[0]):
        print(f"Match {i+1} odds:")
        for x in range(0,odds.shape[1]):
            print(odds[i, x]," ", end='')
        print()
        print("Sannorlikhet:")
        for x in range(0,odds.shape[1]):
            print(f"{round(oddsProcent[i, x], 1)}% ", end='')
        print()
        print("Andel bets lagda")
        for x in range(0,odds.shape[1]):
            print(f"{folkProcent[i, x]}% ", end='')
        print()
        print("förväntat värde på 1X2")
        for x in range(0,odds.shape[1]):
            print(f"{round((värdeBets[i, x]-1)*100, 1)}% ", end='')
        print()
        print()
        while True:
            svar = input("Vill du sätta 1, X eller 2?")
            if svar != "1" and svar != "2" and svar != "x" and svar != "X":
                print("skriv 1, X eller 2")
                continue
            else:
                kupong.append(svar)
                break
    print(kupong)

"""def hämtaInput(svar):
    bet = 0
    if svar == "x" or svar == "X":
        bet = 1
    elif svar == "1":
        bet = 0
    elif svar == "2":
        bet = 2
    else:
        return -1
    return bet"""


hämtaData()
