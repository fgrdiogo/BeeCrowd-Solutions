T1 = input()
T2 = input()
T3 = input()

if T1 == "vertebrado":
    if T2 == "ave":
        if T3 == "carnivoro":
            print("aguia")
        elif T3 == "onivoro":
            print("pomba")
    elif T2 == "mamifero":
        if T3 == "onivoro":
            print("homem")
        elif T3 == "herbivoro":
            print("vaca")

elif T1 == "invertebrado":
    if T2 == "inseto":
        if T3 == "hematofago":
            print("pulga")
        elif T3 == "herbivoro":
            print("lagarta")
    elif T2 == "anelideo":
        if T3 == "hematofago":
            print("sanguessuga")
        elif T3 == "onivoro":
            print("minhoca")