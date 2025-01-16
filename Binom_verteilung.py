import math


def Binominialverteilung():
    try:
        n = int(input("n (Anzahl der Versuche): "))
        p = float(input("Wahrscheinlichkeit für Erfolg in %: ")) / 100
        operation = input("Welche Wahrscheinlichkeit möchtest du berechnen?\n"
                          "Gib ein (>, <, >=, <=, =): ").strip()

        k = int(input("Für welchen Wert von k möchtest du die Wahrscheinlichkeit berechnen? "))

        # Eingabekontrollen
        if n <= 0 or p < 0 or p > 1 or operation not in ['>', '<', '>=', '<=', '=']:
            print("Ungültige Eingabe! Stelle sicher, dass n > 0, 0 <= p <= 1 und die Operation gültig ist.")
            return

        wahrscheinlichkeit = 0

        # Berechnung je nach Auswahl der Operation
        if operation == '>':
            for i in range(k + 1, n + 1):
                wahrscheinlichkeit += math.comb(n, i) * (p ** i) * ((1 - p) ** (n - i))
        elif operation == '<':
            for i in range(k):
                wahrscheinlichkeit += math.comb(n, i) * (p ** i) * ((1 - p) ** (n - i))
        elif operation == '>=':
            for i in range(k, n + 1):
                wahrscheinlichkeit += math.comb(n, i) * (p ** i) * ((1 - p) ** (n - i))
        elif operation == '<=':
            for i in range(k + 1):
                wahrscheinlichkeit += math.comb(n, i) * (p ** i) * ((1 - p) ** (n - i))
        elif operation == '=':
            wahrscheinlichkeit = math.comb(n, k) * (p ** k) * ((1 - p) ** (n - k))

        print(f"Wahrscheinlichkeit P(X {operation} {k}): {wahrscheinlichkeit * 100:.5f}%")

        # Berechnung des Erwartungswerts und der Varianz
        erwartungswert = n * p
        print(f"Erwartungswert E(X): {erwartungswert:.2f}")

        varianz = n * p * (1 - p)
        print(f"Varianz: {varianz:.2f}")

    except ValueError:
        print("Bitte gib gültige Zahlen ein.")