#!/usr/bin/python3.9
# Licence GPL3 copyright (c) 2022 Stéphane Lassalvy
def my_SommeTermesArith(u_p, p, u_n, n):
  # Somme des termes d'une suite arithmétique u
  # Paramètres
  # u_p : premier terme de la somme
  # p   : rang du premier terme de la somme
  # u_n : dernier terme de la somme
  # n   : rang du dernier terme de la somme
  #
  # Sortie
  # sommeTermes : somme des termes consécutifs de la suite arithmétique correspondante
  nombreTermes = n - p + 1
  premierTerme = u_p
  dernierTerme = u_n
  print(f"S = u({p}) + ... + u({n})")
  print("")
  print(f"Il y a {nombreTermes} termes")
  print("")
  print(f"Premier terme : u({p}) = {u_p}")
  print("")
  print(f"Dernier terme : u({n}) = {u_n}")
  print("")
  print("S = (nombre de termes) x (premier terme + dernier terme) / 2")
  sommeTermes = nombreTermes * (premierTerme + dernierTerme) / 2
  print(f"S = {sommeTermes}")
  return sommeTermes
# Détermination du rang n pour lequel on veut calculer le terme u(n)
print("calcul de la somme des termes consécutifs d'une suite arithmétique")
print("------------------------------------------------------------------")
print("S = u(p) + u(p+1) + ... + u(n)")
print("")
print("Veuillez saisir la valeur du premier terme u(p) de la somme S :")
u_p = float(input("u(p) = "))
print("")
print("Veuillez saisir le rang p du terme u(p) :")
p = int(input("p = "))
print("")
print("Veuillez saisir la valeur du dernier terme u(n) de la somme S :")
u_n = float(input("u(n) = "))
print("")
print("Veuillez saisir le rang n du terme u(n) :")
n = int(input("n = "))
print("")
print("Calcul de la somme  S")
print("---------------------")
print("")
my_SommeTermesArith(u_p, p, u_n, n)