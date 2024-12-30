import math
from scipy.stats import norm

def normalverteilung_berechnung():

    # Frage, ob es sich um die Standardnormalverteilung handelt
    standard_normal = input("Arbeiten Sie mit einer Standardnormalverteilung (μ = 0, σ = 1)? (j = ja/n = nein): ").strip().lower()

    if standard_normal == "j":
        mu = 0
        sigma = 1
    elif standard_normal == "n":
        # Eingabe des Mittelwerts (mu)
        mu = float(input("Geben Sie den Mittelwert (μ) ein: "))

        # Eingabe der Standardabweichung (sigma)
        sigma = float(input("Geben Sie die Standardabweichung (σ) ein: "))
        if sigma <= 0:
            print("Die Standardabweichung muss größer als 0 sein.")
            return
    else:
        print("Ungültige Eingabe. Bitte starten Sie das Programm erneut und geben Sie 'j' oder 'n' ein.")
        return

    wahl = int(input("Wählen Sie eine Option (1, 2, 3 oder 4): \n"
                     "1: Wahrscheinlichkeit P(X <= x) \n"
                     "2: Wahrscheinlichkeit P(X > x)\n"
                     "3: Wahrscheinlichkeit P(a <= X <= b)\n"
                     "4: Bestimmung des x-Werts für eine gegebene Wahrscheinlichkeit"))
    if wahl not in [1, 2, 3, 4]:
        print("Bitte geben Sie 1, 2, 3 oder 4 ein.")
        return

    if wahl == 1:
        # Wahrscheinlichkeit P(X <= x)
        x = float(input("Geben Sie den x-Wert ein: "))
        z = (x - mu) / sigma
        p = norm.cdf(z)
        print(f"Die Wahrscheinlichkeit P(X <= {x}) beträgt: {p:.4f}")
    elif wahl == 2:
        # Wahrscheinlichkeit P(X > x)
        x = float(input("Geben Sie den x-Wert ein: "))
        z = (x - mu) / sigma
        p = 1 - norm.cdf(z)
        print(f"Die Wahrscheinlichkeit P(X > {x}) beträgt: {p:.4f}")
    elif wahl == 3:
        # Wahrscheinlichkeit P(a <= X <= b)
        a = float(input("Geben Sie den unteren Wert a ein: "))
        b = float(input("Geben Sie den oberen Wert b ein: "))
        if a >= b:
            print("a muss kleiner als b sein.")
            return
        z_a = (a - mu) / sigma
        z_b = (b - mu) / sigma
        p = norm.cdf(z_b) - norm.cdf(z_a)
        print(f"Die Wahrscheinlichkeit P({a} <= X <= {b}) beträgt: {p:.4f}")
    elif wahl == 4:
        # Bestimmung des x-Werts für eine gegebene Wahrscheinlichkeit
        p = float(input("Geben Sie die Wahrscheinlichkeit (als Dezimalzahl) ein: "))
        if p <= 0 or p >= 1:
            print("Die Wahrscheinlichkeit muss zwischen 0 und 1 liegen.")
            return
        z = norm.ppf(p)
        x = z * sigma + mu
        print(f"Der x-Wert, unter dem die besten {p*100:.1f}% der Werte liegen, beträgt: {x:.4f}")
