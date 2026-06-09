from calcul_proba import *
from donne_utiles import *
import random as rd
import numpy as np
import pandas as pd
import statsmodels.api as sm

# Ici, on a écrit une fonction qui retourne le classement des nations dans un groupe donné selon le Ratings des joueurs et la probabilité E
def prediction_groupe_simplifie(nom_groupe):
    liste_points= {equipe : 0 for equipe in groupes[nom_groupe]}
    l = groupes[nom_groupe]
    for i in range(4):
        for j in range(i+1,4):
                RA = ratings[l[i]]
                RB = ratings[l[j]]
                p_win = E(RA,RB)
                p_draw = 0.3*np.exp(-np.abs(RA - RB) / 400)
                p_win = p_win * (1 - p_draw)
                u = rd.random()
                if p_win > u:
                    outcome = 1
                    liste_points[l[i]] +=3
                elif  u < p_win + p_draw :
                    outcome = 0.5
                    liste_points[l[i]] +=1
                    liste_points[l[j]] +=1      
                else:
                    outcome = 0
                    liste_points[l[j]] +=3
                RA,RB = elo_rating(RA,RB,30,outcome)
                ratings[l[i]] = RA
                ratings[l[j]] = RB
    classement = sorted(liste_points.keys(), key=lambda equipe: (liste_points[equipe], ratings[equipe]),reverse=True)          
    return classement            


# On va passer à une prédiction un peu plus sérieuse en utilisant un modèle de Poisson.

# On va essayer maintenant de déterminer les paramètres de la régression de Poisson :
# log(μA) = α0 + α1 · EloA + α2 · EloB
# L’entraînement du modèle de Poisson simplifié
dataf = pd.DataFrame(L,columns=["elo_team","elo_opp","goals"])

X = dataf[["elo_team","elo_opp"]]
X = sm.add_constant(X)
y = dataf["goals"]
model = sm.GLM(y,X,family=sm.families.Poisson())
result = model.fit()
alpha0 = result.params["const"]
alpha1 = result.params["elo_team"]
alpha2 = result.params["elo_opp"]


def prediction_groupe_poisson(nom_groupe):
    liste_point = {equipe : 0 for equipe in groupes[nom_groupe]}
    l = groupes[nom_groupe]
    for i in range(4):
        for j in range(i+1,4):
            A = l[i]
            B = l[j]
            lambda_A = np.exp(alpha0 + alpha1*ratings[A] + alpha2*ratings[B])
            lambda_B = np.exp(alpha0 + alpha1*ratings[B] + alpha2*ratings[A])
            p_win = proba_A_gagne(lambda_A,lambda_B)
            p_draw = prob_draw(lambda_A,lambda_B)
            u = rd.random()
            if p_win > u:
                liste_point[l[i]] +=3
            elif  u < p_win + p_draw :
                liste_point[l[i]] +=1
                liste_point[l[j]] +=1      
            else:
                liste_point[l[j]] +=3
    classement = sorted(liste_point.keys(), key=lambda equipe: (liste_point[equipe], ratings[equipe]),reverse=True)          
    return classement            





#l'entrainement du modele de poisson amélioré
attaque = {}
defence = {}

for equipe in dic.keys() : 
    if equipe not in ratings.keys():
        continue
    df1 = pd.DataFrame(dic[equipe],columns=["elo_opp","goals_team","goals_opp"])
    y1 = df1["goals_team"]
    x1 = df1["elo_opp"]
    x1 = sm.add_constant(x1)
    model1 = sm.GLM(y1,x1,family=sm.families.Poisson())
    result1 = model1.fit()
    a0 = result1.params["const"]
    a1 = result1.params["elo_opp"]
    attaque[equipe] = (a0,a1)
    y2 = df1["goals_opp"]
    x2 = df1["elo_opp"]
    x2 = sm.add_constant(x2)
    model2 = sm.GLM(y2,x2,family=sm.families.Poisson())
    result2 = model2.fit()
    b0 = result2.params["const"]
    b1 = result2.params["elo_opp"]
    defence[equipe] = (b0,b1)


def prediction_groupe_poisson_ameliore(nom_groupe):
    liste_point = {equipe : 0 for equipe in groupes[nom_groupe]}
    l = groupes[nom_groupe]
    for i in range(4):
        for j in range(i+1,4):
            A = l[i]
            B = l[j]
            lambda_A = (np.exp(attaque[A][0] + attaque[A][1]*ratings[B]) + np.exp(defence[B][0] + defence[B][1]*ratings[A])) / 2
            lambda_B = (np.exp(attaque[B][0] + attaque[B][1]*ratings[A]) + np.exp(defence[A][0] + defence[A][1]*ratings[B])) / 2
            p_win = proba_A_gagne(lambda_A,lambda_B)
            p_draw = prob_draw(lambda_A,lambda_B)
            u = rd.random()
            if p_win > u:
                liste_point[l[i]] +=3
            elif  u < p_win + p_draw :
                liste_point[l[i]] +=1
                liste_point[l[j]] +=1      
            else:
                liste_point[l[j]] +=3
    classement = sorted(liste_point.keys(), key=lambda equipe: (liste_point[equipe], ratings[equipe]),reverse=True)          
    return classement            

    



for i in groupes.keys():
    print(i," : ",prediction_groupe_poisson_ameliore(i))

