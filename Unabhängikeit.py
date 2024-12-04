def pruefe_unabhaengigkeit():
    # Eingaben
    P_A = float(input("Geben Sie die Wahrscheinlichkeit von A (P(A)) in % ein: ")) / 100
    P_B = float(input("Geben Sie die Wahrscheinlichkeit von B (P(B)) in % ein: ")) / 100
    P_A_und_B = float(input("Geben Sie die Wahrscheinlichkeit von A und B (P(A ∩ B)) in % ein: ")) / 100
    # Berechnung der erwarteten Wahrscheinlichkeit für unabhängige Ereignisse
    erwartete_P_A_und_B = P_A * P_B

    # Überprüfung auf Gleichheit (unter Berücksichtigung von Rundungsfehlern)
    if abs(P_A_und_B - erwartete_P_A_und_B) < 1e-6:  # Toleranzschwelle für Rundungsfehler
        print("Unabhängig.")
        return
    else:
        print("Abhängig.")
        return

