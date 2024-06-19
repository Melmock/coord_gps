## Sources & vérifications
## https://www.sunearthtools.com/fr/tools/distance.php
## https://fr.distance.to/Lyon,Rh%C3%B4ne,Auvergne-Rh%C3%B4ne-Alpes,FRA/Paris,%C3%8Ele-de-France,FRA
## https://fr.mappy.com/outils/calcul-rayon
## https://www.code-postal.com/59160.html
##
## Coord_gps_des_communes V1.0
##

import math 
import sqlite3     
import pandas as pd
from json import dumps

try:
    dbconnect = sqlite3.connect('coord_gps.sqlite3')
except Error as e:
    print(e)

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

def remove_empty_from_dict(d):
    if type(d) is dict:
        return dict((k, remove_empty_from_dict(v)) for k, v in d.items() if v and remove_empty_from_dict(v))
    elif type(d) is list:
        return [remove_empty_from_dict(v) for v in d if v and remove_empty_from_dict(v)]
    else:
        return d
    
def infos_depuis_ville(ville):
    dbcursor = dbconnect.cursor()
    sql = f"""select * from infosgps where Commune like '%{ville}%' or CommuneMAJ like '%{ville}%';"""
    dbcursor.execute(sql)
    records = dbcursor.fetchall()

    if len(records)>1:
        print('Plusieurs villes trouvées')
        for element in records:
            print(element[1])
        return None
    elif len(records)==0:
        print('Pas de ville trouvée')
        return None
    elif len(records)==1:
        columns = [col[0] for col in dbcursor.description]
        for record in records:
            record = dict(zip(columns, record))
        record=remove_empty_from_dict(record)   # Supprime les clées vides
        return record
    else:
        print('Erreur')
        return None

def cherche_code_postal_depuis_ville(ville,TypeRecherche='Exact'):
    match TypeRecherche:
        case 'contient':
            sql = f"""select CodePostal,Commune from infosgps where Commune like '%{ville}%' or CommuneMAJ like '%{ville}%' order by CodePostal,Commune;"""
        case 'exact':
            sql = f"""select CodePostal,Commune from infosgps where Commune like '{ville}' or CommuneMAJ like '{ville}' order by CodePostal,Commune;"""
        case 'commence':
            sql = f"""select CodePostal,Commune from infosgps where Commune like '{ville}%' or CommuneMAJ like '{ville}%' order by CodePostal,Commune;"""
        case _:
            sql = f"""select CodePostal,Commune from infosgps where Commune like '%{ville}%' or CommuneMAJ like '%{ville}%' order by CodePostal,Commune;"""

    df  = pd.read_sql(sql, dbconnect)
    if len(df.index)==0:
        print("Pas de résultat")
    else:
        print(df)

def cherche_ville_depuis_code_postal(code_postal):
    sql      =f"""select CodePostal,CodeInsee,Commune from infosgps where CodePostal like '%{code_postal}%';"""
    df = pd.read_sql(sql, dbconnect)
    if len(df.index)==0:
        print("Pas de résultat")
    else:
        print(df)

def distance_entre_deux_villes(ville1,ville2):
    dbcursor = dbconnect.cursor()
    sql      =f"""select CoordCommune_X,CoordCommune_Y from infosgps where Commune like '{ville1}' or CommuneMAJ like '{ville1}';"""
    dbcursor.execute(sql)
    records = dbcursor.fetchall()
    
    if len(records)>1 or len(records)==0:
        print('erreur',sql)
    else:
        ville1_coord_x=records[0][0]
        ville1_coord_y=records[0][1]

    sql      =f"""select CoordCommune_X,CoordCommune_Y from infosgps where Commune like '{ville2}' or CommuneMAJ like '{ville2}';"""
    dbcursor.execute(sql)
    records = dbcursor.fetchall()
    
    if len(records)>1 or len(records)==0:
        print('erreur',sql)
    else:
        ville2_coord_x=records[0][0]
        ville2_coord_y=records[0][1]
    distance=math.acos(math.sin(math.radians(ville1_coord_x))*math.sin(math.radians(ville2_coord_x))+math.cos(math.radians(ville1_coord_x))*math.cos(math.radians(ville2_coord_x))*math.cos(math.radians(ville1_coord_y-ville2_coord_y)))*6371
    print(f"La distance à vol d'oiseau entre {ville1} et {ville2} est de {distance:.2f} km")

def trouver_ville_autour_de_x_km(ville,km=10):
    dbcursor = dbconnect.cursor()
    sql      =f"""select CoordCommune_X,CoordCommune_Y from infosgps where Commune like '{ville}';"""
    dbcursor.execute(sql)
    records = dbcursor.fetchall()

    if len(records)>1 or len(records)==0:
        print('erreur',sql)
    else:
        ville1_coord_x=records[0][0]
        ville1_coord_y=records[0][1]

    sql      = f"""select CoordCommune_X,CoordCommune_Y,Commune,Population from infosgps;"""
    dbcursor.execute(sql)
    records = dbcursor.fetchall()
    df = pd.DataFrame({'ville':[],'distance':[],'population':[]})
    for ville in records:
        ville2_coord_x      = ville[0]
        ville2_coord_y      = ville[1]
        ville_nom           = ville[2]
        population          = ville[3]

        try:
            distance=math.acos(math.sin(math.radians(ville1_coord_x))*math.sin(math.radians(ville2_coord_x))+math.cos(math.radians(ville1_coord_x))*math.cos(math.radians(ville2_coord_x))*math.cos(math.radians(ville1_coord_y-ville2_coord_y)))*6371
            if (distance>0.1) and (distance<=km):
                #print(f"{ville_nom}\t\t\t\t\t\t{distance:0.2f}")
                new_row={'ville':ville_nom,'distance':round(distance,2),'population':int(population*1000)}
                df.loc[len(df)] =new_row
        except:
            None
    df = df.sort_values(by=['distance'])
    print(df)


cherche_code_postal_depuis_ville('Bagnères-de-Bigorre')
print('-----------------------')
cherche_ville_depuis_code_postal('65200')
print('-----------------------')
distance_entre_deux_villes('lyon','paris')
print('-----------------------')
trouver_ville_autour_de_x_km('Bagnères-de-Bigorre',10)
print('-----------------------')

info_ville  = infos_depuis_ville('Bagnères-de-Bigorre')
if info_ville != None:
    df          = pd.DataFrame([info_ville])
    print(df.T)
    #print(dumps(info_ville,indent=2))  # Sortie en Json
print('-----------------------')

dbconnect.close()
print('Fin')