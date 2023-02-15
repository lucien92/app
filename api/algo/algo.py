from shapely.geometry import Point
from shapely.geometry import Polygon, Point
import geopandas
import json
import pandas as pd

#on extrait les coordonnées du polygône de la maison de Clamart <3

def polygone(contenance):

    contenance = float(contenance)

    cadastre_path = "/home/lucien/Documents/app/data/cadastre-74281-parcelles.json"
    with open(cadastre_path) as config_buffer:
            cadastre = json.loads(config_buffer.read())



    #1) On récupère d'abord tous les polygônes correspondant au passerelle ayant la contenance indiquée
    liste_id = []
    for elem in cadastre["features"]:
        if "contenance" in elem["properties"]:
            test = elem["properties"]["contenance"]
            if test == contenance:
                liste_id.append(elem["id"])

    #on récupère cet id grâce à la contenance du cadatsre que l'on met en entrée
    list_polygone = []
    for id_test in liste_id:
        for elem in cadastre["features"]: #cadastre["features"] est une liste de dictionnaires
            id = elem["id"]
            if id == id_test:
                polygone = elem["geometry"]["coordinates"]
                list_polygone.append(polygone)

    #on veut transformer la liste de liste des polygônes en liste de tuples

    L3 = []
    for polygone in list_polygone:
        L2 = []
        for elem in polygone:
            for elem2 in elem:
                L2.append(tuple(elem2))
        polygon = Polygon(L2)
        L3.append(polygon)
    
    return L3

    

