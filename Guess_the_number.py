import random

# Boucle pour recommencer une partie à l'infini
while True:
    nombre = random.randint(1, 10000)
    reponse = None

    # Tant que la réponse n'est pas égale au nombre, on boucle
    while reponse != nombre:
        reponse = int(input("Guess the number between 1 and 10000:"))

        if reponse == nombre:
            print("You guessed the number.")
        elif reponse < nombre:
            print("The number is greater than : ", reponse)
        else:
            print("The number is smaller than : ", reponse)
