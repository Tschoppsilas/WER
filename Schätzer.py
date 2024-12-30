import numpy as np
import scipy.stats as stats


# Funktion zur Berechnung der Punktschätzung, Konfidenzintervall und Maximum Likelihood Schätzung
def schätzung(daten=None, mittelwert=None, std_abw=None):
    if daten is not None:
        # Punktschätzung
        erwartungswert = np.mean(daten)
        varianz = np.var(daten, ddof=1)
        std_abw = np.sqrt(varianz)
        n = len(daten)
        std_error = std_abw / np.sqrt(n)

        # Erfolgswahrscheinlichkeit (nur für binäre Daten)
        if np.all(np.isin(daten, [0, 1])):
            erfolgswahrscheinlichkeit = np.mean(daten)
        else:
            erfolgswahrscheinlichkeit = None
    else:
        # Wenn Mittelwert und Standardabweichung gegeben sind
        if mittelwert is None or std_abw is None:
            print("Mittelwert und Standardabweichung müssen angegeben werden.")
            return
        n = int(input("Wie groß ist die Stichprobengröße?"))
        std_error = std_abw / np.sqrt(n)
        erwartungswert = mittelwert
        erfolgswahrscheinlichkeit = None

    # Ausgabe der Punktschätzung
    print(f"Erwartungswert (Mittelwert der Daten): {erwartungswert}")
    print(f"Standardabweichung: {std_abw}")
    print(f"Standardfehler: {std_error}")
    if erfolgswahrscheinlichkeit is not None:
        print(f"Erfolgswahrscheinlichkeit: {erfolgswahrscheinlichkeit}")
    else:
        print("Die Erfolgswahrscheinlichkeit kann nur für binäre Daten berechnet werden (0 und 1).")

    # Berechnung des Konfidenzintervalls
    konfidenz = float(input("Gib das Konfidenzintervall in Dezimalstellen an (z.B. 0.95 für 95%): "))
    if konfidenz <= 0 or konfidenz >= 1:
        print("Ungültiges Konfidenzniveau. Es muss zwischen 0 und 1 liegen.")
        return

    z_value = stats.norm.ppf((1 + konfidenz) / 2)
    intervall = z_value * std_error
    untergrenze = erwartungswert - intervall
    obergrenze = erwartungswert + intervall

    print(f"{konfidenz * 100} % Konfidenzintervall: ({untergrenze}, {obergrenze})")

    if daten is not None:
        # Maximum Likelihood Schätzung für Mittelwert und Standardabweichung
        mu_mle = np.mean(daten)
        sigma_mle = np.std(daten, ddof=0)  # MLE für die Standardabweichung
        print(f"Maximum Likelihood Schätzung für den Mittelwert (mu): {mu_mle}")
        print(f"Maximum Likelihood Schätzung für die Standardabweichung (sigma): {sigma_mle}")
    else:
        print("Maximum Likelihood ist nicht möglich, da keine Daten vorhanden sind")
