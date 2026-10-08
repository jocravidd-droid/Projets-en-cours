while True:

    try:
        
        print("\nS (SOMME GÉOMETRIQUE) ou CG (Calcul Géometrique) ou CA (Calcul Arithmétique)\n")

        choice = input('Choix : ').upper()

        match choice:
            case 'CG':
                P = float(input('Premier terme : '))
                Q = float(input('Raison (q) : '))
                print(f"Le terme {P} de raison q = {Q}")
                start = int(input('Terme de départ (exemple : U2 = 2, terme de départ) : '))
                stop = int(input('Terme d\'arrêt (exemple: U2 a U10 = 10) : '))
                if start <= 0:
                    print(f'Mon programme n\'accepte pas un indice de départ inférieur ou égal à 0 : {start}.')
                elif stop < start:
                    print(f'La fin du compte : {stop} est plus petite que le début.')
                else:
                    for i in range(start, stop + 1):
                        U = P * Q**(i-1)
                        print(f"U{i} = {round(U, 2)}")
            case 'S':
                P = float(input('Premier terme : '))
                Q = float(input('Raison (q) : '))
                n = int(input("Somme de combien de termes : "))
                if n < 1:
                    print("Le nombre de termes utilisé pour la somme ne peut pas être inférieur à 1.")
                elif Q != 1:
                    S = P * ((1-Q**n) / (1-Q))
                    print(f"La somme et : {round(S, 2)}")
                else:
                    S = P * n
                    print(f"La somme et : {round(S, 2)}")
            case 'CA':
                P = float(input('Premier terme : '))
                R = float(input('Raison (r) : '))
                print(f"le terme {P} de raison r = {R}")
                start = int(input('Terme de départ (exemple: U2 = 2 terme de depart) : '))
                stop = int(input('Terme d\'arret (exemple: U2 a U10 = 10) : '))
                if start <= 0:
                    print(f'Mon programme n\'accepte pas un indice de départ inférieur ou égal à 0 : {start}.')
                elif stop < start:
                    print(f'La fin du compte : {stop} et plus petit que le debut : {start}')
                else:
                    for i in range(start, stop + 1):
                        U = P + (i-1) * R
                        print(f"U{i} = {round(U, 2)}")
            case _:
                print("Choix Inconnu !")
    except ValueError:
        print("Mauvaise Valeur !")
