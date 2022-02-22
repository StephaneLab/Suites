#!/usr/bin/python3.9
# Licence GPL3 copyright (c) 2022 Stéphane Lassalvy
import pandas as pd
import numpy as np
def my_ApproximationE(n):
    # Pour les élèves de terminale
    # Calcule les n premiers termes de la suite u(n) = (1 + 1/n)^n
    # Cette suite converge vers le nombre e tel que exp(1) = e
    # Remarque : e est environ égal à 2,718
    if n == 0:
        print("n doit être non nul")
    else:
        # Liste des rangs pour lesquels on calcule u(n)
        Rang   = []
        # Liste des termes de la suite u
        u      = []
        # Liste des distances entre u(n) et le nombre e
        Delta_ue = []
        # Compteur
        count = 1
        # Application de la formule de récurrence pour les rangs >= 2 jusqu'à n
        while count <= n:
            Rang.append(count)
            u_count = (1 + 1/count)**count
            delta_ue = abs(u_count - np.exp(1))
            print(f"Au rang {count} : u({count}) = {u_count}")
            u.append(u_count)
            Delta_ue.append(delta_ue)
            count += 1
        print("")
        print(f"Calcul des n = {n} premiers termes de la suite u(n) = (1 + 1/n)^n :")
        Rang        = pd.DataFrame(Rang, columns=["Rang n"])
        u           = pd.DataFrame(u, columns = ["Terme u(n)"])
        Delta_ue    = pd.DataFrame(Delta_ue, columns = ["|u(n) - e|"])
        Resultat    = Rang.join(u)
        Resultat    = Resultat.join(Delta_ue)
        print(Resultat)
# Exécution de la fonction
# Détermination du rang n pour lequel on veut calculer les rangs de la suite de 0 à n
print("Veuillez saisir le rang n jusqu'auquel vous voulez calculer les termes de la suite :\n")
n = input("n = ")
print("\n")
n = int(n)
my_ApproximationE(n)