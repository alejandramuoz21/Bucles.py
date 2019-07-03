comics_usario = 0
num_comics = int(input("Cuantos comics te gustaria tener?"))
while comics_usario < num_comics:
    print("Tienes", comics_usario, "comics. ")
    print("Has comprado un comic nuevo. ")
    comics_usario += 1


num_comics = int(input("Cuantos comics te gustaria tener?"))
while num_comics <= 0:
    print("Debes introducir un numero mayor que cero. ")
    num_comics = int(input("Cuantos comics te gustaria tener?"))