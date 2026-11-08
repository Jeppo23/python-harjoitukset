def poista_parittomat(luvut):
    parilliset = []

    for luku in luvut:
        if luku % 2 == 0:
            parilliset.append(luku)

    return parilliset

numerot = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

karsittu_lista = poista_parittomat(numerot)

print("Alkuperäinen lista:", numerot)
print("Karsittu lista:", karsittu_lista)