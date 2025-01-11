def calculate_conditional_probability():
    """
    Berechnet die bedingte Wahrscheinlichkeit basierend auf den Eingaben des Nutzers.
    """
    print("=== Berechnung der bedingten Wahrscheinlichkeit ===")
    p_b_given_a = float(input("Geben Sie P(B|A) in Kommazahlen (zwischen 0 und 1) ein: "))
    p_a = float(input("Geben Sie P(A) in Kommazahlen (zwischen 0 und 1) ein: "))
    p_b = float(input("Geben Sie P(B) in Kommazahlen (zwischen 0 und 1) ein: "))

    p_a_given_b = (p_b_given_a * p_a) / p_b
    return p_a_given_b
