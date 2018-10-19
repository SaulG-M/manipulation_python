phrase = input("saisissez une phrase").lower()
voyelles = ["a",'e','i','o','u','y']
compteur = 0
for lettre in phrase:
    if lettre in voyelles:
        compteur+=1
print("la phrase saisie comporte donc ",compteur,"voyelles")
