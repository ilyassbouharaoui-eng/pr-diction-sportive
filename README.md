#  Prédiction des résultats de la Coupe du Monde 2026

Ce projet a pour objectif de prédire les résultats de la phase de groupes de la Coupe du Monde 2026 en utilisant le classement Elo et des modèles probabilistes basés sur la loi de Poisson.

Différentes approches ont été développées et comparées afin d’évaluer leur performance dans la prédiction des résultats de matchs et des équipes qualifiées.

---

##  Résultats

Les modèles testés incluent :
- un modèle basé sur le classement Elo
- un modèle de Poisson simple
- un modèle de Poisson amélioré (attaque/défense)

Le modèle de Poisson amélioré obtient les meilleures performances globales.

---

##  Rapport complet

Le rapport détaillé du projet est disponible dans le dépôt et contient :
- la description complète des modèles
- la méthodologie utilisée
- les résultats expérimentaux
- l’analyse des performances

---

##  Données

Les données utilisées proviennent de :
- https://github.com/martj42/international_results
- https://eloratings.net/

---
##  Structure du projet

.
├── data/
│   └── results.csv
├── source/
│   ├── prediction.py
│   ├── donnees_utiles.py
│   ├── calcul_proba.py
│   └── evaluation.py
└── README.md
