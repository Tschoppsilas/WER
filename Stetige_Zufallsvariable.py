import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
import scipy.stats as stats
def normal_verteilung_berechnen():
    """
    Berechnet die Dichtefunktion (PDF), das Integral (CDF), den Erwartungswert (E[X])
    und die Varianz (Var[X]) für eine Normalverteilung oder eine benutzerdefinierte Dichte.
    Der Benutzer gibt die Werte für das Intervall für das Integral ein und die Funktion wird berechnet.

    Formeln:
    - Erwartungswert: E(X) = \int_{ - \infty }^\infty {x \cdot f(x)} \, dx
    - Varianz: Var(X) = \int_{ - \infty }^\infty {(x - E(X))^2 \cdot f(x)} \, dx
    """
    sicherheitsabfrage = input("Haben Sie bereits mu und sigma? (Ja=j, Nein=n): ").lower()

    if sicherheitsabfrage == "n":
        # Eingabe der Daten, für die die Dichte berechnet werden soll
        daten = np.array([float(i) for i in input("Geben Sie die Datenpunkte (getrennt durch Kommas) ein: ").split(",")])

        # Berechnung des Erwartungswertes (mu) aus den Daten
        mu = np.mean(daten)

        # Berechnung der Varianz (sigma^2) aus den Daten
        sigma_squared = np.var(daten)
        sigma = np.sqrt(sigma_squared)  # Standardabweichung

    elif sicherheitsabfrage == "j":
        # Eingabe von mu und sigma, wenn sie nicht aus den Daten berechnet werden sollen
        mu = float(input("Gib mu (Erwartungswert) ein: "))
        sigma = float(input("Gib sigma (Standardabweichung) ein: "))
        sigma_squared = sigma ** 2
        # Daten werden nicht benötigt, wenn mu und sigma direkt eingegeben werden
        daten = None

    else:
        print("Ungültige Eingabe. Bitte geben Sie 'j' für Ja oder 'n' für Nein ein.")
        return

    # Ausgabe des berechneten Erwartungswertes und der Varianz
    print(f"Berechneter Erwartungswert (mu): {mu}")
    print(f"Berechnete Standardabweichung (sigma): {sigma}")
    print(f"Berechnete Varianz (sigma^2): {sigma_squared}")

    # Berechnung der Dichtefunktion (PDF) für eine Normalverteilung
    def benutzer_dichte(x):
        return (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)

    # Eingabe für das Intervall des Integrals
    a = float(input(f"Geben Sie den unteren Wert des Intervalls (a) ein (Standardwert: {min(daten) if daten is not None else 0}): ") or (min(daten) if daten is not None else 0))
    b = float(input(f"Geben Sie den oberen Wert des Intervalls (b) ein (Standardwert: {max(daten) if daten is not None else 10}): ") or (max(daten) if daten is not None else 10))

    # Berechnung des Erwartungswerts aus der Dichte (E[X])
    def erwartungswert(dichte):
        result, _ = quad(lambda x: x * dichte(x), -np.inf, np.inf)
        return result

    # Berechnung der Varianz aus der Dichte (Var[X])
    def varianz(dichte, E_x):
        result, _ = quad(lambda x: (x - E_x) ** 2 * dichte(x), -np.inf, np.inf)
        return result

    # Berechnung des Erwartungswerts basierend auf der Dichte
    E_x = erwartungswert(benutzer_dichte)

    # Berechnung der Varianz basierend auf der Dichte
    var_x = varianz(benutzer_dichte, E_x)

    p_wahrscheinlichkeit = stats.norm.cdf(b, mu, sigma) - stats.norm.cdf(a, mu, sigma)

    perzentil = int(input("Welches Perzentil muss berechnet werden? (falls keines, einfach eine zahl angeben)"))
    quantil = stats.norm.ppf(perzentil/100, mu, sigma)

    p_standardisierung = stats.norm.cdf(1) - stats.norm.cdf(-1)

    # Ausgabe des Erwartungswerts und der Varianz, die mit der Dichte berechnet wurden
    print(f"Erwartungswert (E[X] aus Dichte): {round(E_x,2)}")
    print(f"Varianz (Var[X] aus Dichte): {round(var_x,2)}")
    print(f"Warscheinlichkeit: {round(p_wahrscheinlichkeit,2)}")
    print(f"Quantil: {round(quantil,2)}")
    print(f"standardisierte Warscheinlichkeit: {round(p_standardisierung,2)}")
    # Visualisierung der Dichtefunktion
    x = np.linspace(a, b, 1000)
    pdf_values = np.array([benutzer_dichte(xi) for xi in x])

    plt.plot(x, pdf_values, label="Dichtefunktion (PDF)")
    plt.title("Normalverteilung Dichtefunktion")
    plt.xlabel("x")
    plt.ylabel("Dichte")
    plt.grid(True)
    plt.legend()
    plt.show()

