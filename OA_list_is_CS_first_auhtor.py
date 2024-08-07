import pandas

# Charger le fichier Excel
data = pandas.read_excel("Carlos_Silva_OpenAlex_2019-2023.xlsx")

# Sélectionner les colonnes souhaitées
colonnes_a_garder = [0, 2, 4, 7, 24, 112, 113, 115, 116]
data_reduit = data.iloc[:, colonnes_a_garder]
data_reduit = data_reduit.drop(labels=[48,49])

for colonne in data_reduit.columns[-4:]:
    try:
        data_reduit[colonne] = data_reduit[colonne].str.split('|', expand=True)[0]
    except:
        print("Error with line")

data_reduit.to_excel('fichier_reduit.xlsx', index=False)

print(data_reduit.head())