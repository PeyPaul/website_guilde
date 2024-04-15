import sqlite3
import pandas as pd

df = pd.read_csv("./inventaire_jdr.csv", sep=';')

conn = sqlite3.connect('../guilde/db.sqlite3')
cur = conn.cursor()


def description(cat='-'):
    return f"Ce jeu est de catégorie {str(cat).lower()}."


cur.execute('''
            CREATE TABLE IF NOT EXISTS stock_game_role(
            rol_id INTEGER PRIMARY KEY,
            rol_name TEXT NOT NULL,
            rol_desc TEXT,
            rol_cat TEXT,
            rol_img TEXT,
            UNIQUE(rol_name))''')

colonne_nom = df['Nom']
colonne_cat = df['Categorie']


for i in range(int(df.shape[0])):
    nom = colonne_nom.iloc[i]
    cat = colonne_cat.iloc[i]
    desc = description(cat)
    try:
        cur.execute(
            "INSERT INTO stock_game_role (rol_id, rol_name, rol_desc, rol_cat, rol_img) VALUES (?,?,?,?,'https://www.blog.leroliste.com/wp-content/uploads/article-histoire-des-1600x1067.jpg') ", (i, nom, desc, cat))
    except sqlite3.Error as e:
        conn.rollback()

conn.commit()
conn.close()
