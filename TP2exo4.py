BASE = 4
fromage = 800.0
eau = 2
ail = 2
pain = 400
nbConvives = int(input("Entrez le nombre de personne(s) conviées à la fondue:"))
Nfromage = fromage * nbConvives / BASE
Neau = eau * nbConvives / BASE
Nail = ail * nbConvives / BASE
Npain =pain * nbConvives / BASE
print(f"Pour faire une fondue fribourgeoise pour {nbConvives} personnes, il vous faut:  \n-{Nfromage} gr de fromage, \n-{Neau} dl d'eau, \n-{Nail} gousse d'ail, \n-{Npain} ,gr de pain."
)