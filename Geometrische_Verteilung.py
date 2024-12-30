from scipy.stats import geom

def geometrische_verteilung_berechnung():
    # Erfolgswahrscheinlichkeit p eingeben
    p = float(input("Geben Sie die Erfolgswahrscheinlichkeit p ein (0 < p <= 1): "))
    if p <= 0 or p > 1:
        print("Die Erfolgswahrscheinlichkeit muss zwischen 0 und 1 liegen.")
        return

    wahl = int(input("Wählen Sie eine Option (1, 2, 3 oder 4): \n"
                     "1: Dichtefunktion P(X = k) (Wahrscheinlichkeit für genau k Versuche bis zum ersten Erfolg)\n"
                     "2: Verteilungsfunktion P(X <= k) (Wahrscheinlichkeit für k oder weniger Versuche bis zum ersten Erfolg)\n"
                     "3: Wahrscheinlichkeit P(X > k) (Wahrscheinlichkeit, dass mehr als k Versuche nötig sind)\n"
                     "4: Erwartungswert und Varianz (Kennzahlen der Verteilung)"))
    if wahl not in [1, 2, 3, 4]:
        print("Bitte geben Sie 1, 2, 3 oder 4 ein.")
        return

    if wahl == 1:
        # Dichtefunktion P(X = k)
        k = int(input("Geben Sie den Wert k ein (k >= 1): "))
        if k < 1:
            print("k muss eine ganze Zahl >= 1 sein.")
            return
        p_k = geom.pmf(k, p)
        print(f"Die Dichtefunktion P(X = {k}) beträgt: {p_k:.4f}")
    elif wahl == 2:
        # Verteilungsfunktion P(X <= k)
        k = int(input("Geben Sie den Wert k ein (k >= 1): "))
        if k < 1:
            print("k muss eine ganze Zahl >= 1 sein.")
            return
        p_le_k = geom.cdf(k, p)
        print(f"Die Verteilungsfunktion P(X <= {k}) beträgt: {p_le_k:.4f}")
    elif wahl == 3:
        # Wahrscheinlichkeit P(X > k)
        k = int(input("Geben Sie den Wert k ein (k >= 1): "))
        if k < 1:
            print("k muss eine ganze Zahl >= 1 sein.")
            return
        p_gt_k = 1 - geom.cdf(k, p)
        print(f"Die Wahrscheinlichkeit P(X > {k}) beträgt: {p_gt_k:.4f}")
    elif wahl == 4:
        # Erwartungswert und Varianz
        erwartungswert = 1 / p
        varianz = (1 - p) / (p ** 2)
        print(f"Der Erwartungswert (durchschnittliche Anzahl Versuche bis zum ersten Erfolg) beträgt: {erwartungswert:.4f}")
        print(f"Die Varianz (Maß für die Streuung der Anzahl Versuche) beträgt: {varianz:.4f}")
