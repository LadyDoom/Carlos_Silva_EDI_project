Ce dossier contient deux scripts Python qui exploitent l'API d'[OpenAlex](https://openalex.org/) :

[Carlos_Silva_API_OpenAlex.py](https://github.com/LadyDoom/Carlos_Silva_EDI_project/blob/main/Carlos_Silva_API_OpenAlex.py) va chercher la liste des références des articles de Carlos Silva publiés entre 2019 et 2023 et va chercher les infos du premier auteur.
Il génère un tableau dont chaque ligne correspond à une référence. Pour chaque référence, les colonnes indiquent :
- son id OpenAlex
- son titre
- le premier auteur
- l'id OpenAlex du premier auteur
- le nom de l'institution de provenance du premier auteur
- le nom de l'affiliation du premier auteur

[CS_API_OA_with_source.py](https://github.com/LadyDoom/Carlos_Silva_EDI_project/blob/main/CS_API_OA_with_source.py) va chercher la liste des références des articles de Carlos Silva publiés entre 2019 et 2023 et va chercher les infos du premier auteur.
Il génère un tableau dont chaque ligne correspond à une référence. Pour chaque référence, les colonnes indiquent :
- **l'id OpenAlex de l'article dans lequel elle est citée**
- son id OpenAlex
- son titre
- le premier auteur
- l'id OpenAlex du premier auteur
- le nom de l'institution de provenance du premier auteur
- le nom de l'affiliation du premier auteur

Il contient aussi un script Python qui traite le fichier Carlos_Silva_OpenAlex_2019-2023.xlsx afin d'obtenir uniquement les premiers auteurs des articles co-écrits par Carlos Silva. Les colonnes retenues sont :
- l'id OpenAlex de l'article
- son titre
- l'année de publication
- le type de document
- le nombre de références de l'article
- le nom du premier auteur
- l'institution de provenance du premier auteur
- l'id OpenAlex du premier auteur
