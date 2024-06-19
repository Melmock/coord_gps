**<p style="text-align: center;">Coordonnées GPS des communes francaises</p>**

- [Installation](#installation)
- [Introduction](#introduction)
  - [Fonctionnalités clées](#fonctionnalités-clées)
  - [Avantages pour les Commerciaux](#avantages-pour-les-commerciaux)
  - [Cas d'Usage](#cas-dusage)
  - [Conclusion](#conclusion)
- [Librairie python:](#librairie-python)
  - [cherche\_code\_postal\_depuis\_ville(ville,TypeRecherche)](#cherche_code_postal_depuis_villevilletyperecherche)
  - [cherche\_ville\_depuis\_code\_postal(code\_postal)](#cherche_ville_depuis_code_postalcode_postal)
  - [distance\_entre\_deux\_villes(ville1,ville2)](#distance_entre_deux_villesville1ville2)
  - [trouver\_ville\_autour\_de\_x\_km(ville,km=10):](#trouver_ville_autour_de_x_kmvillekm10)
  - [infos\_depuis\_ville(ville)](#infos_depuis_villeville)
- [Sources](#sources)
- [Vérifications:](#vérifications)

# Installation

Librairies nécessaires commandes à lancer depuis un prompt ("cmd.exe")

1. pip install pandas
2. pip install sqlite3
3. pip install json -> Si vous utilisez des exports en json uniquement

# Introduction

Ce logiciel répond aux besoins des commerciaux en déplacement. Il a été conçu afin de maximiser les visites des clients et optimiser les trajets.
Cette librairie a été intégré à nos logiciels pour téléphones (iPhone) & tablettes (iPad). Elle est autonome grace à sa base de données intégrée. En effet nos commerciaux sont régulièrement en zone "blanche" ou couverte uniquement par du edge.

## Fonctionnalités clées

  - Détection des Villes dans un périmètre déterminé :
    - Entrez un rayon en kilomètres, et ce logiciel identifiera instantanément toutes les villes situées dans ce périmètre.
    - Vous pouvez ainsi planifier vos visites de manière stratégique et ne manquer aucun client potentiel dans la zone sélectionnée.

  - Optimisation des voyages :
    - Lors de la visite d’un client, ce logiciel vous aide à repérer d’autres clients ou prospects à proximité.
    - Gagnez du temps et des ressources en regroupant vos visites de manière intelligente et en réduisant les déplacements inutiles.

## Avantages pour les Commerciaux

- Gain de Temps : Concentrez-vous sur les interactions commerciales plutôt que sur la planification des déplacements.
- Efficacité Accrue : Maximisez le nombre de visites par jour grâce à une organisation optimale des trajets.
- Économie de Coûts : Réduisez les dépenses liées aux déplacements en évitant les trajets inutiles.
- Amélioration de la Relation Client : Multipliez les opportunités de rencontrer des clients et prospects en étant systématiquement au bon endroit au bon moment.

## Cas d'Usage

Imaginez un commercial se rendant à Lyon pour visiter un client. Grâce à ce logiciel :

    Il peut découvrir que plusieurs autres clients ou prospects se trouvent dans un rayon de 50 km.
    Il planifie ses visites de manière à rencontrer le maximum de clients en un seul trajet, optimisant ainsi son temps et ses ressources.

## Conclusion

Ce logiciel/librairie permet pour tout commercial d'optimiser ces déplacement.

# Librairie python:
## cherche_code_postal_depuis_ville(ville,TypeRecherche)
**Fonction**:
Permet de retrouver un code postal depuis le nom d'une ville

**Paramètres:**
ville : Nom de la ville avec ou sans accent

Type recherche:
1. 'exact' 
   
   Recherche exactement le nom de cette ville (avec ou sans accent)

    cherche_code_postal_depuis_ville('lyon','exact')
    
    |No|CodePostal|Commune|
    |-|----------|-------|
    |0|69000|Lyon|  

2. 'contient'
Recherche toutes les villes qui contiennent ce nom (avec ou sans accent)

    cherche_code_postal_depuis_ville('lyon','contient')
    
    |No|CodePostal|Commune|
    |-|---------|-------|
    |0|03110|Cognat-Lyonne|
    |1|27480|Beauficel-en-Lyons|
    |2|27480|Lyons-la-Forêt|
    |3|42140|Chazelles-sur-Lyon|
    |4|69000|Lyon|
    |5|69001|Lyon 1er|
    |6|69002|Lyon 2e|
    |7|69003|Lyon 3e|
    |8|69004|Lyon 4e|
    |9|69005|Lyon 5e|
    |10|69006|Lyon 6e|
    |11|69007|Lyon 7e|
    |12|69008|Lyon 8e|
    |13|69009|Lyon 9e|
    |14|69110|Sainte-Foy-lès-Lyon|
    |15|76220|Beauvoir-en-Lyons|

3. commence
Recherche toutes les villes qui commencent par ce nom (avec ou sans accent)
    
    cherche_code_postal_depuis_ville('lyon','commence')

    |No|CodePostal|Commune|
    |-|---------|-------|
    |0|27480|Lyons-la-Forêt|
    |1|69000|Lyon|
    |2|69001|Lyon 1er|
    |3|69002|Lyon 2e|
    |4|69003|Lyon 3e|
    |5|69004|Lyon 4e|
    |6|69005|Lyon 5e|
    |7|69006|Lyon 6e|
    |8|69007|Lyon 7e|
    |9|69008|Lyon 8e|
    |10|69009|Lyon 9e|

## cherche_ville_depuis_code_postal(code_postal)
**Fonction**:
Renvoi la ou les villes correspondant au code postal

**Paramètres:**
N° du code postal

  cherche_ville_depuis_code_postal('65200')

  |No|CodePostal|Commune|
  |-|---------|-------|
  |0|65200|65024|Argelès-Bagnères|
  |1|65200|65043|Astugue|
  |2|65200|65147|Cieutat|
  |3|65200|65198|Gerde|
  |4|65200|65221|Hiis|
  |5|65200|65238|Labassère|
  |6|65200|65281|Loucrup|
  |7|65200|65370|Pouzac|
  |8|65200|65459|Uzer|
  |9|65200|65479|Visker|
  |10|65200|65216|Hauban|
  |11|65200|65275|Lies|
  |12|65200|65310|Mérilheu|
  |13|65200|65335|Ordizan|
  |14|65200|65016|Antist|
  |15|65200|65060|Banios|
  |16|65200|65200|Germs-sur-l'Oussouet|
  |17|65200|65451|Trébons|
  |18|65200|65042|Asté|
  |19|65200/65710|65059|Bagnères-de-Bigorre|
  |20|65200|65300|Marsas|
  |21|65200|65320|Montgaillard|
  |22|65200|65328| Neuilh|
  |23|65200|65338|Orignac|

## distance_entre_deux_villes(ville1,ville2)
**Fonction**:
Retourne le nombre de km à vol d'oiseau entre 2 villes

**Paramètres:**
ville1 et ville2

    distance_entre_deux_villes('lyon','paris')
    La distance à vol d'oiseau entre lyon et paris est de 392.08 km
    
## trouver_ville_autour_de_x_km(ville,km=10):
**Fonction**:
Retourne la liste des villes dans un rayon de x km

**Paramètres:**
ville et nombre de km
  
  trouver_ville_autour_de_x_km('Bagnères-de-Bigorre',10)

  |No|ville|distance|population|
  |-|-----|--------|----------|
  |7|Beaudéan|0.97|400|
  |9|Germs-sur-l'Oussouet|7.10|100|
  |10|Asté|7.33|500|
  |3|Labassère|7.57|300|
  |0|Gerde|7.74|1200|
  |8|Campan|8.27|1500|
  |2|Gazost|8.54|100|
  |4|Pouzac|9.14|1100|
  |6|Banios|9.15|100|
  |5|Lies|9.29|100|
  |1|Ourdis-Cotdoussan|9.41|0|
  |11|Marsas|9.57|100|
  |12|Neuilh|9.63|100|

## infos_depuis_ville(ville)
**Fonction**:
Retourne toutes les informations de la bdd d'une ville donnée

**Paramètres:**
ville recherchée

    info_ville  = infos_depuis_ville('Bagnères-de-Bigorre')

    CodeInsee                                                            65059
    Commune                                                Bagnères-de-Bigorre
    CommuneMAJ                                             BAGNERES DE BIGORRE
    CoordCommune_X                                                   42.999357
    CoordCommune_Y                                                    0.128684
    CodePostal                                                     65200/65710
    Altitude                                                            1544.0
    Superficie                                                         12587.0
    Population                                                             8.0
    CodeCommune                                                             59
    CodeArrondissement                                                       2
    CodeCanton                                                               4
    Statut                                                     Sous-préfecture
    CoordMairie_X                                                    43.068077
    CoordMairie_Y                                                     0.150577
    No departement                                                          65
    Departement                                                Hautes-Pyrénées
    Region                                                           Occitanie
    Ancienne region                                              Midi-Pyrénées
    No Etablissements publics de coopération interc...               246500482
    Etablissements publics de cooperation intercomm...  CC de la Haute-Bigorre
    Unites urbaines et communes rurales                    Bagnères-de-Bigorre
    Academie                                                          Toulouse
    Regroupement                                                      Province

# Sources
1. https://www.data.gouv.fr/fr/datasets/
2. https://public.opendatasoft.com/explore/?sort=modified
3. https://www.insee.fr/fr/accueil

# Vérifications:
1. https://www.sunearthtools.com/fr/tools/distance.php
2. https://fr.distance.to/Lyon,Rh%C3%B4ne,Auvergne-Rh%C3%B4ne-Alpes,FRA/Paris,%C3%8Ele-de-France,FRA
3. https://fr.mappy.com/outils/calcul-rayon
4. https://www.code-postal.com/59160.html
