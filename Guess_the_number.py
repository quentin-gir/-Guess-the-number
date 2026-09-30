import random

# Boucle pour recommencer une partie à l'infini
while True:
    nombre = random.randint(1, 100)
    reponse = None

    # Tant que la réponse n'est pas égale au nombre, on boucle
    while reponse != nombre:
        reponse = int(input("Devine le nombre entre 1 et 100 : "))

        if reponse == nombre:
            print("Tu as deviné le nombre.")
        elif reponse < nombre:
            print("Le nombre est plus grand que", reponse)
        else:
            print("Le nombre est plus petit que", reponse)