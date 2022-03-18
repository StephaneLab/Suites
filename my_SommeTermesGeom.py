#!/usr/bin/python3.9
# Licence GPL3 copyright (c) 2022 Stéphane Lassalvy
def my_SommeTermesGeom(v_p, p, n, q):
  # Somme des termes d'une suite géométrique v
  # Paramètres
  # v_p : premier terme de la somme
  # p   : rang du premier terme de la somme
  # n   : rang du dernier terme de la somme
  # q   : raison de la suite géométrique v
  #
  # Sortie
  # sommeTermes : somme des termes consécutifs de la suite géométrique correspondante
  nombreTermes = n - p + 1
  premierTerme = v_p
  raison       = q
  print(f"S = v({p}) + ... + v({n})")
  print("")
  print(f"Il y a {nombreTermes} termes")
  print("")
  print(f"Premier terme : v({p}) = {v_p}")
  print("")
  print(f"raison : q = {q}")
  print("")
  print("S = (premier terme) * (1 - raison ^ (nombre de termes)) / (1 - raison)")
  sommeTermes = premierTerme * (1 - raison ** nombreTermes) / (1 - raison)
  print(f"S = {sommeTermes}")
  return sommeTermes
# Détermination du rang n pour lequel on veut calculer le terme u(n)
print("calcul de la somme des termes consécutifs d'une suite géométrique")
print("-----------------------------------------------------------------")
print("S = v(p) + v(p+1) + ... + v(n)")
print("")
print("Veuillez saisir la valeur du premier terme v(p) de la somme S :")
v_p = float(input("v(p) = "))
print("")
print("Veuillez saisir le rang p du terme u(p) :")
p = int(input("p = "))
print("")
print("Veuillez saisir le rang n du dernier terme v(n) de la somme S:")
n = int(input("n = "))
print("")
print("Veuillez saisir la raison q de la suite géométrique v :")
q = float(input("q = "))
print("")
print("Calcul de la somme  S")
print("---------------------")
print("")
my_SommeTermesGeom(v_p, p, n, q)