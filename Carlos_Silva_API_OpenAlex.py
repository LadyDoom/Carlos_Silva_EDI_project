import json
import csv
import requests
import re
from time import sleep

w = requests.get("https://api.openalex.org/works?filter=author.id:https://openalex.org/A5100417531,publication_year:2019-2023&select=referenced_works&per-page=200")

refs = w.json()

# Créer un fichier json pour les références :
f1 = open("refs.json", "w")
f1.write(str(refs))
f1.close()

# Rouvrir le fichier créé en mode lecture :
f1 = open("refs.json", "r")

# Extraire seulement les "Work id" des références et les stocker dans une liste :
lst = re.findall('W[0-9]+', f1.read()) # trouve un W suivi de plusieurs chiffres
print(lst)
# pour chaque référence, extraire la liste des auteurs :
count = 1
rows = []
for i in lst :
    print(count)
    # on récupère les données d'OpenAlex
    article = requests.get("https://api.openalex.org/works/" + i + "?select=id,title,authorships")
    try:
        data = article.json()
    except :
        try :
            data = article.text()
            data = json.loads(data)
        except :
            row = ["json error with work " + i, "error"]
    try :
        row = [data["id"], data["title"]]
    except :
        row = ["error with work " + i, "error"]
    # On crée une liste avec les infos du premier auteur
    try :
        row.append(data["authorships"][0]["author"]["display_name"])
    except :
        row.append("error")
    try :
        row.append(data["authorships"][0]["author"]["id"])
    except :
        row.append("error")
    try :
        row.append(data["authorships"][0]["institutions"][0]["display_name"])
    except :
        row.append("error")
    try :
        row.append(data["authorships"][0]["raw_affiliation_strings"])
    except :
        row.append("error")
    # attendre 1 sec pour ne pas dépasser la limite de 10 requêtes/sec
    if (count % 10)==0:
        sleep(1)
    rows.append(row)
    count = count+1

# créer le fichier csv dans lequel on va mettre les données finales
fields = ["Work_id", "Title", "First author", "First author id", "Institution name", "Affiliation"]
filename = "auteurs.csv"
with open(filename, 'w', encoding="utf-8") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)