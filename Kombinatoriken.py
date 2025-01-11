import math

def kombination_variation_permutation():
    # Frage 1: Werden alle Objekte verwendet?
    alle_objekte = input("Werden alle Objekte verwendet? (j = Ja, n = Nein): ").lower()

    if alle_objekte == "j":
        # Permutation (alle Objekte werden verwendet)
        option = input("Treten Wiederholungen auf? (j = Ja, n = Nein): ").lower()

        if option == "j":
            # Permutation mit Wiederholung
            n = int(input("Geben Sie die Gesamtzahl der Elemente (n) ein: "))
            k = list(map(int, input("Geben Sie die Häufigkeiten der Wiederholungen (durch Leerzeichen getrennt) ein: ").split()))
            if sum(k) != n:
                print("Fehler: Die Summe der Häufigkeiten muss n entsprechen!")
                return
            ergebnis = math.factorial(n)
            for h in k:
                ergebnis //= math.factorial(h)
            print(f"Ergebnis (Permutation mit Wiederholung): {ergebnis}")
        elif option == "n":
            # Permutation ohne Wiederholung
            n = int(input("Geben Sie die Gesamtzahl der Elemente (n) ein: "))
            ergebnis = math.factorial(n)
            print(f"Ergebnis (Permutation ohne Wiederholung): {ergebnis}")
        else:
            print("Ungültige Eingabe. Bitte starten Sie das Programm erneut.")

    elif alle_objekte == "n":
        # Frage 2: Spielt die Reihenfolge eine Rolle?
        reihenfolge = input("Spielt die Reihenfolge eine Rolle? (j = Ja, n = Nein): ").lower()

        if reihenfolge == "n":
            # Kombinationen (Reihenfolge spielt keine Rolle)
            option = input("Treten Wiederholungen auf? (j = Ja, n = Nein): ").lower()
            n = int(input("Geben Sie die Gesamtzahl der Elemente (n) ein: "))
            k = int(input("Geben Sie die Anzahl der ausgewählten Elemente (k) ein: "))

            if option == "j":
                # Kombination mit Wiederholung: (n + k - 1) über k
                ergebnis = math.comb(n + k - 1, k)
                print(f"Ergebnis (Kombination mit Wiederholung): {ergebnis}")
            elif option == "n":
                # Kombination ohne Wiederholung
                if k > n:
                    print("Fehler: k darf nicht größer als n sein!")
                    return
                ergebnis = math.comb(n, k)
                print(f"Ergebnis (Kombination ohne Wiederholung): {ergebnis}")
            else:
                print("Ungültige Eingabe. Bitte starten Sie das Programm erneut.")

        elif reihenfolge == "j":
            # Variationen (Reihenfolge spielt eine Rolle)
            option = input("Treten Wiederholungen auf? (j = Ja, n = Nein): ").lower()
            n = int(input("Geben Sie die Gesamtzahl der Elemente (n) ein: "))
            k = int(input("Geben Sie die Anzahl der ausgewählten Elemente (k) ein: "))

            if option == "j":
                # Variation mit Wiederholung: n^k
                ergebnis = n ** k
                print(f"Ergebnis (Variation mit Wiederholung): {ergebnis}")
            elif option == "n":
                # Variation ohne Wiederholung: n! / (n - k)!
                if k > n:
                    print("Fehler: k darf nicht größer als n sein!")
                    return
                ergebnis = math.perm(n, k)
                print(f"Ergebnis (Variation ohne Wiederholung): {ergebnis}")
            else:
                print("Ungültige Eingabe. Bitte starten Sie das Programm erneut.")
        else:
            print("Ungültige Eingabe. Bitte starten Sie das Programm erneut.")
    else:
        print("Ungültige Eingabe. Bitte starten Sie das Programm erneut.")

# Test

