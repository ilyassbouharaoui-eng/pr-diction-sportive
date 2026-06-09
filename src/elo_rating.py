import math
import numpy as np

# Calcul de la probabilité selon le modèle d'Elo et mise à jour du rating


# la probabilité pour que A gagne contre B:
def E(RA, RB):
    return 1 / (1 + 10**((RB - RA) / 400))


# Ratings des joueurs A et B
# outcome représente le résultat : 1 si A gagne, 0 si B gagne, 0.5 en cas de match nul.
def elo_rating(RA, RB, K, outcom):
    PA = E(RA, RB)
    PB = E(RB, RA)

    RA = RA + K * (outcom - PA)
    RB = RB + K * ((1 - outcom) - PB)
    return RA, RB


# Calcul de la probabilité que l’équipe A gagne contre B,
# en supposant que le nombre de buts marqués par A et B suit une loi de Poisson de paramètre lambda.

# Étant donné deux équipes A et B, on calcule la probabilité de victoire de A
# ainsi que la probabilité d’un match nul.
def proba_A_gagne(lambda_A, lambda_B):
    # On fixe un nombre maximum de buts possibles pour A à 30
    N = 30
    s = 0
    for k in range(N):
        s1 = 0
        for i in range(k):
            s1 += (lambda_A**i) / math.factorial(i)
        s += ((lambda_B**k) / math.factorial(k)) * (1 - np.exp(-lambda_A) * s1)
    return np.exp(-lambda_B) * s


def prob_draw(lambda_A, lambda_B):
    N = 30
    s = 0
    for k in range(N):
        s += ((lambda_B * lambda_A)**k) / ((math.factorial(k))**2)
    return np.exp(-(lambda_A + lambda_B)) * s