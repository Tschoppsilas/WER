import math
def Kumulativ():
    n = int(input("n (anzahl versuche / total vorhanden)"))
    p = float(input("Wahrscheinlichkeit in % für erfolg")) / 100
    Wert = int(input("Was ist der Wert in der Formel (P(X>=Wert)"))
    p_x_le_Wert_minus1 = sum(math.comb(n, k) * (p ** k) * ((1 - p) ** (n - k)) for k in range(Wert))
    # Wahrscheinlichkeit für X >= 7
    p_x_ge_Wert = 1 - p_x_le_Wert_minus1

    print(f"Wahrscheinlichkeit ist:{p_x_ge_Wert * 100:.2f}%")