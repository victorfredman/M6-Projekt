import numpy as np

def hämtaData():
    tips = np.loadtxt("topp2.txt", delimiter=',')
    tipsOdds = np.loadtxt("topp2odds.txt", dtype=float, delimiter=',')
    tipsProcent = oddsTillProcent(tipsOdds)
    beräknaVärde(tipsProcent, tips)
    print(tipsOdds)
    print(tips)
    print(tips[3,2])

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
    print(sannorlikhet*100)
    print(total)
    print(högstaVärde)

            
    print(värdeBets)
    
        
hämtaData()
    print(värdeBets)
    
        

    
