import math

def kombination_variation_permutation_():
    # Frage 1: Werden alle Objekte verwendet?
    alle_objekte = input("Werden alle Objekte verwendet? (j = Ja, n =Nein): ")

    if alle_objekte == "j":
        # Permutation (alle Objekte werden verwendet)
        option = input("Treten Wiederholungen ein? (j = Ja, n =Nein):")

        if option == "j":
            # Permutation mit Wiederholung
            n = int(input("Geben Sie die Gesamtzahl der Elemente (n) ein: "))
            k_anz = int(input("Geben Sie die Anzahl der ausgewählten Elemente (k) ein: "))
            for i in range(k_anz):
                k = []
                k_x = 0
                k_x = int(input(f"Geben Sie k{i + 1} ein: "))
                k.append(k_x)
            ergebnis = math.factorial(n)  # n!
            # Wir teilen durch die Fakultäten der Häufigkeiten der wiederholten Objekte
            for h in k:
                ergebnis /= math.factorial(h)
            print(ergebnis)
        elif option == "n":
            # Permutation ohne Wiederholung
            n = int(input("Geben Sie die Gesamtzahl der Elemente (n) ein: "))
            ergebnis = math.factorial(n)
            print(ergebnis)
        else:
            print("Ungültige Eingabe. Bitte starten Sie das Programm erneut.")

    elif alle_objekte == "n":
        # Frage 2: Reihenfolge spielt eine Rolle?
        reihenfolge = input("Spielt die Reihenfolge eine Rolle? (j = Ja, n =Nein): ")

        if reihenfolge == "n":
            # Kombinationen (Reihenfolge spielt keine Rolle)
            option = input("Treten Wiederholungen ein? (Ja, Nein):")

            n = int(input("Geben Sie die Gesamtzahl der Elemente (n) ein: "))
            k = int(input("Geben Sie die Anzahl der ausgewählten Elemente (k) ein: "))

            if option == "j":
                # Kombination mit Wiederholung: (n + k - 1) über k
                ergebnis = math.comb(n + k - 1, k)
                print(ergebnis)
            elif option == "n":
                # Kombination ohne Wiederholung: n! / (k! * (n - k)!)
                ergebnis = math.comb(n, k)
                print(ergebnis)
            else:
                print("Ungültige Eingabe. Bitte starten Sie das Programm erneut.")

        elif reihenfolge == "j":
            # Variationen (Reihenfolge spielt eine Rolle)
            option = input("Treten Wiederholungen ein?")

            n = int(input("Geben Sie die Gesamtzahl der Elemente (n) ein: "))
            k = int(input("Geben Sie die Anzahl der ausgewählten Elemente (k) ein: "))

            if option == "j":
                # Variation mit Wiederholung: n^k
                ergebnis = n ** k
                print(ergebnis)
            elif option == "n":
                # Variation ohne Wiederholung: n! / (n - k)!
                ergebnis = math.perm(n, k)
                print(ergebnis)
            else:
                print("Ungültige Eingabe. Bitte starten Sie das Programm erneut.")
        else:
            print("Ungültige Eingabe. Bitte starten Sie das Programm erneut.")

    else:
        print("Ungültige Eingabe. Bitte starten Sie das Programm erneut.")

