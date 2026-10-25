tuntipalkka = float(input("syötä tunti palkkasi: "))

tehdyttunnit = float(input("syötä tehdyt tunnit: "))

viikonpäivä = (input("syötä viikonpäivä: "))

päiväpalkka = tuntipalkka*tehdyttunnit

if viikonpäivä == "sunnuntai" or viikonpäivä == "su":
    päiväpalkka = tehdyttunnit * tuntipalkka * 2
else:
    päiväpalkka = tehdyttunnit * tuntipalkka

print("päiväpalkka on:", päiväpalkka)





