luvut = []

while True:
    syote = input("Anna luku (lopeta tyhjällä merkkijonolla): ")

    if syote == "":
        break

    luvut.append(float(syote))

luvut.sort(reverse=True)

print("Viisi suurinta lukua:")

for luku in luvut[:5]:
    print(luku)