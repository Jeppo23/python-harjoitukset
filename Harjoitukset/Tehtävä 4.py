from math import sqrt

kokonaisluku = int(input("syötä kokonaisluku: "))

while kokonaisluku != 0:

    if kokonaisluku < 0:
     print("Virheellinen numero")

    else:
        print(sqrt(kokonaisluku))

    kokonaisluku = int(input("syötä kokonaisluku: "))
    