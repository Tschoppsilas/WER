import scipy.stats as stats
from scipy.stats import norm
import numpy as np

def hypothesentests_pruefung():
    def auswahl_test():
        return int(input(
            "1. Binomialtest: Überprüft, ob die Erfolgswahrscheinlichkeit einer binomialverteilten Stichprobe einem bestimmten Wert entspricht.\n"
            "2. Z-Test: Überprüft Hypothese mittels Grundgesamtheit.\n"
            "3. T-Test: Überprüft Hypothese mittels Stichprobe.\n"
            "4. Mann-Whitney-U-Test: Ein nichtparametrischer Test zum Vergleich von zwei unabhängigen Stichproben.\n"
            "5. Kolmogorov-Smirnov-Test: Vergleicht die Verteilung zweier Stichproben oder eine Stichprobe mit einer Referenzverteilung.\n"
            "6. Willst du einen Stichprobenumfang berechnen können?\n"
            "7. Willst du Entscheidungsgrenzen für α und oder β berechnen?\n"
            "8. Willst du den Kritischen Erwartungswert berechnen?\n"
            "Wählen Sie einen Test (1-8): "))

    def binomial_test():
        print("\nBinomialtest ausgewählt.")
        successes = int(input("Anzahl der Erfolge: "))
        trials = int(input("Anzahl der Versuche: "))
        prob = float(input("Erwartete Erfolgswahrscheinlichkeit: "))

        result = stats.binomtest(successes, n=trials, p=prob, alternative='two-sided')
        p_value = result.pvalue
        print(f"P-Wert: {p_value}")
        print(f"Interpretation: {'H0 ablehnen' if p_value < 0.05 else 'H0 nicht ablehnen'}")

    def z_test():
        print("\nZ-Test ausgewählt.")
        mean_sample = float(input("Stichprobenmittelwert: "))
        mean_population = float(input("Der gewünschte Mittelwert: "))
        std_dev_population = float(input("Standardabweichung: "))
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

        if test_type == 1:
            p_value = 1 - stats.norm.cdf(z)
        elif test_type == 2:
            p_value = stats.norm.cdf(z)
        else:
            p_value = 2 * (1 - stats.norm.cdf(abs(z)))

        z_critical = stats.norm.ppf(1 - alpha / 2 if test_type == 3 else 1 - alpha)
        print(f"Z-Wert (Prüfgrösse): {z}")
        print(f"P-Wert: {p_value}")
        print(f"Kritische Grenze: ±{z_critical}")
        print(f"Interpretation: {'H0 ablehnen' if p_value < alpha else 'H0 nicht ablehnen'}")

    def t_test():
        print("\nT-Test ausgewählt.")
        test_type = int(input(
            "1. Ein-Stichproben-Test\n"
            "2. Zwei-Stichproben-Test (ungepaart)\n"
            "Wahl (1-2): "))
        alpha = float(input("Signifikanzniveau (α, z.B. 0.05): "))

        if test_type == 1:
            mean_sample = float(input("Stichprobenmittelwert: "))
            mean_population = float(input("Der gewünschte Mittelwert: "))
            std_dev_sample = float(input("Stichprobenstandardabweichung: "))
            sample_size = int(input("Stichprobengröße: "))

            se = std_dev_sample / np.sqrt(sample_size)
            t = (mean_sample - mean_population) / se
            df = sample_size - 1
            p_value = 2 * (1 - stats.t.cdf(abs(t), df))
            t_critical = stats.t.ppf(1 - alpha, df)
            print(f"T-Wert (Prüfgrösse): {t}")
            print(f"P-Wert: {p_value}")
            print(f"Kritische Grenzen: ±{t_critical}")
            print(f"Interpretation: {'H0 ablehnen' if p_value < alpha else 'H0 nicht ablehnen'}")
        else:
            sample1 = list(map(float, input("Werte der ersten Stichprobe (kommagetrennt): ").split(',')))
            sample2 = list(map(float, input("Werte der zweiten Stichprobe (kommagetrennt): ").split(',')))
            t, p_value = stats.ttest_ind(sample1, sample2)
            print(f"T-Wert (Prüfgrösse): {t}")
            print(f"P-Wert: {p_value}")
            print(f"Interpretation: {'H0 ablehnen' if p_value < alpha else 'H0 nicht ablehnen'}")

    def mann_whitney_u_test():
        print("\nMann-Whitney-U-Test ausgewählt.")
        sample1 = list(map(float, input("Werte der ersten Stichprobe (kommagetrennt): ").split(',')))
        sample2 = list(map(float, input("Werte der zweiten Stichprobe (kommagetrennt): ").split(',')))
        alpha = float(input("Signifikanzniveau (α, z.B. 0.05): "))
        u_stat, p_value = stats.mannwhitneyu(sample1, sample2, alternative='two-sided')
        print(f"U-Wert (Prüfgrösse): {u_stat}")
        print(f"P-Wert: {p_value}")
        print(f"Interpretation: {'H0 ablehnen' if p_value < alpha else 'H0 nicht ablehnen'}")

    def kolmogorov_smirnov_test():
        print("\nKolmogorov-Smirnov-Test ausgewählt.")
        sample1 = list(map(float, input("Werte der ersten Stichprobe (kommagetrennt): ").split(',')))
        sample2 = list(map(float, input("Werte der zweiten Stichprobe (kommagetrennt): ").split(',')))
        alpha = float(input("Signifikanzniveau (α, z.B. 0.05): "))
        ks_stat, p_value = stats.ks_2samp(sample1, sample2)
        print(f"KS-Wert (Prüfgrösse): {ks_stat}")
        print(f"P-Wert: {p_value}")
        print(f"Interpretation: {'H0 ablehnen' if p_value < alpha else 'H0 nicht ablehnen'}")

    def main():
        auswahl = auswahl_test()

        if auswahl == 1:
            binomial_test()
        elif auswahl == 2:
            z_test()
        elif auswahl == 3:
            t_test()
        elif auswahl == 4:
            mann_whitney_u_test()
        elif auswahl == 5:
            kolmogorov_smirnov_test()
        else:
            print("Ungültige Eingabe!")

    main()
