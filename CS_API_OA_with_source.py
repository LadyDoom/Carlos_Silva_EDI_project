# importation des packages nécessaires
import json
import csv
import requests
from time import sleep

# Requête pour obtenir toutes les références citées par C. Silva dans les 5 dernières années complètes
w = requests.get("https://api.openalex.org/works?filter=author.id:https://openalex.org/A5100417531,publication_year:2019-2023&select=id,referenced_works&per-page=200")

# on met ça en json
refs = json.loads(w.content)
refs = refs['results']

# Créer un fichier json pour les références :
f1 = open("refs_w_ids.json", "w")
f1.write(str(refs))
f1.close()

# pour chaque référence, extraire la liste des auteurs :
count = 1
rows = []
for i in refs :

    for j in i['referenced_works'] :
        print(count)
        # on met l'id de l'article source
        row = [i['id']]
        # on récupère les données d'OpenAlex pour chaque référence
        article = requests.get("https://api.openalex.org/works/" + j.replace("https://openalex.org/", "") + "?select=id,title,authorships")

        # On stocke ça en json dans une variable (si on peut)
        try:
            data = article.json()
        except :
            try :
                data = article.text()
                data = json.loads(data)
            except :
                row = [i['id'], "json error with work " + j.replace("https://openalex.org/", ""), "error"]

        # on extrait les données dont on a besoin et on les stocke dans notre liste "row"
        try :
            row = [i['id'], data["id"], data["title"]]
        except :
            row = [i['id'], ("error with work " + j.replace("https://openalex.org/", ""), "error")]
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

        # attendre 1 sec pour ne pas dépasser la limite de 10 requêtes/sec imposée par OpenAlex
        if (count % 10)==0:
            sleep(1)

        # On ajoute cette nouvelle ligne à notre liste de lignes et on idente le compteur
        rows.append(row)
        count = count+1

# créer le fichier csv dans lequel on va mettre les données finales
fields = ["Cited in", "Work_id", "Title", "First author", "First author id", "Institution name", "Affiliation"]
filename = "auteurs_w_source.csv"
with open(filename, 'w', encoding="utf-8") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)