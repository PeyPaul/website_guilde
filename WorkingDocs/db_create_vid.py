import sqlite3
import pandas as pd

df = pd.read_csv("./inventaire_jv.csv", sep=';')

conn = sqlite3.connect('../guilde/db.sqlite3')
cur = conn.cursor()


def description(platf='-'):
    return f"Ce jeu vidéo peut se jouer sur {platf}."


cur.execute('''
            CREATE TABLE IF NOT EXISTS stock_game_video(
            vid_id INTEGER PRIMARY KEY,
            vid_name TEXT NOT NULL,
            vid_desc TEXT,
            vid_cat TEXT,
            vid_img TEXT,
            UNIQUE(vid_name))''')

colonne_nom = df['Nom']
colonne_cat = df['Type']
colonne_plat = df['Support']

for i in range(int(df.shape[0])):
    nom = colonne_nom.iloc[i]
    cat = colonne_cat.iloc[i]
    pf = colonne_plat.iloc[i]
    desc = description(pf)
    try:
        cur.execute(
            "INSERT INTO stock_game_video (vid_id, vid_name, vid_desc, vid_cat, vid_img) VALUES (?,?,?,?,'https://static.vecteezy.com/ti/vecteur-libre/p3/14057818-jeu-video-avec-des-enfants-jouant-des-controleurs-de-manette-de-jeu-console-de-combat-sur-un-ordinateur-mobile-android-dans-un-dessin-anime-plat-illustration-de-modele-dessine-a-la-main-vectoriel.jpg') ", (i, nom, desc, cat))
    except sqlite3.Error as e:
        conn.rollback()

conn.commit()
conn.close()
