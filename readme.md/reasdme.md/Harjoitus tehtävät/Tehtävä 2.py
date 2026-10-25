kokonaisluku = int(input("syötä kokonaisluku: "))

if kokonaisluku % 3 == 0 and kokonaisluku % 5 == 0:
    print("jaollinen sekä kolmella että viidellä")

elif kokonaisluku % 3 == 0:
    print("kolmella jaollinen")

elif kokonaisluku % 5 == 0:
    print("jaollinen viidellä")

else:
    print("Ei ole 3 eikä 5 jaollinen")