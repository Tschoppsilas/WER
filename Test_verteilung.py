import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

def Testverteilung():
    """
    Berechnet die Dichtefunktion (PDF) und die kumulierte Verteilungsfunktion (CDF) für die Binomialverteilung.
    Gibt die einzelnen und kumulierten Wahrscheinlichkeiten aus und visualisiert die Dichtefunktion.
    """
    # Eingabe der Parameter für die Binomialverteilung
    n = int(input("Gib n (Anzahl der Versuche) ein: "))
    p = (float(input("Gib p (Wahrscheinlichkeit für Erfolg) in % ein: "))/100)

    # Sicherstellen, dass p im gültigen Bereich ist
    if p < 0 or p > 1:
        print("Ungültige Wahrscheinlichkeit! p muss zwischen 0 und 1 liegen.")
        return

    # Berechnung der Wahrscheinlichkeitsverteilung (PDF) und der kumulierten Verteilung (CDF)
    k_max = n  # Maximale Anzahl der Erfolge (k) in der Binomialverteilung
    k = np.arange(0, k_max + 1)  # Werte von k (Anzahl der Erfolge)

    # Berechnung der Binomialwahrscheinlichkeiten (Dichtefunktion)
    pdf_values = binom.pmf(k, n, p)

    # Berechnung der kumulierten Binomialwahrscheinlichkeiten
    cdf_values = binom.cdf(k, n, p)

    # Ausgabe der einzelnen Wahrscheinlichkeiten (Dichtefunktion)
    print(f"{'k':<5} {'P(X=k) (PDF) in %':<20} {'P(X<=k) (CDF) in %'}")
    print("-" * 50)
    for i in range(len(k)):
        print(f"{k[i]:<5} {(pdf_values[i]*100):<20.2f} {(cdf_values[i]*100):<20.2f}")

    # Visualisierung der Wahrscheinlichkeitsverteilung
    plt.figure(figsize=(10, 6))
    plt.bar(k, (pdf_values*100), alpha=0.7, color='blue', label='Wahrscheinlichkeitsverteilung (P(X=k))')
    plt.step(k, (cdf_values*100), where='mid', color='red', label='Kumulierte Wahrscheinlichkeitsverteilung (P(X<=k))', linewidth=2)
    plt.title(f'Binomialverteilung (n={n}, p={(p*100)}%)')
    plt.xlabel('k (Anzahl der Erfolge)')
    plt.ylabel('Wahrscheinlichkeit (%)')
    plt.xticks(k)
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()



