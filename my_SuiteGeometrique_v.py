#!/usr/bin/python3.9
# Licence GPL3 copyright (c) 2022 Stéphane Lassalvy
import time as time
def (v_p, p, n, q):
    # Pour une suite v, calcule v_n à partir de v_p par la formule de récurrence v(n+1) = v(n) * q
    # Paramètres d'entrée
    # v_p : valeur d'un premier terme connu v_p
    # p   : valeur du rang p correspondant
    # n   : valeur du rang n pour lequel on veut connaitre v_n = v(n)
    # q   : raison (multiplicative) de la suite
    # Paramètre de sortie
    # v_n : valeur v_n du terme calculé
    print("Suites géométriques")
    print("-------------------")
    print(f"On connait le terme v({p}) de la suite v, v({p}) = {v_p},  la raison de la suite est q = {q}\n")
    print(f"v(p) = v({p}) = {v_p}\n")
    print(f"n - p = {n} - {p} = {n - p}\n")
    print(f"q = {q}\n")
    print(f"Calcul de v({n}) à partir du terme connu v({p}) et de la définition récurrente v(n+1) = v(n) * q :\n")
    temps_depart = time.time()
    v = v_p
    # On applique la formule de réccurrence n-p fois pour calculer v_n
    for i in range(n-p): # range(n-p) compte de 0 à n-p-1 ce qui fait bien n-p facteur
        v = v * q
    v_n = v
    print(f"la valeur du terme v({n}) est v({n}) = {v_n}\n")
    delta_temps = time.time() - temps_depart
    print(f"Temps d'exécution du calcul : {delta_temps} secondes.\n")
    return(v_n)
def u_geom_expl(v_p, p, n, q):
    # Pour une suite v, calcule v_n à partir de v_p et d'une d'une formule explicite
    # Paramètres d'entrée
    # v_p : valeur d'un premier terme connu v_p
    # p   : valeur du rang p correspondant
    # n   : valeur du rang n pour lequel on veut connaitre v_n = v(n)
    # q   : raison (multiplicative) de la suite
    # Paramètre de sortie
    # v_n : valeur v_n du terme calculé
    print("Suites géométriques")
    print("-------------------")
    print(f"On connait le terme v({p}) de la suite v, v({p}) = {v_p},  la raison de la suite est q = {q}\n")
    print(f"v(p) = v({p}) = {v_p}\n")
    print(f"n - p = {n} - {p} = {n - p}\n")
    print(f"q = {q}\n")
    print(f"Calcul de v_{n} à partir de la formule explicite v(n) = v(p) * q^(n - p):\n")
    temps_depart = time.time()
    v_n = v_p * (q ** (n - p))
    print(f"la valeur du terme v({n}) est v({n}) =  {v_p}  * {q} ^ {(n - p)} = {v_n}\n")
    delta_temps = time.time() - temps_depart
    print(f"Temps d'exécution du calcul : {delta_temps} secondes.\n")
    return(v_n)
# Détermination du rang n pour lequel on veut calculer le terme v(n)
print("calcul du terme v(n) d'une suite géométrique v connaissant un terme v(p) de la suite et sa raison q")
print("---------------------------------------------------------------------------------------------------\n")
print("Veuillez saisir le rang p du terme v(p) que vous connaissez :\n")
p = int(input("p = "))
print("")
print("Veuillez saisir la valeur du terme v(p) de rang p que vous connaissez :\n")
v_p = float(input("v_p = "))
print("")
print("Veuillez saisir la valeur q de la raison de la suite :\n")
q = float(input("q = "))
print("")
print("Veuillez saisir le rang n pour lequel vous voulez calculer v(n) :\n")
n = int(input("n = "))
print("\n")
print("Méthode 1, calcul de v(n) de façon réccurrente")
print("")
u_geom_rec(v_p ,p , n, q)
print("Méthode 2, calcul de v(n) de façon explicite")
print("")
u_geom_expl(v_p ,p , n, q)
print("Y a t-il une méthode plus rapide selon vous ?")
print("Réponse : si on fait les calculs à la main, il faut connaitre tous les termes de p à n pour la méthode par récurrence, la méthode explicite est donc plus rapide. Pour des temps de calculs courts avec peu d'itérations, le calcul en Python peut contredire cela.")
print("Des problèmes d'arrondis peuvent aussi se poser qui font que les valeurs obtenues par les deux méthodes ne sont pas tout à fait identiques, la gestion des produits est plus problématique que la gestion des sommes car les croissances ou décroissances obtenues sont exponentielles.")