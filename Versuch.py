import numpy as np
import sympy as sp


def ask_for_input(prompt, value_type=float):
    """
    Hilfsmethode zum Abfragen von Benutzereingaben und Konvertieren in den richtigen Typ.
    """
    while True:
        try:
            return value_type(input(prompt))
        except ValueError:
            print(f"Bitte geben Sie eine gültige {value_type} Zahl ein.")


def calculate_discrete_expected_value():
    print("Berechnung des Erwartungswerts einer diskreten Zufallsvariablen:")

    # Eingabe der möglichen Werte und Wahrscheinlichkeiten
    n = int(input("Wie viele mögliche Werte gibt es? "))

    values = []
    probabilities = []

    for i in range(n):
        value = float(input(f"Geben Sie den Wert x_{i + 1} ein: "))
        prob = float(input(f"Geben Sie die Wahrscheinlichkeit p(x_{i + 1}) ein: "))

        values.append(value)
        probabilities.append(prob)

    # Erwartungswert berechnen
    expected_value = sum(v * p for v, p in zip(values, probabilities))
    print(f"Der Erwartungswert der diskreten Zufallsvariablen ist: {expected_value:.4f}")


def calculate_continuous_expected_value():
    print("Berechnung des Erwartungswerts einer stetigen Zufallsvariablen:")

    # Eingabe der Dichtefunktion
    x = sp.symbols('x')
    func_str = input("Geben Sie die Dichtefunktion f(x) der Zufallsvariablen ein (z.B. x**2): ")

    # Umwandlung der Funktion in eine sympy-Funktion
    f_x = sp.sympify(func_str)

    # Eingabe des Integrationsbereichs
    a = ask_for_input("Geben Sie die untere Grenze des Integrationsbereichs ein: ", float)
    b = ask_for_input("Geben Sie die obere Grenze des Integrationsbereichs ein: ", float)

    # Erwartungswert berechnen
    expected_value = sp.integrate(x * f_x, (x, a, b))
    print(f"Der Erwartungswert der stetigen Zufallsvariablen ist: {expected_value:.4f}")


def main():
    print("Willkommen zum Erwartungswert-Berechner!")

    choice = input(
        "Wählen Sie den Typ der Zufallsvariablen:\n1: Diskrete Zufallsvariable\n2: Stetige Zufallsvariable\nEingabe (1/2): ")

    if choice == "1":
        calculate_discrete_expected_value()
    elif choice == "2":
        calculate_continuous_expected_value()
    else:
        print("Ungültige Eingabe! Bitte starten Sie das Programm erneut und wählen Sie eine gültige Option.")


if __name__ == "__main__":
    main()
