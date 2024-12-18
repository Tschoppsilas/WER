import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import math


def exponential_verteilung_berechnen():
    """
    Berechnet die Dichtefunktion (PDF), die kumulierte Verteilungsfunktion (CDF),
    den Erwartungswert (E[X]), die Varianz (Var[X]), und die Wahrscheinlichkeit
    für einen gegebenen Intervall [a, b] für eine Exponentialverteilung.
    """

    # Eingabe des Parameters lambda
    lambda_ = float(input("Gib lambda (den Rate-Parameter) ein: "))
    print(f"Rate (Lambda): {lambda_}")
    # Berechnung des Erwartungswerts und der Varianz
    mu = 1 / lambda_  # Erwartungswert
    varianz = 1 / (lambda_ ** 2)  # Varianz

    print(f"Erwartungswert (E[X]): {mu}")
    print(f"Varianz (Var[X]): {varianz}")

    # 1. Dichtefunktion f(x) der Exponentialverteilung
    def dichtefunktion(x):
        return lambda_ * math.exp(-lambda_ * x)

    print(f"Dichtefunktion bei x = 1 {round(dichtefunktion(1),2)}")
    # 2. Kumulierte Verteilungsfunktion F(x)
    def cdf(x):
        return 1 - np.exp(-lambda_ * x)

    # 3. Wahrscheinlichkeit P(a <= X <= b)
    a = float(input("Gib die untere Grenze des Intervalls (a) ein: "))
    b = float(input("Gib die obere Grenze des Intervalls (b) ein: "))
    p_wahrscheinlichkeit = cdf(b) - cdf(a)

    # 4. Quantil: Bestimme das 90. Perzentil (P(X <= x) = 0.9)
    perzentil = int(input("Das wievielte Quantil soll berechnet werden?"))/100
    quantil_90 = stats.expon.ppf(perzentil, scale=1 / lambda_)

    # Ausgabe der Ergebnisse
    print(f"Wahrscheinlichkeit P({a} <= X <= {b}): {p_wahrscheinlichkeit:.4f}")
    print(f"Das {perzentil *100} Quantil: {quantil_90:.2f}")

    # Visualisierung der Dichtefunktion
    x = np.linspace(0, 5 * mu, 1000)  # Visualisierung für 5 * Erwartungswert
    pdf_values = lambda_ * np.exp(-lambda_ * x)

    plt.plot(x, pdf_values, label="Dichtefunktion (PDF)")
    plt.title("Exponentialverteilung Dichtefunktion")
    plt.xlabel("x")
    plt.ylabel("Dichte")
    plt.grid(True)
    plt.legend()
    plt.show()

