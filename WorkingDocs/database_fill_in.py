# -*- coding: utf-8 -*-


import sqlite3
import pandas as pd


# Utilisez read_excel en spécifiant l'encodage
df = pd.read_csv("./inventaire_jds.csv", sep=';')
dfv = pd.read_csv("./inventaire_jv.csv", sep=';')
dfr = pd.read_csv("./inventaire_jdr.csv", sep=';')
print("Créations DFs : OK")
# Affichez les premières lignes du DataFrame pour vérifier si les données ont été correctement chargées

conn = sqlite3.connect('../guilde/db.sqlite3')
cur = conn.cursor()
print("Ouverture connexion : OK")


def verifier_doublon(nom):
    cur.execute("SELECT * FROM stock_game WHERE name=?", (nom,))
    row = cur.fetchone()
    return row is None


def description(nbr_joueur='-', type='-', duree='-'):
    if len(str(nbr_joueur)) >= 3:
        return f"Ce jeu est un jeu de {str(type).lower()}. Il peut se jouer de {nbr_joueur}, et dure {duree}."
    else:
        return f"Ce jeu est un jeu de {str(type).lower()}. Il peut se jouer à {nbr_joueur}, et dure {duree}."


def desc_video(platf='-'):
    return f"Ce jeu vidéo peut se jouer sur {platf}."


def desc_role(cat='-'):
    return f"Ce jeu est de catégorie {str(cat).lower()}."


print("Définitions fonctions : OK")


nan = df['Taille de la boite'][51]

colonne_nom = df['Nom']
colonne_nbj = df['Nb de joueurs']
colonne_temps = df['Temps']
colonne_cat = df['Categorie']
colonne_i = df['Image']
colonne_nomv = dfv['Nom']
colonne_platf = dfv['Support']
colonne_iv = dfv['Image']
colonne_nomr = dfr['Nom']
colonne_catr = dfr['Categorie']
colonne_ir = dfr['Image']

print("Colonnes : OK")

igame = 1

for i in range(int(df.shape[0])):
    nom = colonne_nom.iloc[i]
    nbj = colonne_nbj.iloc[i]
    temps = colonne_temps.iloc[i]
    cat = colonne_cat.iloc[i]
    desc = description(nbj, cat, temps)
    img = colonne_i.iloc[i]
    if verifier_doublon(nom):
        res = cur.execute(
            "INSERT INTO stock_game (id,name,description,category,image) VALUES (?,?,?,?,?) ", (igame, nom, desc, "Jeu de société", img))
    igame += 1

print("JdS : OK")

for i in range(int(dfv.shape[0])):
    nom = colonne_nomv.iloc[i]
    pf = colonne_platf.iloc[i]
    desc = desc_video(pf)
    img = colonne_iv.iloc[i]
    if verifier_doublon(nom):
        res = cur.execute(
            "INSERT INTO stock_game (id,name,description,category,image) VALUES (?,?,?,?,?)", (igame, nom, desc, "Jeu vidéo", img))
    igame += 1

print("JV : OK")

for i in range(int(dfr.shape[0])):
    nom = colonne_nomr.iloc[i]
    cat = colonne_catr.iloc[i]
    desc = desc_role(cat)
    img = colonne_ir.iloc[i]
    if verifier_doublon(nom):
        res = cur.execute(
            "INSERT INTO stock_game (id,name,description,category,image) VALUES (?,?,?,?,?)", (igame, nom, desc, "Jeu de rôle", img))
    igame += 1

print("JdR : OK")


"""
def description(nbr_joueur  , type, duree):
	if len(str(nbr_joueur)) >= 3:
		return f"Ce jeu est un jeu de {type}. Il peut se jouer de {nbr_joueur}, et dure {duree}."
	else:
		return f"Ce jeu est un jeu de {type}. Il peut se jouer à {nbr_joueur}, et dure {duree}."


nan = df['Taille de la boite'][51]


colonne_nom = df['Nom']
colonne_nbj = df['Nb de joueurs']
colonne_temps = df['Temps']
colonne_cat = df['Categorie']

for i in range(int(df.shape[0])):
    nom = colonne_nom.iloc[i]
    nbj = colonne_nbj.iloc[i]
    temps = colonne_temps.iloc[i]
    cat = colonne_cat.iloc[i]
    desc = description(nbj,cat,temps)
    if nom == nan:
        nom = '-'
    if nbj == nan:
        nbj = '-'
    if temps == nan:
        temps = '-'
    if cat == nan:
        cat = '-'
    res = cur.execute("INSERT INTO stock_game (name,description,category,image) VALUES (?,?,?,'https://petitsfrenchies.com/wp-content/uploads/2016/08/cartes-jouer-70797.jpg') ",(nom,desc,cat))
                   
liste_js = [
    "https://joueclub-joueclub-fr-storage.omn.proximis.com/Imagestorage/imagesSynchro/0/0/16ee33eec916630d683acd157633132a2f848ea4_41067038.jpeg",
    "https://static.fnac-static.com/multimedia/Images/85/85/22/F4/15999621-3-1541-1/tsp20230127193013/Deadlines.jpg",
    "https://i0.wp.com/gusandco.net/wp-content/uploads/2016/08/complots-matos2.jpg?fit=1135%2C738&ssl=1",
    "https://cdn.laredoute.com/products/4/5/b/45b380cba7dd6fd1c79d52680d404cda.jpg?width=1200&dpr=1",
    "https://www.laposte.fr/ecom/occ/ecommerce/medias/sys_master/productsmedias/hb4/he9/9948599353374/mp-500168827_media2/mp-500168827_media2.jpg_450Wx450H",
    "https://auparadisdujeu.ch/shop/801-medium_default/time-bomb.jpg",
    "https://www.goldenmeeple.be/wp-content/uploads/2019/01/citadelles-3-edition-00.jpg",
    "https://www.espritjeu.com/upload/image/katana-p-image-50279-grande.jpg",
    "https://cdn1.philibertnet.com/377954-large_default/le-poker-des-cafards.jpg",
    "https://cdn1.trictrac.net/documents/formats/enlargement/documents/originals/8c/11/d98cf0147ab41383a608611667da98ce3dfa.png",
    "https://joueclub-joueclub-fr-storage.omn.proximis.com/Imagestorage/imagesSynchro/0/0/884eac661b6c4d03b98c6b0a5ddcfde2ca4ec805_06024161.jpeg",
    "https://cdn2.trictrac.net/documents/formats/enlargement/documents/originals/f7/a3/00d7cdd99fa30bc7c48a31c5668ae03ad3b2.jpeg",
    "https://ulule.me/presales/4/7/6/11674/khromix_vue_globale_jpg_640x860_q85.jpg",
    "https://cdn1.philibertnet.com/502880-thickbox_default/twin-it.jpg",
    "https://image.darty.com/darty?type=image&source=/market/2023/09/01/19468743_3723_1.jpg&width=497&height=330&quality=95&effects=Pad(CC,FFFFFF)",
    "https://cdn2.philibertnet.com/472779-thickbox_default/linkto-cuisine.jpg",
    "https://ludovox-fr.exactdn.com/wp-content/uploads/2014/06/jeu-de-societe-novembre-rouge.png?strip=all&lossy=1&ssl=1",
    "https://i0.wp.com/gusandco.net/wp-content/uploads/2016/09/notalone.jpg?fit=747%2C1024",
    "https://m.media-amazon.com/images/I/619wWrB4cXL.jpg",
    "https://ludovox-fr.exactdn.com/wp-content/uploads/2017/03/crossfire-boite-plaid-hat-games-ludovox.jpg?strip=all&lossy=1&ssl=1",
    "https://m.media-amazon.com/images/I/819gGZtv8iL._AC_UF1000,1000_QL80_.jpg",
    "https://joueclub-joueclub-fr-storage.omn.proximis.com/Imagestorage/imagesSynchro/0/0/80cf1a64794e48bf3e4d67e65fea5cca04fc5221_06040809.jpeg",
    "https://m.media-amazon.com/images/I/71iUWr9AgYL._AC_UF1000,1000_QL80_.jpg",
    "https://m.media-amazon.com/images/I/81Mehg9cPCL.jpg",
    "https://m.media-amazon.com/images/I/71Mspmwr4aL._AC_UF1000,1000_QL80_.jpg",
    "https://m.media-amazon.com/images/I/7171zQPDUKL._AC_UF1000,1000_QL80_.jpg",
    "https://m.media-amazon.com/images/I/81N4AavTB-L.jpg",
    "https://joueclub-joueclub-fr-storage.omn.proximis.com/Imagestorage/imagesSynchro/0/0/d46a8ee6930e53ad1231777e55c4ed9d1407c087_06029027.jpeg",
    "https://static.fnac-static.com/multimedia/Images/FR/NR/83/2a/20/2108035/1540-1/tsp20161013084410/La-guerre-des-moutons-Asmodee.jpg",
    "https://i1.wp.com/gusandco.net/wp-content/uploads/2018/09/robin-wood.jpg?fit=372%2C372",
    "https://www.lencephalo.com/wp-content/uploads/2018/08/la-fievre-de-l-or-eclate.jpg",
    "https://static.fnac-static.com/multimedia/FR/Images_Produits/FR/fnac.com/Visual_Principal_340/6/6/2/3558380000266/tsp20120919180422/Asmodee-Camelot.jpg",
    "https://joueclub-joueclub-fr-storage.omn.proximis.com/Imagestorage/imagesSynchro/0/0/6cf0708959e21c68eb8e490ca39d246834d6e10d_06023811.jpeg",
    "https://cdn2.philibertnet.com/533237-thickbox_default/kinoko.jpg",
    "https://cdn1.philibertnet.com/316332-large_default/noe.jpg",
    "https://img.over-blog.com/600x448/3/53/65/32/New/thecity.jpg",
    "https://cdn2.trictrac.net/documents/formats/enlargement/documents/originals/c8/6b/1a0149d176bb16780885df18101681a51c46.jpeg",
    "https://cdn1.trictrac.net/documents/formats/enlargement/documents/originals/55/4c/d06a49f13db0862b36a801bf799bdd690a0b.jpeg",
    "https://www.jeuxdenim.be/images/jeux/TchinTchin_large01.jpg",
    "https://m.media-amazon.com/images/I/61TVebb1n3L._AC_UF894,1000_QL80_.jpg",
    "https://www.espritjeu.com/upload/image/bluff-party---orange-p-image-78775-grande.png",
    "https://choupichoupa.fr/wp-content/uploads/2023/07/TAGGLE_2.png",
    "https://m.media-amazon.com/images/W/MEDIAX_792452-T2/images/I/41CWnxU4zlL._AC_UF1000,1000_QL80_.jpg",
    "https://www.espritjeu.com/upload/image/limite-limite-p-image-75040-grande.jpg",
    "https://m.media-amazon.com/images/I/816EWmXtejL._AC_UF1000,1000_QL80_.jpg",
    "https://cdn1.philibertnet.com/384580-large_default/exploding-kittens-vf.jpg",
    "https://www.gigamic.com/587-large_default/bazar-bizarre.jpg",
    "https://lagranderecre-lagranderecre-fr-storage.omn.proximis.com/Imagestorage/imagesSynchro/575/575/3701793ea39e6dacc23049e484a1a0252904ca76_IMG-PRODUCT-778201-1.jpeg",
    "https://www.ludicbox.fr/images/stories/virtuemart/product/munchkin-loot-letter-vf.jpg?auto=compress&cs=tinysrgb",
    "https://www.fairplay-jeux.com/1587/munchkin-6-le-donjon-de-la-farce.jpg"
    
]


liste_jv = [
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTURlDb7Mzq-HndzL4PJxp3lDfy-fBp-tFCmA&usqp=CAU",
    "https://gaming-cdn.com/images/products/2615/616x353/mario-kart-8-deluxe-switch-switch-jeu-nintendo-eshop-europe-cover.jpg?v=1649856900",
    "https://gaming-cdn.com/images/products/3000/orig/super-smash-bros-ultimate-switch-switch-jeu-nintendo-eshop-europe-cover.jpg?v=1649860652",
    "https://gaming-cdn.com/images/products/12567/616x353/minecraft-java-et-bedrock-edition-pc-jeu-europe-cover.jpg?v=1680508579",
    "https://m.media-amazon.com/images/I/71bNIxi11sL.jpg",
    "https://www.gamecash.fr/thumbnail-600/wii-sport-e15224.jpg",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ07iRyk0J8KhAqmfQ77R0Zbu4wF_PoN5MeDFzDsC0vYBP8fHn75WnYbonoNyHgVXkDCJA&usqp=CAU",
    "https://images.ctfassets.net/wn7ipiv9ue5v/6ZSV0CNlsw4xhNcCNK4haj/82d0f54cf5010ab9f05a5e5558d3b4f0/RDR2_HeroSquare_1080x1080.jpg",
    "https://image.api.playstation.com/vulcan/ap/rnd/202211/0711/kh4MUIuMmHlktOHar3lVl6rY.png",
]


liste_jr = [
    "https://www.letempledujeu.fr/IMG/arton18762.jpg?1670234252",
    "https://upload.wikimedia.org/wikipedia/en/thumb/c/ca/TSR9162_Lankhmar_City_Of_Adventure.jpg/220px-TSR9162_Lankhmar_City_Of_Adventure.jpg",
    "https://www.legrog.org/visuels/couvertures/4110.jpg",
    "https://upload.wikimedia.org/wikipedia/en/0/09/PlayersHandbook8Cover.jpg",
    "https://cdn3.philibertnet.com/380469-large_default/dungeons-dragons-5e-ed-dungeon-master-s-guide-guide-du-maitre-version-francaise.jpg",
    "https://www.legrog.org/visuels/couvertures/4959.jpg",
    "https://m.media-amazon.com/images/W/MEDIAX_792452-T2/images/I/7193e8OkGVL._AC_UF1000,1000_QL80_.jpg",
    "https://m.media-amazon.com/images/W/MEDIAX_792452-T2/images/I/91-sX3EVAFL._AC_UF894,1000_QL80_.jpg",
    "https://www.legrog.org/visuels/couvertures/7690.jpg",
    "https://www.legrog.org/visuels/couvertures/5430.jpg",
    "https://www.okkazeo.com/images/jeux/14397.jpg",
    "https://www.okkazeo.com/images/jeux/14397.jpg",
    "https://www.okkazeo.com/images/jeux/14397.jpg",
    "https://www.okkazeo.com/images/jeux/14397.jpg",
    "https://www.okkazeo.com/images/jeux/14397.jpg",
    "https://fr.shopping.rakuten.com/photo/1333076636.jpg",
    "https://gimmethedice.files.wordpress.com/2021/06/call_of_cthulhu_rpg_1st_ed_1981-1.jpg",
    "https://m.media-amazon.com/images/I/710eToptiBL._AC_UF894,1000_QL80_.jpg",
    "https://www.legrog.org/visuels/couvertures/11838.jpg",
    "https://www.legrog.org/visuels/couvertures/1203.jpg",
    "https://www.legrog.org/visuels/couvertures/4891.jpg",
    "https://fr.shopping.rakuten.com/photo/1185146062_L.jpg",
    "https://i.ebayimg.com/images/g/5yQAAOSwANZkGJEI/s-l1200.webp",
    "https://m.media-amazon.com/images/I/61ogDyZj8SL._AC_UF1000,1000_QL80_.jpg",
    "https://www.legrog.org/visuels/couvertures/3163.jpg",
    "https://www.legrog.org/visuels/couvertures/3310.jpg",
    "https://www.legrog.org/visuels/couvertures/2962.jpg",
    "https://www.legrog.org/visuels/couvertures/4864.jpg",
    "https://www.legrog.org/visuels/couvertures/828.jpg",
    "https://m.media-amazon.com/images/I/5183KJQE6XL._AC_UF1000,1000_QL80_.jpg",
    "https://static.fnac-static.com/multimedia/Images/FR/MDM/1c/fb/f8/16317212/1540-1/tsp20230505233800/Jeu-de-roles-Asmodee-L-Appel-de-Cthulhu-Les-Acceoires-du-Gardien.jpg",
    "https://www.legrog.org/visuels/couvertures/6614.jpg",
    "https://www.legrog.org/visuels/couvertures/3311.jpg",
    "https://m.media-amazon.com/images/W/MEDIAX_792452-T2/images/I/719nrQnk28L._AC_UF1000,1000_QL80_.jpg",
    "https://1.bp.blogspot.com/-PSEC4Cb62II/VuL6r2MnnBI/AAAAAAAAIX4/G9m2v8CfqU4hkQU5z3GVDDVKHkh58edyw/s1600/vanishing_conjurer.jpg",
    "https://fr.shopping.rakuten.com/photo/1984088097.jpg",
    "https://www.legrog.org/visuels/couvertures/3243.jpg",
    "https://www.legrog.org/visuels/couvertures/188.jpg",
    "https://m.media-amazon.com/images/I/81cw5IcoM+L._AC_UF1000,1000_QL80_.jpg",
    "https://m.media-amazon.com/images/I/811dDmyv-pL._AC_UF1000,1000_QL80_.jpg",
    "https://cdn2.philibertnet.com/371363-thickbox_default/dungeons-dragons-5e-ed-monster-manual-manuel-des-monstres-version-francaise.jpg",
    "https://www.legrog.org/visuels/couvertures/5405.jpg",
    "https://www.letempledujeu.fr/images/531.jpg?1585855369",
    "https://www.legrog.org/visuels/couvertures/4438.jpg",
    "https://www.legrog.org/visuels/couvertures/4716.jpg",
    
]


for i in range(len(liste_js)):
    cur.execute("UPDATE stock_game SET image = ? WHERE id = ?", (liste_js[i], i+1))

for i in range(len(liste_jv)):
    cur.execute("UPDATE stock_game SET image = ? WHERE id = ?", (liste_jv[i], i+408))
    
for i in range(len(liste_jr)):
    cur.execute("UPDATE stock_game SET image = ? WHERE id = ?", (liste_jr[i], i+418))"""

print("Images : OK")

conn.commit()
conn.close()

print("Fermeture : OK")
