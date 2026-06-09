from donne_utiles import normalize
from prediction import *
# Pour utiliser ce code, il est nécessaire de commenter les données de la Coupe du Monde 2026.
# Il faut également supprimer celles relatives à la Coupe du Monde 2022 au Qatar.
resultats_reel = {
    "A": [normalize(name) for name in ["NETHERLANDS", "SENEGAL", "ECUADOR", "QATAR"]],
    "B": [normalize(name) for name in ["ENGLAND", "United States", "IRAN", "WALES"]],
    "C": [normalize(name) for name in ["ARGENTINA", "POLAND", "MEXICO", "SAUDI ARABIA"]],
    "D": [normalize(name) for name in ["FRANCE", "AUSTRALIA", "TUNISIA", "DENMARK"]],
    "E": [normalize(name) for name in ["JAPAN", "SPAIN", "GERMANY", "COSTA RICA"]],
    "F": [normalize(name) for name in ["MOROCCO", "CROATIA", "BELGIUM", "CANADA"]],
    "G": [normalize(name) for name in ["BRAZIL", "SWITZERLAND", "CAMEROON", "SERBIA"]],
    "H": [normalize(name) for name in ["PORTUGAL", "South Korea", "URUGUAY", "GHANA"]]
}
resultats_elo_simple = {}
resultats_poisson = {}
resultats_poisson_ameliore = {}

for i in groupes.keys() :
   resultats_elo_simple[i] = prediction_groupe_simplifie(i)
   resultats_poisson[i] = prediction_groupe_poisson(i)
   resultats_poisson_ameliore[i] = prediction_groupe_poisson_ameliore(i)


score1 = 0
score2 = 0
score3 = 0

for g in resultats_reel.keys():
    for i in range(4):
        if resultats_elo_simple[g][i] == resultats_reel[g][i]:
            score1 += 1
        if resultats_poisson[g][i] == resultats_reel[g][i]: 
            score2 +=1
        if resultats_poisson_ameliore[g][i] == resultats_reel[g][i]:   
            score3 +=1    

accuracy1 = score1 / 32
accuracy2 = score2 / 32
accuracy3 = score3 / 32

print(accuracy1)
print(accuracy2)
print(accuracy3)


erreur1 = 0
erreur2 = 0
erreur3 = 0

for g in resultats_reel.keys():
    for equipe in resultats_reel[g]:

        rang_reel = resultats_reel[g].index(equipe)

        rang_pred1 = resultats_elo_simple[g].index(equipe)
        erreur1 += abs(rang_reel - rang_pred1)

        rang_pred2 = resultats_poisson[g].index(equipe)
        erreur2 += abs(rang_reel - rang_pred2)

        rang_pred3 = resultats_poisson_ameliore[g].index(equipe)
        erreur3 += abs(rang_reel - rang_pred3)

erreur_moyenne1 = erreur1 / 32
erreur_moyenne2 = erreur2 / 32
erreur_moyenne3 = erreur3 / 32

print(erreur_moyenne1)
print(erreur_moyenne2)
print(erreur_moyenne3)


qualif1 = 0
qualif2 = 0
qualif3 = 0

for g in resultats_reel.keys():

    reels = set(resultats_reel[g][:2])

    pred1 = set(resultats_elo_simple[g][:2])
    pred2 = set(resultats_poisson[g][:2])
    pred3 = set(resultats_poisson_ameliore[g][:2])

    qualif1 += len(reels & pred1)
    qualif2 += len(reels & pred2)
    qualif3 += len(reels & pred3)

taux1 = qualif1 / 16
taux2 = qualif2 / 16
taux3 = qualif3 / 16

print(taux1)
print(taux2)
print(taux3)
