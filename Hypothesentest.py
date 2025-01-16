import scipy.stats as stats
from scipy.stats import norm
import numpy as np


def hypothesentests_pruefung():
    def auswahl_test():
        return int(input("1. Binomialtest: Überprüft, ob die Erfolgswahrscheinlichkeit einer binomialverteilten Stichprobe einem bestimmten Wert entspricht.\n"
                         "2. Z-Test: Überprüft Hypothese mittels Grundgesamtheit.\n"
                         "3. T-Test: Überprüft Hypothese mittels Stichprobe.\n"
                         "4. Mann-Whitney-U-Test: Ein nichtparametrischer Test zum Vergleich von zwei unabhängigen Stichproben.\n"
                         "5. Kolmogorov-Smirnov-Test: Vergleicht die Verteilung zweier Stichproben oder eine Stichprobe mit einer Referenzverteilung.\n"
                         "6.Willst du einen Stichprobenumfang berechnen können?\n"
                         "7. Willst du Entscheidungsgrenzen für α und oder β berechnen?\n"
                         "8. Willst du den Kritischen Erwartungswert berechnen?\n"
                         "Wählen Sie einen Test (1-8): "))


    def binomial_test():
        print("\nBinomialtest ausgewählt.")
        successes = int(input("Anzahl der Erfolge: "))
        trials = int(input("Anzahl der Versuche: "))
        prob = float(input("Erwartete Erfolgswahrscheinlichkeit: "))

        result = stats.binomtest(successes, n=trials, p=prob, alternative='two-sided')
        p_value = result.pvalue  # Extrahiere den P-Wert
        print(f"P-Wert: {p_value}")
        print(f"Interpretation: {'H0 ablehnen' if p_value < 0.05 else 'H0 nicht ablehnen'}")

    def z_test():
        print("\nZ-Test ausgewählt.")
        mean_sample = float(input("Stichprobenmittelwert: "))
        mean_population = float(input("Der gewünschte Mittelwert (Bsp. Ziel Gewicht eines Sackes): "))
        std_dev_population = float(input("standardabweichung: "))
        sample_size = int(input("Stichprobengröße: "))
        alpha = float(input("Signifikanzniveau (α, z.B. 0.05): "))

        se = std_dev_population / np.sqrt(sample_size)
        z = (mean_sample - mean_population) / se

        test_type = int(input(
            "Testtyp:\n"
            "1. Einseitig (größer)\n"
            "2. Einseitig (kleiner)\n"
            "3. Zweiseitig\n"
            "Wahl (1-3): "))

        # Berechnung des P-Werts für den Z-Test
        if test_type == 1:
            p_value = 1 - stats.norm.cdf(z)
        elif test_type == 2:
            p_value = stats.norm.cdf(z)
        else:
            p_value = 2 * (1 - stats.norm.cdf(abs(z)))

        print(f"Z-Wert: {z}")
        print(f"P-Wert: {p_value}")
        print(f"Interpretation: {'H0 ablehnen' if p_value < alpha else 'H0 nicht ablehnen'}")

        # Berechnung von Alpha-Fehler und Beta-Fehler
        # Kritischer Z-Wert
        z_crit = stats.norm.ppf(1 - alpha / 2)  # Für zweiseitigen Test
        alpha_error = stats.norm.cdf(z_crit - z)  # Alpha-Fehler

        # Berechnung des Beta-Fehlers (angenommener Mittelwert unter H1)
        mu_a = float(input("Der gewünschte Mittelwert unter H1 (Alternativhypothese): "))  # Populationsmittelwert unter H1
        beta_error = stats.norm.cdf(z_crit - (mu_a - mean_population) / se) - stats.norm.cdf(-z_crit - (mu_a - mean_population) / se)

        print(f"Alpha-Fehler (Fehler 1. Art, α): {alpha_error:.4f}")
        print(f"Beta-Fehler (Fehler 2. Art, β): {beta_error:.4f}")

    def t_test():
        print("\nT-Test ausgewählt.")
        test_type = int(input(
            "1. Ein-Stichproben-Test\n"
            "2. Zwei-Stichproben-Test (ungepaart)\n"
            "Wahl (1-2): "))
        alpha = float(input("Signifikanzniveau (α, z.B. 0.05): "))

        if test_type == 1:
            mean_sample = float(input("Stichprobenmittelwert: "))
            mean_population = float(input("Der gewünschte Mittelwert (Bsp. Ziel Gewicht eines Sackes): "))
            std_dev_sample = float(input("Stichprobenstandardabweichung: "))
            sample_size = int(input("Stichprobengröße: "))

            se = std_dev_sample / np.sqrt(sample_size)
            t = (mean_sample - mean_population) / se
            df = sample_size - 1
            p_value = 2 * (1 - stats.t.cdf(abs(t), df))
        else:
            sample1 = list(map(float, input("Werte der ersten Stichprobe (kommagetrennt): ").split(',')))
            sample2 = list(map(float, input("Werte der zweiten Stichprobe (kommagetrennt): ").split(',')))
            t, p_value = stats.ttest_ind(sample1, sample2)

        print(f"T-Wert: {t}")
        print(f"P-Wert: {p_value}")
        print(f"Interpretation: {'H0 ablehnen' if p_value < alpha else 'H0 nicht ablehnen'}")

    def mann_whitney_u_test():
        print("\nMann-Whitney-U-Test ausgewählt.")
        sample1 = list(map(float, input("Werte der ersten Stichprobe (kommagetrennt): ").split(',')))
        sample2 = list(map(float, input("Werte der zweiten Stichprobe (kommagetrennt): ").split(',')))
        alpha = float(input("Signifikanzniveau (α, z.B. 0.05): "))
        u_stat, p_value = stats.mannwhitneyu(sample1, sample2, alternative='two-sided')
        print(f"U-Wert: {u_stat}")
        print(f"P-Wert: {p_value}")
        print(f"Interpretation: {'H0 ablehnen' if p_value < alpha else 'H0 nicht ablehnen'}")

    def kolmogorov_smirnov_test():
        print("\nKolmogorov-Smirnov-Test ausgewählt.")
        sample1 = list(map(float, input("Werte der ersten Stichprobe (kommagetrennt): ").split(',')))
        sample2 = list(map(float, input("Werte der zweiten Stichprobe (kommagetrennt): ").split(',')))
        alpha = float(input("Signifikanzniveau (α, z.B. 0.05): "))
        ks_stat, p_value = stats.ks_2samp(sample1, sample2)
        print(f"KS-Wert: {ks_stat}")
        print(f"P-Wert: {p_value}")
        print(f"Interpretation: {'H0 ablehnen' if p_value < alpha else 'H0 nicht ablehnen'}")

    def berechne_stichprobenumfang():
        # Eingabe der erforderlichen Werte
        mu_0 = float(input("Geben Sie den behaupteten Mittelwert (mu_0) ein: "))
        x_bar = float(input("Geben Sie den beobachteten Mittelwert (x̄) ein: "))
        sigma = float(input("Geben Sie die bekannte Standardabweichung (sigma) ein: "))
        alpha = float(input("Geben Sie das Signifikanzniveau (alpha, z.B. 0.05) ein: "))

        # Berechnung des Unterschieds zwischen dem beobachteten Mittelwert und dem behaupteten Mittelwert
        delta = abs(x_bar - mu_0)

        # Berechnung des kritischen Z-Werts
        z_alpha = stats.norm.ppf(1 - alpha)

        # Berechnung des Stichprobenumfangs
        n = (z_alpha * sigma / delta) ** 2

        # Ausgabe des Ergebnisses
        print(f"\nDer benötigte Stichprobenumfang beträgt: {np.ceil(n)}")

    def find_threshold_alpha(mu1, sigma1, mu2, sigma2, sample_size, alpha):
        """
        Berechnet die Entscheidungsgrenze c für eine gegebene Irrtumswahrscheinlichkeit α (1. Art).

        :param mu1: Erwartungswert der ersten Normalverteilung (H0)
        :param sigma1: Standardabweichung der ersten Normalverteilung (H0)
        :param mu2: Erwartungswert der zweiten Normalverteilung (H1)
        :param sigma2: Standardabweichung der zweiten Normalverteilung (H1)
        :param sample_size: Stichprobenumfang n
        :param alpha: Irrtumswahrscheinlichkeit α
        :return: Entscheidungsgrenze c, Irrtumswahrscheinlichkeit β
        """
        sigma1_adjusted = sigma1 / np.sqrt(sample_size)
        sigma2_adjusted = sigma2 / np.sqrt(sample_size)
        c = norm.ppf(1 - alpha, loc=mu1, scale=sigma1_adjusted)
        beta = 1 - norm.cdf(c, loc=mu2, scale=sigma2_adjusted)
        return c, beta

    def find_threshold_beta(mu1, sigma1, mu2, sigma2, sample_size, beta):
        """
        Berechnet die Entscheidungsgrenze c für eine gegebene Irrtumswahrscheinlichkeit β (2. Art).

        :param mu1: Erwartungswert der ersten Normalverteilung (H0)
        :param sigma1: Standardabweichung der ersten Normalverteilung (H0)
        :param mu2: Erwartungswert der zweiten Normalverteilung (H1)
        :param sigma2: Standardabweichung der zweiten Normalverteilung (H1)
        :param sample_size: Stichprobenumfang n
        :param beta: Irrtumswahrscheinlichkeit β
        :return: Entscheidungsgrenze c, Irrtumswahrscheinlichkeit α
        """
        sigma1_adjusted = sigma1 / np.sqrt(sample_size)
        sigma2_adjusted = sigma2 / np.sqrt(sample_size)
        c = norm.ppf(beta, loc=mu2, scale=sigma2_adjusted)
        alpha = 1 - norm.cdf(c, loc=mu1, scale=sigma1_adjusted)
        return c, alpha

    def find_threshold_equal_alpha_beta(mu1, sigma1, mu2, sigma2, sample_size):
        """
        Berechnet die Entscheidungsgrenze c, wenn α = β gelten soll.

        :param mu1: Erwartungswert der ersten Normalverteilung (H0)
        :param sigma1: Standardabweichung der ersten Normalverteilung (H0)
        :param mu2: Erwartungswert der zweiten Normalverteilung (H1)
        :param sigma2: Standardabweichung der zweiten Normalverteilung (H1)
        :param sample_size: Stichprobenumfang n
        :return: Entscheidungsgrenze c, gemeinsame Irrtumswahrscheinlichkeit
        """
        sigma1_adjusted = sigma1 / np.sqrt(sample_size)
        sigma2_adjusted = sigma2 / np.sqrt(sample_size)

        # Berechnung der Entscheidungsgrenze c
        c = (mu1 * sigma2_adjusted + mu2 * sigma1_adjusted) / (sigma1_adjusted + sigma2_adjusted)
        #c = (mu1 / sigma1_adjusted ** 2 + mu2 / sigma2_adjusted ** 2) / (1 / sigma1_adjusted ** 2 + 1 / sigma2_adjusted ** 2)

        # Berechnung der Irrtumswahrscheinlichkeiten
        alpha = 1 - norm.cdf(c, loc=mu1, scale=sigma1_adjusted)
        beta = norm.cdf(c, loc=mu2, scale=sigma2_adjusted)

        return c, alpha, beta

    def find_sample_size(mu1, sigma1, mu2, sigma2, target_error):
        """
        Berechnet den benötigten Stichprobenumfang n, um α und β kleiner oder gleich target_error zu halten.

        :param mu1: Erwartungswert der ersten Normalverteilung (H0)
        :param sigma1: Standardabweichung der ersten Normalverteilung (H0)
        :param mu2: Erwartungswert der zweiten Normalverteilung (H1)
        :param sigma2: Standardabweichung der zweiten Normalverteilung (H1)
        :param target_error: Maximal erlaubte Irrtumswahrscheinlichkeit
        :return: Benötigter Stichprobenumfang n
        """
        # Berechnung des z-Werts für das gegebene Signifikanzniveau
        z = stats.norm.ppf(1 - target_error)

        # Berechnung des erforderlichen Stichprobenumfangs n
        n = ((z * (sigma1 + sigma2)) / (mu2 - mu1)) ** 2

        print(f"Der erforderliche Stichprobenumfang n ist {np.ceil(n):.0f}.")
        return

    def run_hypothesis_test():
        """
        Führt das Hypothesentestprogramm interaktiv aus.
        """
        print("Willkommen zum Hypothesentest-Tool!")

        mu1 = float(input("Geben Sie den Erwartungswert der ersten Verteilung (H0) ein: "))
        print(f"Erwartungswert der ersten Verteilung (H0): {mu1}")
        sigma1 = float(input("Geben Sie die Standardabweichung der ersten Verteilung (H0) ein: "))
        print(f"Standardabweichung der ersten Verteilung (H0): {sigma1}")
        mu2 = float(input("Geben Sie den Erwartungswert der zweiten Verteilung (H1) ein: "))
        print(f"Erwartungswert der zweiten Verteilung (H1): {mu2}")
        sigma2 = float(input("Geben Sie die Standardabweichung der zweiten Verteilung (H1) ein: "))
        print(f"Standardabweichung der zweiten Verteilung (H1): {sigma2}")
        sample_size = int(input("Geben Sie den Stichprobenumfang n ein: "))
        print(f"Stichprobenumfang n = {sample_size}")

        choice = int(input("Wählen Sie eine Option:\n"
                           "1: Entscheidungsgrenze c bei gegebenem α (1. Art)\n"
                           "2: Entscheidungsgrenze c bei gegebenem β (2. Art)\n"
                           "3: Entscheidungsgrenze c bei α = β\n"
                           "4: Benötigten Stichprobenumfang berechnen\n"
                           "Ihre Wahl (1-4): "))

        if choice == 1:
            alpha = float(input("Geben Sie die Irrtumswahrscheinlichkeit α ein: "))
            c, beta = find_threshold_alpha(mu1, sigma1, mu2, sigma2, sample_size, alpha)
            print(f"Entscheidungsgrenze c: {c:.2f}, Irrtumswahrscheinlichkeit β: {(1-beta):.4f}")
        elif choice == 2:
            beta = float(input("Geben Sie die Irrtumswahrscheinlichkeit β ein: "))
            c, alpha = find_threshold_beta(mu1, sigma1, mu2, sigma2, sample_size, beta)
            print(f"Entscheidungsgrenze c: {c:.2f}, Irrtumswahrscheinlichkeit α: {alpha:.4f}")
        elif choice == 3:
            c, alpha, beta = find_threshold_equal_alpha_beta(mu1, sigma1, mu2, sigma2, sample_size)
            print(f"Entscheidungsgrenze c: {c:.2f}, Gemeinsame Irrtumswahrscheinlichkeit: {alpha:.4f}")
        elif choice == 4:
            target_error = float(input("Geben Sie die maximal erlaubte Irrtumswahrscheinlichkeit ein: "))
            find_sample_size(mu1, sigma1, mu2, sigma2, target_error)
        else:
            print("Ungültige Auswahl. Bitte versuchen Sie es erneut.")

    def kritischer_erwartungswert():
        """
        Berechnet den kritischen Erwartungswert, um die Nullhypothese abzulehnen.

        Parameter:
        mu0 (float): Nullhypothese Erwartungswert
        sigma (float): Standardabweichung
        n (int): Stichprobengröße
        alpha (float): Signifikanzniveau
        operator (str): Vergleichsoperator ('<', '>', '<=', '>=')

        Rückgabe:
        float: Kritischer Erwartungswert der Laufleistung
        """
        mu0 = float(input("was ist Nullhypothese Erwartungswert:"))
        print(f"Erwartungswert= {mu0}")
        sigma = float(input("Standardabweichung sigma:"))
        print(f"Standardabweichung (sigma)={sigma}")
        n = int(input("Stichprobengrösse:"))
        print(f"Stichprobengrösse={n}")
        alpha = float(input("Signifikanzniveau (alpha):"))
        print(f"Signifikanzniveau (alpha)={alpha}")
        operator = str(input("Vergleichsoperator um H0 abzulehnen (umgekehrt zu H0) /anunehmen('<', '>', '<=', '>='):"))
        print(f"Vergleichsoperator: {operator}")
        if operator in ['<', '<=']:
            z_critical = stats.norm.ppf(alpha)
        elif operator in ['>', '>=']:
            z_critical = stats.norm.ppf(1 - alpha)
        else:
            raise ValueError("Ungültiger Operator. Verwenden Sie '<', '>', '<=' oder '>='.")

        mu_critical = mu0 + z_critical * (sigma / np.sqrt(n))
        print(mu_critical)

    test = auswahl_test()

    if test == 1:
        binomial_test()
    elif test == 2:
        z_test()
    elif test == 3:
        t_test()
    elif test == 4:
        mann_whitney_u_test()
    elif test == 5:
        kolmogorov_smirnov_test()
    elif test == 6:
        berechne_stichprobenumfang()
    elif test == 7:
        run_hypothesis_test()
    elif test == 8:
        kritischer_erwartungswert()

if __name__ == "__main__":
    hypothesentests_pruefung()
