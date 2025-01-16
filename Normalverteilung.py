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

    wahl = int(input("Wählen Sie eine Option (1-7):\n"
                     "1: Wahrscheinlichkeit P(X <= x)\n"
                     "2: Wahrscheinlichkeit P(X > x)\n"
                     "3: Wahrscheinlichkeit P(a <= X <= b)\n"
                     "4: Bestimmung eines Quantils (z.B. Perzentil)\n"
                     "5: Visualisierung der Dichtefunktion\n"
                     "6: Berechnung von Erwartungswert und Varianz aus der Dichte\n"
                     "7: Berechnung des X-Wertes wenn ein Prozentsatz gegeben ist\n"
                     "0: Beenden\n"
                     "Ihre Auswahl: "))
    if wahl >7 :
        raise ValueError("Ungültige Eingabe. Bitte eine Zahl zwischen 0 und 6 eingeben.")

    if wahl == 0:
        print("Programm beendet.")
        return

    elif wahl == 1:
        x = float(input("Geben Sie den x-Wert ein: "))
        p = norm.cdf(x, mu, sigma)
        print(f"Die Wahrscheinlichkeit P(X <= {x}) beträgt: {p:.4f}")

    elif wahl == 2:
        x = float(input("Geben Sie den x-Wert ein: "))
        p = 1 - norm.cdf(x, mu, sigma)
        print(f"Die Wahrscheinlichkeit P(X > {x}) beträgt: {p:.4f}")

    elif wahl == 3:
        a = float(input("Geben Sie den unteren Wert a ein: "))
        b = float(input("Geben Sie den oberen Wert b ein: "))
        p = norm.cdf(b, mu, sigma) - norm.cdf(a, mu, sigma)
        print(f"Die Wahrscheinlichkeit P({a} <= X <= {b}) beträgt: {p:.4f}")

    elif wahl == 4:
        perzentil = float(input("Geben Sie das gewünschte Perzentil (z.B. 95 für 95%) ein: "))
        quantil = norm.ppf(perzentil / 100, mu, sigma)
        print(f"Das {perzentil}%-Quantil beträgt: {quantil:.4f}")

    elif wahl == 5:
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

    elif wahl == 6:
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
    elif wahl == 7:
        # Bestimmung des x-Werts für eine gegebene Wahrscheinlichkeit
        p = float(input("Geben Sie die Wahrscheinlichkeit (als Dezimalzahl) ein: "))
        if p <= 0 or p >= 1:
            print("Die Wahrscheinlichkeit muss zwischen 0 und 1 liegen.")
            return
        z = norm.ppf(p)
        x = z * sigma + mu
        print(f"Der x-Wert, unter dem die besten {p*100:.1f}% der Werte liegen, beträgt: {x:.4f}")

    else:
        print("Ungültige Auswahl. Bitte wählen Sie eine Zahl zwischen 0 und 6.")
