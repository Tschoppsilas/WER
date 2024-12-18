import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson


def poisson_verteilung():

    lam = float(input("Geb den Wert des Erwartungswert E(X) ein:"))
    k_max = int(input("Gib das Maximale k (Anzahl der Ereignisse), welche betrachtet werden ein"))
    # Werte von k (Anzahl der Ereignisse)
    k = np.arange(0, k_max + 1)

    # Berechnung der Wahrscheinlichkeitsverteilung
    wahrscheinlichkeit = poisson.pmf(k, lam)

    # Berechnung der kumulierten Wahrscheinlichkeitsverteilung
    kumulierte_wahrscheinlichkeit = poisson.cdf(k, lam)

    # Tabellarische Ausgabe der Ergebnisse
    print(
        f"{'k':<5} {'Wahrscheinlichkeitsverteilung (P(X=k))':<40} {'Kumulierte Wahrscheinlichkeitsverteilung (P(X≤k))'}")
    print("-" * 85)

    for i in range(len(k)):
        # Formatierte Ausgabe mit 4 Dezimalstellen für eine einheitliche Darstellung
        print(f"{k[i]:<5} {wahrscheinlichkeit[i]:<40.4f} {kumulierte_wahrscheinlichkeit[i]:<25.4f}")

    # Visualisierung der Wahrscheinlichkeitsverteilung
    plt.figure(figsize=(10, 6))
    plt.bar(k, wahrscheinlichkeit, alpha=0.7, color='blue', label='Wahrscheinlichkeitsverteilung (P(X=k))')
    plt.step(k, kumulierte_wahrscheinlichkeit, where='mid', color='red',
             label='Kumulierte Wahrscheinlichkeitsverteilung (P(X≤k))', linewidth=2)
    plt.title(f'Poisson-Verteilung (λ={lam})')
    plt.xlabel('k (Anzahl der Ereignisse)')
    plt.ylabel('Wahrscheinlichkeit')
    plt.xticks(k)
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

