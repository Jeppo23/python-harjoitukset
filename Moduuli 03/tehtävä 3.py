sukupuoli=input("mikä on sukupuolesi?" )
hemoglobiini =float(input("paljonko on hemoglobiini arvosi? "))

if sukupuoli == "nainen":
    if hemoglobiini <117:
        print("hemoglobiini arvo alhainen!")
    elif hemoglobiini <=175:
        print("hemoglobiini normaali!")
    else:
        print("hemoglobiini korkea!")

elif sukupuoli == "mies":
    if hemoglobiini <134:
        print("Hemoglobiiniarvo on alhainen.")
    elif hemoglobiini <=195:
        print("Hemoglobiiniarvo on normaali.")
    else:
        print("Hemoglobiiniarvo on korkea.")
