#!/usr/bin/python3.9
# Licence GPL3 copyright (c) 2022 Stéphane Lassalvy
import time as time
def (u_p, p, n, r):
    # Pour une suite u, calcule u_n à partir de u_p à partir de la formule de récurrance u(n+1) = u(n) + r
    # Paramètres d'entrée
    # u_p : valeur d'un premier terme connu u_p
    # p   : valeur du rang p correspondant
    # n   : valeur du rang n pour lequel on veut connaitre u(n)
    # r   : raison (additive) de la suite
    # Paramètre de sortie
    # u_n : valeur u(n) du terme calculé
    print("Suites arithmétiques")
    print("--------------------")
    print(f"u(p) = u({p}) = {u_p}\n")
    print(f"n - p = {n} - {p} = {n - p}\n")
    print(f"r = {r}\n")
    print(f"Calcul de u({n}) à partir d'un terme connu u(p) de la suite u et de sa définition récurrente u(n+1) = u(n) + r :\n")
    temps_depart = time.time()
    u = u_p
    # On applique la formule de réccurrence n-p fois pour calculer u_n
    for i in range(n-p): # range(n-p) compte de 0 à n-p-1 ce qui fait bien n-p termes
        u = u + r
    u_n = u
    print(f"La valeur du terme u({n}) est u({n}) = {u_n}\n")
    delta_temps = time.time() - temps_depart
    print(f"Temps d'exécution du calcul : {delta_temps} secondes.\n")
    return(u_n)
def u_arith_expl(u_p, p, n, r):
    # Pour une suite u, calcule u_n à partir de u_p à partir d'une formule explicite
    # Paramètres d'entrée
    # u_p : valeur d'un premier terme connu u_p
    # p   : valeur du rang p correspondant
    # n   : valeur du rang n pour lequel on veut connaitre u(n)
    # r   : raison (additive) de la suite
    # Paramètre de sortie
    # u_n : valeur u(n) du terme calculé
    print("Suites arithmétiques")
    print("--------------------")
    print(f"u(p) = u({p}) = {u_p}\n")
    print(f"n - p = {n} - {p} = {n - p}\n")
    print(f"r = {r}\n")
    print(f"Calcul de u({n}) à partir d'une formule explicite u(n) = u(p) + (n - p) * r:\n")
    temps_depart = time.time()
    u_n = u_p + (n - p) * r
    print(f"la valeur du terme u({n}) est u({n}) =  {u_p} + {(n - p)} * {r} = {u_n}\n")
    delta_temps = time.time() - temps_depart
    print(f"Temps d'exécution du calcul : {delta_temps} secondes.\n")
    return(u_n)
# Détermination du rang n pour lequel on veut calculer le terme u(n)
print("calcul du terme u(n) d'une suite arithmétique u connaissant un terme u(p) de la suite et sa raison r")
print("----------------------------------------------------------------------------------------------------\n")
print("Veuillez saisir le rang p du terme u(p) que vous connaissez :\n")
p = int(input("p = "))
print("")
print("Veuillez saisir la valeur du terme u(p) de rang p que vous connaissez :\n")
u_p = float(input("u_p = "))
print("")
print("Veuillez saisir la valeur r de la raison de la suite :\n")
r = float(input("r = "))
print("")
print("Veuillez saisir le rang n pour lequel vous voulez calculer u(n) :\n")
n = int(input("n = "))
print("\n")
print("Méthode 1, calcul de u(n) de façon réccurrente")
print("")
u_arith_rec(u_p ,p , n, r)
print("Méthode 2, calcul de u(n) de façon explicite")
print("")
u_arith_expl(u_p ,p , n, r)
print("Y a t-il une méthode plus rapide selon vous ?")
print("Réponse : si on fait les calculs à la main, il faut connaitre tous les termes de p à n pour la méthode par récurrence, la méthode explicite est donc plus rapide.")