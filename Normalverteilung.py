import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.stats import norm

def normalverteilung_tool():
    """
    Ein umfassendes Tool zur Berechnung und Visualisierung von Normalverteilungen.
    Funktionen:
    - Berechnung von Wahrscheinlichkeiten (P(X <= x), P(X > x), P(a <= X <= b)).
    - Bestimmung von Quantilen (z.B. Perzentilen).
    - Visualisierung der Dichtefunktion.
    - Berechnung von Erwartungswert und Varianz aus der Dichtefunktion.
    """
    bekannt = input("Sind μ und σ bekannt? (Ja = j, Nein = n").lower()
    if bekannt == "n":
        x1 = int(input("Wie gross ist der X-Wert aus P(X<=x)?"))
        p1 = float(input("Gib die WK von P(X <= x) in Dezimalstellen ein"))
        x2 = int(input("Wie gross ist der X-Wert aus P(X>=x)?"))
        p2 = float(input("Gib die WK von P(X >= x) in Dezimalstellen ein"))
        z1 = norm.ppf(p1)  # z-Wert für P(X <= x1)
        z2 = norm.ppf(1 - p2)  # z-Wert für P(X >= x2)

        # Lösen des Gleichungssystems
        sigma = (x2 - x1) / (z2 - z1)
        mu = x1 - z1 * sigma
        print(f"μ = {mu} und σ = {sigma}")
        return
    # Eingabe der Verteilungsparameter
    standard_normal = input("Arbeiten Sie mit einer Standardnormalverteilung (μ = 0, σ = 1)? (j = ja/n = nein): ").strip().lower()

    if standard_normal == "j":
        mu = 0
        sigma = 1
    elif standard_normal == "n":
        mu = float(input("Geben Sie den Mittelwert (μ) ein: "))
        sigma = float(input("Geben Sie die Standardabweichung (σ) ein: "))
        if sigma <= 0:
            print("Die Standardabweichung muss größer als 0 sein.")
            return
    else:
        print("Ungültige Eingabe. Bitte starten Sie das Programm erneut und geben Sie 'j' oder 'n' ein.")
        return

    wahl = int(input("Wählen Sie eine Option (1-5):\n"
                     "1: Wahrscheinlichkeiten(P(X <= x), P(X < x), P(X > x), P(X >= x), P(a <= X <= b), \n"
                     "2: Bestimmung eines Quantils (z.B. Perzentil)\n"
                     "3: Visualisierung der Dichtefunktion\n"
                     "4: Berechnung von Erwartungswert und Varianz aus der Dichte\n"
                     "5: Berechnung des X-Wertes wenn ein Prozentsatz gegeben ist\n"
                     "0: Beenden\n"
                     "Ihre Auswahl: "))
    if wahl >5 :
        raise ValueError("Ungültige Eingabe. Bitte eine Zahl zwischen 0 und 6 eingeben.")

    if wahl == 0:
        print("Programm beendet.")
        return

    elif wahl == 1:
        check = int(input("Wählen Sie eine Option (1-6):\n"
                         "1: Wahrscheinlichkeit P(X <= x)\n"
                         "2: Wahrscheinlichkeit P(X > x)\n"
                         "3: Wahrscheinlichkeit P(a <= X <= b)\n"
                         "4: Wahrscheinlichkeit P(X >= x)\n"
                         "5: Wahrscheinlichkeit P(X < x)\n"
                          "ihre Wahl:"))
        if check == 1:
            x = float(input("Geben Sie den x-Wert ein: "))
            p = norm.cdf(x, mu, sigma)
            print(f"Die Wahrscheinlichkeit P(X <= {x}) beträgt: {p:.4f}")
        elif check == 2:
            x = float(input("Geben Sie den x-Wert ein: "))
            p = 1 - norm.cdf(x, mu, sigma)
            print(f"Die Wahrscheinlichkeit P(X > {x}) beträgt: {p:.4f}")

        elif check == 3:
            a = float(input("Geben Sie den unteren Wert a ein: "))
            print(f"mu = {mu}")
            print(f"sigma = {sigma}")
            print(f"a = {a}")
            b = float(input("Geben Sie den oberen Wert b ein: "))
            print(f"b = {b}")
            p = norm.cdf(b, mu, sigma) - norm.cdf(a, mu, sigma)
            print(f"Die Wahrscheinlichkeit P({a} <= X <= {b}) beträgt: {p:.4f}")

        elif check == 4:
            x = float(input("Geben Sie den x-Wert ein: "))
            p = 1 - norm.cdf(x, mu, sigma)
            print(f"Die Wahrscheinlichkeit P(X >= {x}) beträgt: {p:.4f}")

        elif check == 5:
            x = float(input("Geben Sie den x-Wert ein: "))
            p = norm.cdf(x, mu, sigma)
            print(f"Die Wahrscheinlichkeit P(X < {x}) beträgt: {p:.4f}")


    elif wahl == 2:
        perzentil = float(input("Geben Sie das gewünschte Perzentil (z.B. 95 für 95%) ein: "))
        quantil = norm.ppf(perzentil / 100, mu, sigma)
        print(f"Das {perzentil}%-Quantil beträgt: {quantil:.4f}")

    elif wahl == 3:
        a = float(input("Geben Sie den unteren Wert des Intervalls (a) ein: "))
        b = float(input("Geben Sie den oberen Wert des Intervalls (b) ein: "))
        x = np.linspace(a, b, 1000)
        pdf_values = norm.pdf(x, mu, sigma)
        plt.plot(x, pdf_values, label=f"Normalverteilung (μ={mu}, σ={sigma})")
        plt.title("Dichtefunktion der Normalverteilung")
        plt.xlabel("x")
        plt.ylabel("Dichte")
        plt.grid(True)
        plt.legend()
        plt.show()

    elif wahl == 4:
        def dichte(x):
            return (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)

        # Berechnung des Erwartungswerts
        def erwartungswert(dichte):
            result, _ = quad(lambda x: x * dichte(x), -np.inf, np.inf)
            return result

        # Berechnung der Varianz
        def varianz(dichte, E_x):
            result, _ = quad(lambda x: (x - E_x) ** 2 * dichte(x), -np.inf, np.inf)
            return result

        E_x = erwartungswert(dichte)
        var_x = varianz(dichte, E_x)

        print(f"Erwartungswert (E[X]): {E_x:.4f}")
        print(f"Varianz (Var[X]): {var_x:.4f}")
    elif wahl == 5:
        # Bestimmung des x-Werts für eine gegebene Wahrscheinlichkeit
        p = float(input("Geben Sie die Wahrscheinlichkeit (als Dezimalzahl) ein: (P(X<x) WK = 1-p"))
        if p <= 0 or p >= 1:
            print("Die Wahrscheinlichkeit muss zwischen 0 und 1 liegen.")
            return
        x = norm.ppf(p, mu, sigma)
        print(f"Der x-Wert, unter dem die besten {p*100:.1f}% der Werte liegen, beträgt: {x:.4f}")

    else:
        print("Ungültige Auswahl. Bitte wählen Sie eine Zahl zwischen 0 und 6.")
