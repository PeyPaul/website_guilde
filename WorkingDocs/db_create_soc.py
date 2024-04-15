import sqlite3
import pandas as pd

df = pd.read_csv("./inventaire_jds.csv", sep=';')

conn = sqlite3.connect('../guilde/db.sqlite3')
cur = conn.cursor()


def description(nbr_joueur='-', type='-', duree='-'):
    if len(str(nbr_joueur)) >= 3:
        return f"Ce jeu est un jeu de {str(type).lower()}. Il peut se jouer de {nbr_joueur}, et dure {duree}."
    else:
        return f"Ce jeu est un jeu de {str(type).lower()}. Il peut se jouer à {nbr_joueur}, et dure {duree}."


cur.execute('''
            CREATE TABLE IF NOT EXISTS stock_game_societe(
            soc_id INTEGER PRIMARY KEY,
            soc_name TEXT NOT NULL,
            soc_desc TEXT,
            soc_cat TEXT,
            soc_img TEXT,
            UNIQUE(soc_name))''')

colonne_nom = df['Nom']
colonne_nbj = df['Nb de joueurs']
colonne_temps = df['Temps']
colonne_cat = df['Categorie']

for i in range(int(df.shape[0])):
    nom = colonne_nom.iloc[i]
    nbj = colonne_nbj.iloc[i]
    temps = colonne_temps.iloc[i]
    cat = colonne_cat.iloc[i]
    desc = description(nbj, cat, temps)
    try:
        cur.execute(
            "INSERT INTO stock_game_societe (soc_id, soc_name, soc_desc, soc_cat,soc_img) VALUES (?,?,?,?,'https://petitsfrenchies.com/wp-content/uploads/2016/08/cartes-jouer-70797.jpg') ", (i, nom, desc, cat))
    except sqlite3.Error as e:
        conn.rollback()

conn.commit()
conn.close()
