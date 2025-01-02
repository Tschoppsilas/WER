import scipy.stats as stats
import numpy as np


def hypothesentests_pruefung():
    def auswahl_test():
        return int(input("1. Binomialtest: Überprüft, ob die Erfolgswahrscheinlichkeit einer binomialverteilten Stichprobe einem bestimmten Wert entspricht.\n"
                         "2. Z-Test: Vergleicht den Mittelwert einer Stichprobe mit einem bekannten Populationsmittelwert, wenn die Standardabweichung der Population bekannt ist.\n"
                         "3. T-Test: Testet Mittelwertunterschiede, entweder für eine Stichprobe oder zwei unabhängige Stichproben (ungepaart).\n"
                         "4. Mann-Whitney-U-Test: Ein nichtparametrischer Test zum Vergleich von zwei unabhängigen Stichproben.\n"
                         "5. Kolmogorov-Smirnov-Test: Vergleicht die Verteilung zweier Stichproben oder eine Stichprobe mit einer Referenzverteilung.\n"
                         "6.Willst du einen Stichprobenumfang berechnen können?\n"
                         "Wählen Sie einen Test (1-5): "))


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


if __name__ == "__main__":
    hypothesentests_pruefung()
