import math

def yksikkohinta(halkaisija, hinta):
    sade = halkaisija / 2
    pinta_ala = math.pi * sade ** 2
    pinta_ala_m2 = pinta_ala / 10000
    return hinta / pinta_ala_m2



halkaisija1 = float(input("Anna ensimmäisen pizzan halkaisija senttimetreinä: "))
hinta1 = float(input("Anna ensimmäisen pizzan hinta euroina: "))

halkaisija2 = float(input("Anna toisen pizzan halkaisija senttimetreinä: "))
hinta2 = float(input("Anna toisen pizzan hinta euroina: "))

hinta_m2_1 = yksikkohinta(halkaisija1, hinta1)
hinta_m2_2 = yksikkohinta(halkaisija2, hinta2)

print("Ensimmäisen pizzan yksikköhinta:", round(hinta_m2_1, 2), "€/m2")
print("Toisen pizzan yksikköhinta:", round(hinta_m2_2, 2), "€/m2")

if hinta_m2_1 < hinta_m2_2:
    print("Ensimmäinen pizza on edullisempi.")
elif hinta_m2_2 < hinta_m2_1:
    print("Toinen pizza on edullisempi.")
else:
    print("Molemmat pizzat ovat yhtä edullisia.")