import pandas as pd

# On implémente une fonction qui supprime les espaces et met les noms en majuscules
# afin de les adapter au format du DataFrame
def normalize(name):
    return name.strip().upper()

# ================================Données Coupe du Monde 2026 ===============================

ratings = {
    "CANADA" : 1793,
    "United States"    : 1733,
    "MEXICO" : 1867,
    "JAPAN"  : 1906,
    "New Zealand": 1563,
    "IRAN"   : 1764,
    "ARGENTINA" : 2113,
    "UZBEKISTAN" : 1718,
    "South Korea"  : 1375,
    "JORDAN" : 1685,
    "AUSTRALIA" : 1774,
    "BRAZIL"  : 1988,
    "ECUADOR" : 1935,
    "URUGUAY" : 1892,
    "PARAGUAY" : 1832,
    "COLOMBIA" : 1977,
    "MOROCCO" : 1824,
    "TUNISIA" : 1633,
    "EGYPT"  : 1699,
    "ALGERIA" : 1743,
    "GHANA" : 1510,
    "CAPE VERDE" : 1576,
    "SOUTH AFRICA" : 1518,
    "QATAR"  : 1423,
    "SAUDI ARABIA" : 1566,
    "ENGLAND" : 2020,
    "Ivory Coast" : 1676,
    "SENEGAL" : 1867,
    "FRANCE" : 2081,
    "CROATIA" : 1908,
    "PORTUGAL" : 1984,
    "NORWAY" : 1917,
    "GERMANY" : 1925,
    "NETHERLANDS" : 1961,
    "AUSTRIA" : 1830,
    "BELGIUM" : 1888,
    "SCOTLAND" : 1770,
    "SPAIN" : 2165,
    "SWITZERLAND" : 1894,
    "Haiti" : 1554,
    "PANAMA" : 1733,
    "Curaçao" : 1433,
    "SWEDEN"  : 1714,
    "TURKEY" : 1906,
    "Czech Republic" : 1733,
    "Bosnia and Herzegovina": 1591,
    "CONGO" : 1207,
    "IRAQ" : 1608,
} 
ratings = {normalize(k): v for k, v in ratings.items()}


groupes = {
    "A": [normalize(name) for name in ["MEXICO", "South Korea", "Czech Republic", "SOUTH AFRICA"]],

    "B": [normalize(name) for name in ["CANADA", "SWITZERLAND", "QATAR", "Bosnia and Herzegovina"]],

    "C": [normalize(name) for name in ["BRAZIL", "MOROCCO", "Haiti", "SCOTLAND"]],

    "D": [normalize(name) for name in ["United States", "PARAGUAY", "TURKEY", "AUSTRALIA"]],

    "E": [normalize(name) for name in ["GERMANY", "Curaçao", "Ivory Coast", "ECUADOR"]],

    "F": [normalize(name) for name in ["NETHERLANDS", "JAPAN", "SWEDEN", "TUNISIA"]],

    "G": [normalize(name) for name in ["BELGIUM", "EGYPT", "IRAN", "New Zealand"]],

    "H": [normalize(name) for name in ["SPAIN", "CAPE VERDE", "SAUDI ARABIA", "URUGUAY"]],

    "I": [normalize(name) for name in ["FRANCE", "SENEGAL", "IRAQ", "NORWAY"]],

    "J": [normalize(name) for name in ["ARGENTINA", "ALGERIA", "AUSTRIA", "JORDAN"]],

    "K": [normalize(name) for name in ["PORTUGAL", "CONGO", "UZBEKISTAN", "COLOMBIA"]],

    "L": [normalize(name) for name in ["ENGLAND", "CROATIA", "GHANA", "PANAMA"]]
}

#================================Données pour la Coupe du Monde Qatar 2022================================================

"""
ratings = {
    "QATAR": 1577,
    "ECUADOR": 1431,
    "SENEGAL": 1745,
    "NETHERLANDS": 2073,

    "ENGLAND": 1966,
    "IRAN": 1780,
    "United States": 1817,
    "WALES": 1716,

    "ARGENTINA": 2144,
    "SAUDI ARABIA": 1644,
    "MEXICO": 1812,
    "POLAND": 1801, 

    "FRANCE": 2081,
    "AUSTRALIA": 1772,
    "DENMARK": 1883,  
    "TUNISIA": 1745,

    "SPAIN": 1997,
    "GERMANY": 1955,
    "JAPAN": 1851,
    "COSTA RICA": 1737,

    "BELGIUM": 1947,
    "CANADA": 1711,
    "MOROCCO": 1866,
    "CROATIA": 1950,

    "BRAZIL": 2133,
    "SERBIA": 1835,
    "SWITZERLAND": 1878,
    "CAMEROON": 1676,

    "PORTUGAL": 1998,
    "GHANA": 1593,
    "URUGUAY": 1904,
    "South Korea": 1788
}
ratings = {normalize(k): v for k, v in ratings.items()}
groupes = {
    "A": [normalize(name) for name in [
        "QATAR", "ECUADOR", "SENEGAL", "NETHERLANDS"
    ]],

    "B": [normalize(name) for name in [
        "ENGLAND", "IRAN", "United States", "WALES"
    ]],

    "C": [normalize(name) for name in [
        "ARGENTINA", "SAUDI ARABIA", "MEXICO", "POLAND"
    ]],

    "D": [normalize(name) for name in [
        "FRANCE", "AUSTRALIA", "DENMARK", "TUNISIA"
    ]],

    "E": [normalize(name) for name in [
        "SPAIN", "GERMANY", "JAPAN", "COSTA RICA"
    ]],

    "F": [normalize(name) for name in [
        "BELGIUM", "CANADA", "MOROCCO", "CROATIA"
    ]],

    "G": [normalize(name) for name in [
        "BRAZIL", "SERBIA", "SWITZERLAND", "CAMEROON"
    ]],

    "H": [normalize(name) for name in [
        "PORTUGAL", "GHANA", "URUGUAY", "South Korea"
    ]]
}

"""

# Données pour entraîner le modèle de Poisson simple :
# log(μA) = α0 + α1 · EloA + α2 · EloB

L = []
df = pd.read_csv("../data/results.csv")
for _, row in df.iterrows():
    #row designe les lignes de notre data frame
    home = normalize(row["home_team"])
    away = normalize(row["away_team"])

    if home not in ratings or away not in ratings:
        continue

    L.append((ratings[home], ratings[away], row["home_score"]))
    L.append((ratings[away], ratings[home], row["away_score"]))


# Préparation des données pour le modèle de Poisson amélioré


teams = set(df["home_team"]).union(set(df["away_team"]))

dic = {normalize(team): [] for team in teams}
for _, row in df.iterrows():
    #row designe les lignes de notre data frame
    home = normalize(row["home_team"])
    away = normalize(row["away_team"])

    if home not in ratings or away not in ratings:
        continue

    dic[home].append((ratings[away], row["home_score"],row["away_score"]))
    dic[away].append((ratings[home], row["away_score"], row["home_score"]))

