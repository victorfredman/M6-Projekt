import numpy as np
import random
def hämtaData(n):
    tips = np.loadtxt(f"topp{n}.txt", delimiter=',')
    tipsOdds = np.loadtxt(f"topp{n}odds.txt", dtype=float, delimiter=',')
    tipsProcent = oddsTillProcent(tipsOdds)
    värdeBets = beräknaVärde(tipsProcent, tips)
    play(tipsOdds, tipsProcent, tips, värdeBets)

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
        
def skrivResultat(resultat, kupong, tips):
        print("\nDin kupong:")
        for i in range(0, len(kupong)):
            print("Match", i+1, ": ", end='')    
            
            print(kupong[i])
        print("\nResultat:")    
        for i in range(0, len(kupong)):
            print("Match", i+1, ": ", end='')    
            
            print(resultat[i])
        print("Resultat:")
        rätt = jämförKupong(kupong, resultat)
        medelRätt = andelRätt(resultat, tips)
        print(f"Du hade {rätt} rätt!") 
        print(f"Medelvärdet var {medelRätt} rätt för den här kupongen!")       
    
def slumpa(tipsProcent, tips):
    resultat = []
    for i in range(0, tips.shape[0]):
        svar = random.randint(1, 101)
        if svar <= tipsProcent[i, 0]:
            resultat.append("1")
        elif svar <= tipsProcent[i, 0] + tipsProcent[i, 1]:
            resultat.append("X")
        else:
            resultat.append("2")
    return resultat

def jämförKupong(kupong, resultat):
    rätt = 0
    for i in range(0, len(kupong)):
        if kupong[i] == resultat[i]:
            rätt += 1
        
        
    return rätt

def andelRätt(resultat, tips):
    medelRätt = 0
    for i in range(0, len(resultat)):
        if resultat[i] == "1":
            medelRätt += tips[i, 0]/100
        elif resultat[i] == "X":
            medelRätt += tips[i, 1]/100
        else:
            medelRätt += tips[i, 2]/100
    medelRätt = round(medelRätt, 1)
    return medelRätt
            
    
    
def play(tipsOdds, tipsProcent, tips, värdeBets):  
    print("1. Se data för alla matcher")
    print("2. Lägga en kupong")
    print("3. Avsluta")

    val = input("Välj ett alternativ: ")
    if val == "1":
        skrivUt(tipsOdds, tipsProcent, tips, värdeBets)
        play(tipsOdds, tipsProcent, tips, värdeBets)
    elif val == "2":
        kupong = []
        for i in range(1, 9):
            print(f"Match {i} odds:")
            while True:
                svar = input("Vill du sätta 1, X eller 2? ")
                if svar == "x":
                    svar = svar.upper()
                if svar != "1" and svar != "2" and svar != "X":
                    print("Fel input! Skriv 1, X eller 2 ")
                    continue
                else:
                    kupong.append(svar)
                    break
        resultat = slumpa(tipsProcent, tips)
        skrivResultat(resultat, kupong, tips)
        print("Vill du spela igen? (j/n)")
        svar = input()
        if svar == "j" or svar == "J":
            play(tipsOdds, tipsProcent, tips, värdeBets)
        else:
            exit()

    elif val == "3":
        exit()
    else:
        print("Ogiltigt alternativ")
    
def start():
    print("Välkommen till Stryktipset!")
    while True:
        strykTopp = input("vill du spela stryktipset eller topptipset? (s/t)?")
        strykTopp = strykTopp.lower()
        if strykTopp != "s" and strykTopp != "t":
            print("Fel inmatning, skriv t eller s!")
            continue
        break
    while True:
        nummer = input("vilken gameweek vill du köra på? 1, 2 eller 3?")
        if nummer != "1" and nummer != "2" and nummer != "3":
            print("Fel inmatning, skriv 1, 2 eller 3!")
            continue
        break

    hämtaData(nummer)
start()
