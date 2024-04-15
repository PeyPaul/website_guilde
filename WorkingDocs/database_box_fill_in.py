# -*- coding: utf-8 -*-

import sqlite3
import pandas as pd
print('Imports : OK')

# Création des dataframes à partir des csv

dfs = pd.read_csv("./inventaire_jds.csv", sep=';')
dfv = pd.read_csv("./inventaire_jv.csv", sep=';')
dfr = pd.read_csv("./inventaire_jdr.csv", sep=';')
print("Créations DFs : OK")

# Implémentation de fonction


def etat(state='Neuf'):
    return state.upper()


def dispo(avaible='Disponible'):
    return avaible.upper()


print('Implémentation de fonction : OK')

# Création des colonnes

nom_soc = dfs['Nom']
dup_soc = dfs['Duplicata']
nom_vid = dfv['Nom']
dup_vid = dfv['Nombre']
nom_rol = dfr['Nom']
dup_rol = dfr['Nombre']
state_rol = dfr['Etat']
print("Colonnes : OK")

# Connexion à la DB
conn = sqlite3.connect('../guilde/db.sqlite3')
cur = conn.cursor()
print("Ouverture connexion : OK")

# Remplissage de la table stock_gameinstance

for i in range(int(dfs.shape[0])):
    nom = nom_soc.iloc[i]
    nbr = int(dup_soc.iloc[i])
    res = cur.execute("SELECT id FROM stock_game WHERE name=?", (nom,))
    jeu = res.fetchone()[0]
    n = cur.execute(
        "SELECT COUNT(*) FROM stock_gameinstance WHERE game_id=?", (jeu,)).fetchone()[0]
    while n < nbr:
        res2 = cur.execute(
            "INSERT INTO stock_gameinstance (state, disponibility,game_id) VALUES (?,?,?)", (etat(), dispo(), jeu))
        n += 1

for i in range(int(dfv.shape[0])):
    nom = nom_vid.iloc[i]
    nbr = int(dup_vid.iloc[i])
    res = cur.execute("SELECT id FROM stock_game WHERE name=?", (nom,))
    jeu = res.fetchone()[0]
    n = cur.execute(
        "SELECT COUNT(*) FROM stock_gameinstance WHERE game_id=?", (jeu,)).fetchone()[0]
    while n < nbr:
        res2 = cur.execute(
            "INSERT INTO stock_gameinstance (state, disponibility,game_id) VALUES (?,?,?)", (etat(), dispo(), jeu))
        n += 1

for i in range(int(dfr.shape[0])):
    nom = nom_rol.iloc[i]
    nbr = int(dup_rol.iloc[i])
    res = cur.execute("SELECT id FROM stock_game WHERE name=?", (nom,))
    jeu = res.fetchone()[0]
    n = cur.execute(
        "SELECT COUNT(*) FROM stock_gameinstance WHERE game_id=?", (jeu,)).fetchone()[0]
    while n < nbr:
        res2 = cur.execute(
            "INSERT INTO stock_gameinstance (state, disponibility,game_id) VALUES (?,?,?)", (etat(state_rol.iloc[i]), dispo(), jeu))
        n += 1

print("DB : OK")

conn.commit()
conn.close()
