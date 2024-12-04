
def bayes_theorem(n):
    P_A = float(input(
        "Die Wahrscheinlichkeit in %, dass das Ereignis A (P(A)) wahr ist (z. B. gezinkter Würfel)")) / 100  # Wahrscheinlichkeit, dass das Ereignis A wahr ist (z. B. gezinkter Würfel)
    P_neg_A = float(input(
        " Die Wahrscheinlichkeit in %, dass das Ereignis A (P(NA))nicht wahr ist (z. B. fairer Würfel)")) / 100  # Wahrscheinlichkeit, dass das Ereignis A nicht wahr ist (z. B. fairer Würfel)
    P_B_given_A = float(input(
        "Die Wahrscheinlichkeit in %, dass B eintritt, wenn A wahr ist (P(B|A))(z. B. Wahrscheinlichkeit für eine 5 bei gezinktem Würfel)")) / 100  # Wahrscheinlichkeit, dass B eintritt, wenn A wahr ist (z. B. Wahrscheinlichkeit für eine 5 bei gezinktem Würfel)
    P_B_given_neg_A = float(input(
        "Die Wahrscheinlichkeitin %, dass B eintritt, wenn A nicht wahr ist (P(B|NA)(z. B. Wahrscheinlichkeit für eine 5 bei einem fairen Würfel)")) / 100  # Wahrscheinlichkeit, dass B eintritt, wenn A nicht wahr ist (z. B. Wahrscheinlichkeit für eine 5 bei einem fairen Würfel)

    # Berechnung der Wahrscheinlichkeit für n Wiederholungen von B bei A
    P_B_given_A_n = P_B_given_A ** n

    # Berechnung der Wahrscheinlichkeit für n Wiederholungen von B bei ¬A
    P_B_given_neg_A_n = P_B_given_neg_A ** n

    # Gesamtwahrscheinlichkeit für n Wiederholungen von B
    P_B = P_B_given_A_n * P_A + P_B_given_neg_A_n * P_neg_A

    # Bayes' Theorem anwenden
    P_A_given_B = (P_B_given_A_n * P_A) / P_B
    print(f"{P_A_given_B * 100}%")


