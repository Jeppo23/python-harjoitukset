
tuotteet = []
määrät = []

jatko = "Kyllä"

while jatko == "Kyllä":
    tuote = input("Mitä tuotetta valmistetaan? ")
    määrä = int(input("Kuinka monta valmistetaan? "))

    tuotteet.append(tuote)
    määrät.append(määrä)

    jatko = input("Jatketaanko tuotantoa? ")

print("Tuotanto lopetettu!")
print("Valmistetut tuotteet:")

for tuote in tuotteet:
    i = tuotteet.index(tuote)
    print(tuote, ":", määrät[i], "kpl")
