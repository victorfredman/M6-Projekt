import numpy as np
import random
def hämtaData(n, st):#Takes the type of coupon and number
    if st == "s" :
        st = "stryk"
    else:
        st = "topp"
    tips = np.loadtxt(f"{st}{n}.txt", delimiter=',')#Collects people percentage
    tipsOdds = np.loadtxt(f"{st}{n}odds.txt", dtype=float, delimiter=',')#Collects odds
    tipsProcent = oddsTillProcent(tipsOdds)#Converts odds to percentage, used as a probability for the games
    värdeBets = beräknaVärde(tipsProcent, tips)#List of value for each bet
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

def beräknaVärde(odds, folket):#Takes the probability and the people percentage as arguments
    värdeBets = np.empty((odds.shape[0], odds.shape[1]))#Creates an empty array, same size as the arguments
    for i in range(0,odds.shape[0]):#Nested for loop, range is the size of the arrays
        for x in range(0,odds.shape[1]):
            värdeBets[i, x] = odds[i, x]/folket[i, x]#Compares the lists index by index 
    return värdeBets#Returns the value of each bet as a new array
    

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
    
def slumpa(tipsProcent):#Takes the probability for the outcome of each game
    resultat = []#Creates a new list
    for i in range(0, tipsProcent.shape[0]):#Range is the amount of games
        svar = random.randint(1, 101)#Generates a random number from 1 to 100
        if svar <= tipsProcent[i, 0]:#If the number is less than the probability of a home win
            resultat.append("1")#1 means home win
        elif svar <= tipsProcent[i, 0] + tipsProcent[i, 1]:#If the number is less than the probability of home win + draw
            resultat.append("X")#X means draw
        else:#Else its an away win
            resultat.append("2")#2 means away win
    return resultat#returns a list with the result

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
        for i in range(1, tips.shape[0] + 1):
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
        resultat = slumpa(tipsProcent)
        skrivResultat(resultat, kupong, tips)
        print("Vill du spela igen? (j/n)")
        svar = str(input())
        if svar == "j" or svar == "J":
            start()
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

    hämtaData(nummer, strykTopp)
start()
