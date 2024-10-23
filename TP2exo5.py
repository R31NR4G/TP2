nbr= int(input("Entrez un nombre entier:"))
if nbr == 0:
    print("le nombre est O est pair")
elif nbr % 2 == 0:
    if nbr > 0:
        print("le nombre est pair et positif")
    else:
        print("le nombre est pair et negatif")

if  nbr % 2 == 1:
    if nbr < 0:
        print("le nombre est impair et positif")
    else:
        print("le nombre est impair et negatif")
