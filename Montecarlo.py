import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, binom

def monte_carlo_learning_tool():
    choice = int(input("1: Wahrscheinlichkeiten schätzen\n"
                       "2: Modellbildung\n"
                       "3: Konvergenz im Modell\n"
                       "4: Pseudozufallszahl erzeugen\n"
                       "Geben Sie die Nummer des gewünschten Themas ein: "))

    if choice == 1:
        print("\n=== Wahrscheinlichkeiten schätzen ===")
        num_trials = int(input("Geben Sie die Anzahl der Versuche ein: "))
        success_prob = float(input("Geben Sie die Erfolgswahrscheinlichkeit (zwischen 0 und 1) ein: "))
        alpha = float(input("Geben sie das Signifikanzniveau alpha ein (falls keines bekannt ist geben sie 0.05 ein):"))
        successes = np.random.binomial(1, success_prob, num_trials)
        estimated_prob = np.mean(successes)

        # Konfidenzintervall berechnen
        z = norm.ppf(1 - alpha / 2)
        margin_of_error = z * np.sqrt((estimated_prob * (1 - estimated_prob)) / num_trials)
        conf_interval = (estimated_prob - margin_of_error, estimated_prob + margin_of_error)

        print(f"Geschätzte Wahrscheinlichkeit: {estimated_prob:.4f}")
        print(f"{(1-alpha)*100}% Konfidenzintervall: {conf_interval}")

    elif choice == 2:
        print("\n=== Modellbildung ===")
        print("Welche Verteilung möchten Sie simulieren?")
        print("1: Normalverteilung")
        print("2: Binomialverteilung")

        choice = int(input("Welche Verteilung möchten Sie simulieren?\n"
                           "1: Normalverteilung -> In vielen natürlichen Prozessen und Messdaten (z. B. Körpergröße, Temperaturmessungen)\n"
                           "2: Binomialverteilung -> Modelliert die Anzahl der Erfolge in einer festen Anzahl von Bernoulli-Experimenten \n"))

        if choice == 1:
            mean = float(input("Geben Sie den Mittelwert der Verteilung ein: "))
            std_dev = float(input("Geben Sie die Standardabweichung ein: "))
            num_samples = int(input("Geben Sie die Anzahl der zu generierenden Zufallszahlen ein: "))

            samples = np.random.normal(mean, std_dev, num_samples)
            print(f"Generierte Zufallszahlen: {samples[:10]}...")

            plt.hist(samples, bins=30, density=True, alpha=0.6, color='g')
            xmin, xmax = plt.xlim()
            x = np.linspace(xmin, xmax, 100)
            p = norm.pdf(x, mean, std_dev)
            plt.plot(x, p, 'k', linewidth=2)
            plt.title("Normalverteilung")
            plt.show()

        elif choice == 2:
            n = int(input("Geben Sie die Anzahl der Versuche ein: "))
            p = float(input("Geben Sie die Erfolgswahrscheinlichkeit ein: "))
            num_samples = int(input("Geben Sie die Anzahl der zu generierenden Zufallszahlen ein: "))

            samples = np.random.binomial(n, p, num_samples)
            print(f"Generierte Zufallszahlen: {samples[:10]}...")

            plt.hist(samples, bins=range(min(samples), max(samples) + 1), density=True, alpha=0.6, color='b')
            plt.title("Binomialverteilung")
            plt.show()
        else:
            print("Ungültige Auswahl.")

    elif choice == 3:
        print("\n=== Konvergenz im Modell ===")
        num_simulations = int(input("Geben Sie die Anzahl der Simulationen ein: "))
        success_prob = float(input("Geben Sie die Erfolgswahrscheinlichkeit ein: "))

        estimates = []
        for i in range(1, num_simulations + 1):
            successes = np.random.binomial(1, success_prob, i)
            estimates.append(np.mean(successes))

        plt.plot(estimates)
        plt.title("Konvergenz der geschätzten Wahrscheinlichkeit")
        plt.xlabel("Anzahl der Simulationen")
        plt.ylabel("Geschätzte Wahrscheinlichkeit")
        plt.show()

    elif choice == 4:
        print("\n=== Pseudozufallszahl erzeugen ===")
        p = float(input("Geben Sie die Erfolgswahrscheinlichkeit p (zwischen 0 und 1) ein: "))
        try:
            result = generate_random_bit(p)
            print(f"Generierte Zufallszahl: {result}")
        except ValueError as e:
            print(e)

    else:
        print("Ungültige Eingabe. Bitte starten Sie das Programm neu und wählen Sie eine gültige Option.")

def generate_random_bit(p):
    """
    Generiert eine Pseudozufallszahl mit den Werten 0 und 1.

    Parameter:
        p (float): Wahrscheinlichkeit für eine 1 (zwischen 0 und 1).

    Rückgabewert:
        int: 0 oder 1, wobei die Wahrscheinlichkeit für 1 gerade p ist.
    """
    if 0 <= p <= 1:
        return np.random.binomial(1, p)
    else:
        raise ValueError("Die Wahrscheinlichkeit p muss zwischen 0 und 1 liegen.")

if __name__ == "__main__":
    monte_carlo_learning_tool()
