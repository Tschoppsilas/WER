import numpy as np
import matplotlib.pyplot as plt


def gleichverteilung_berechnen():
    """
    Berechnet die Dichtefunktion, den Erwartungswert, die Varianz
    und die Wahrscheinlichkeit für die Gleichverteilung im Intervall [a, b].
    Der Benutzer gibt die Werte für das Intervall ein und alles wird berechnet.
    """

    # Eingabe des Intervalls [a, b]
    a = float(input("Geben Sie die untere Grenze a des Intervalls ein: "))
    b = float(input("Geben Sie die obere Grenze b des Intervalls ein: "))

    # Dichtefunktion (PDF)
    def dichte(x):
        if a <= x <= b:
            return 1 / (b - a)
        else:
            return 0

    # Erwartungswert
    erwartungswert = (a + b) / 2

    # Varianz
    varianz = ((b - a) ** 2) / 12

    # Wahrscheinlichkeitsberechnung für ein beliebiges Intervall [x1, x2]
    def wahrscheinlichkeit(x1, x2):
        if x1 < a: x1 = a
        if x2 > b: x2 = b
        if x1 >= x2:
            return 0
        return (x2 - x1) / (b - a)

    # Eingabe für das Intervall zur Wahrscheinlichkeitsberechnung
    x1 = float(input("Geben Sie den unteren Wert x1 für die Wahrscheinlichkeit ein: \n Falls keine Warscheinlichkeit gefragt wird, gib hier a erneut ein"))
    x2 = float(input("Geben Sie den oberen Wert x2 für die Wahrscheinlichkeit ein: \n Falls keine Warscheinlichkeit gefragt wird, gib hier b erneut ein"))

    # Berechnung der Wahrscheinlichkeit
    wahrscheinlichkeit_result = wahrscheinlichkeit(x1, x2)
    # Perzentil (Quantil) Berechnung
    p = int(input("Welches Quantil soll berechten werden: "))/100
    quantil = a + p * (b - a)

    # Ausgabe der Berechnungen
    print(f"Dichtefunktion f(x) im Intervall [{a}, {b}]:{round((1 / (b - a)),2)}")
    print(f"Erwartungswert E[X]: {(a + b) / 2}")
    print(f"Varianz Var[X]: {((b - a) ** 2) / 12}")
    print(f"Wahrscheinlichkeit, dass X im Intervall [{x1}, {x2}] liegt: {round(wahrscheinlichkeit_result,2)}")
    print(f"Das {p * 100}% Perzentil ist: {quantil}")

    # Visualisierung der Dichtefunktion
    x = np.linspace(a - 1, b + 1, 1000)
    y = np.array([dichte(xi) for xi in x])

    plt.plot(x, y, label="Dichtefunktion (PDF)")
    plt.fill_between(x, y, alpha=0.2)
    plt.title("Dichtefunktion der Gleichverteilung")
    plt.xlabel("x")
    plt.ylabel("Dichte")
    plt.grid(True)
    plt.legend()
    plt.show()


