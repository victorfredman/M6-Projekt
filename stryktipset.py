import numpy as np

def hämtaData():
    tips = np.loadtxt("topp1.txt", delimiter=',')
    tipsOdds = np.loadtxt("topp1odds.txt", dtype=float, delimiter=',')
    tipsProcent = oddsTillProcent(tipsOdds)
    beräknaVärde(tipsProcent, tips)
    print(tipsOdds)
    print(tips)
    print(tips[3,2])

def oddsTillProcent(odds):
    oddsProcent = np.empty((8, 3))
    for i in range(0,8):
        sportbookMarginal = 0
        for x in range(0,3):
            oddsProcent[i, x] = (1/odds[i, x])*100
            sportbookMarginal += oddsProcent[i, x]
        konvertera = sportbookMarginal/100
        for x in range(0,3):
            oddsProcent[i, x] = oddsProcent[i, x]/konvertera
    return oddsProcent
    print(oddsProcent)

def beräknaVärde(odds, folket):
    värdeBets = np.empty((8, 3))
    for i in range(0,8):
        for x in range(0,3):
            värdeBets[i, x] = odds[i, x]/folket[i, x]
            
    print(värdeBets)
    
        
hämtaData()     