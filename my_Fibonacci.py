#!/usr/bin/python3.9
# Licence GPL3 copyright (c) 2022 Stéphane Lassalvy
import pandas as pd
import numpy as np
def my_Fibonacci(n):
    # Calcule les n premiers termes d'une suite de Fibonacci
    # Initialisation F(0) = 0, F(1) = 1
    # Formule de récurrence : F(n) = F(n-1) + F(n-2)
    # C'est une suite définie par une récurrence double
    if n < 2:
        print("n doit être supérieur ou égal à 2")
    else:
        # Initialisation des deux premiers rangs connus et des deux premières valeurs connues de la suite
        F     = [0,1]
        Rang  = [0,1]
        print("F(0) = 0")
        print("F(1) = 1")
        # Initialisation du premier rang à calculer par récurrence
        count = 2
        # Application de la formule de récurrence pour les rangs >= 2 jusqu'à n
        while count <= n:
            print(f"Au rang n = {count}")
            print(f"F({count-2}) + F({count-1}) = F({count})")
            Rang.append(count)
            F.append(F[count-2] + F[count-1])
            print(f"{F[count-2]} + {F[count - 1]} = {F[count]}")
            count += 1
        print("\n")
        print(f"Calcul des n = {n} premiers termes de la suite de Fibonacci:")
        Rang = pd.DataFrame(Rang, columns=["Rang n"])
        F    = pd.DataFrame(F, columns = ["Terme F(n)"])
        Resultat = Rang.join(F)
        print(Resultat)
# Exécution de la fonction
# Détermination du rang n pour lequel on veut calculer les rangs de la suite de 0 à n
print("Veuillez saisir le rang n jusqu'auquel vous voulez calculer les termes de la suite :\n")
n = input("n = ")
print("\n")
n = int(n)
my_Fibonacci(n)