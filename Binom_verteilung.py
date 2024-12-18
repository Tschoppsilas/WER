import math
def Binominialverteilung():

    n = int(input("n (anzahl versuche / total vorhanden)"))
    k = int(input("k (Die Anzahl der Erfolge / im Poker die grösser der Hand (bsp 5 Karten = 1 Hand)"))
    p = float(input("Wahrscheinlichkeit in % für erfolg"))/100
    resultat = math.comb(n, k) * (p**k) * ((1-p)**(n-k)) *100
    print(f"{resultat}%")
    erwartungswert = n*p
    print(f"Erwartungswert E(X): {erwartungswert}")
    varianz = erwartungswert *(1-p)
    print(f"Varianz: {varianz}")
