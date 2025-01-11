import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import math

def exponential_verteilung_berechnen():
    """
    Berechnet die Dichtefunktion (PDF), die kumulierte Verteilungsfunktion (CDF),
    den Erwartungswert (E[X]), die Varianz (Var[X]), und die Wahrscheinlichkeit
    für ein gegebenes Intervall [a, b], eine "mindestens"-Wahrscheinlichkeit
    oder eine "maximal"-Wahrscheinlichkeit für eine Exponentialverteilung.
    """

    # Abfrage, ob der Benutzer lambda oder mu eingeben möchte
    choice_lambda = input(
        "Möchtest du den Rate-Parameter lambda oder den Erwartungswert mu eingeben? (l = lambda/m = mu): ").lower()

    if choice_lambda == 'l':
        # Eingabe von lambda direkt
        lambda_ = float(input("Gib den Rate-Parameter lambda ein: "))
        print(f"Rate (Lambda): {lambda_}")
        mu = 1 / lambda_  # Berechnung von mu
        print(f"Erwartungswert (E[X]): {mu}")
    elif choice_lambda == 'm':
        # Eingabe von mu und Berechnung von lambda
        mu = float(input("Gib den Erwartungswert mu ein: "))
        lambda_ = 1 / mu  # Berechnung von lambda
        print(f"Rate (Lambda): {lambda_}")
    else:
        print("Ungültige Eingabe! Bitte wähle 'lambda' oder 'mu'.")
        return
    varianz = 1 / (lambda_ ** 2)  # Varianz

    print(f"Erwartungswert (E[X]): {mu}")
    print(f"Varianz (Var[X]): {varianz}")

    # 1. Dichtefunktion f(x) der Exponentialverteilung
    def dichtefunktion(x):
        return lambda_ * math.exp(-lambda_ * x)

    print(f"Dichtefunktion bei x = 1 {round(dichtefunktion(1), 2)}")
    # 2. Kumulierte Verteilungsfunktion F(x)
    def cdf(x):
        return 1 - np.exp(-lambda_ * x)

    # Abfrage, ob ein Intervall, "mindestens" oder "maximal" berechnet werden soll
    choice = input("Möchtest du eine Wahrscheinlichkeit für ein Intervall [a, b],\n "
                   "für 'mindestens' eine bestimmte Zahl oder 'maximal' eine Zahl berechnen? \n"
                   "(int = intervall/min = mindestens/max = maximal): ").lower()

    if choice == 'int':
        # 3. Wahrscheinlichkeit P(a <= X <= b)
        a = float(input("Gib die untere Grenze des Intervalls (a) ein: "))
        b = float(input("Gib die obere Grenze des Intervalls (b) ein: "))
        p_wahrscheinlichkeit = cdf(b) - cdf(a)
        print(f"Wahrscheinlichkeit P({a} <= X <= {b}): {round((p_wahrscheinlichkeit*100),2)}%")

    elif choice == 'min':
        # 4. Wahrscheinlichkeit P(X >= x)
        grenze = float(input("Mit welcher Wahrscheinlichkeit grösser als?"))
        p_wahrscheinlichkeit = 1 - cdf(grenze)
        print(f"Wahrscheinlichkeit:{round((p_wahrscheinlichkeit*100),2)}%")

    elif choice == 'max':
        # 5. Wahrscheinlichkeit P(X <= b)
        grenze = float(input("Mit welcher Wahrscheinlichkeit kleiner als?"))
        p_wahrscheinlichkeit = cdf(grenze)
        print(f"Wahrscheinlichkeit:{round((p_wahrscheinlichkeit*100),2)}%")

    else:
        print("Ungültige Eingabe! Bitte wähle 'intervall', 'mindestens' oder 'maximal'.")

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

