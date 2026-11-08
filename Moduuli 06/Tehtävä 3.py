def muunna_litroiksi(gallonat):
    return gallonat * 3.785


while True:
    gallonat = float(input("Anna gallonamäärä: "))

    if gallonat < 0:
        break

    litrat = muunna_litroiksi(gallonat)
    print(f"{gallonat} gallonaa on {litrat:.2f} litraa.")