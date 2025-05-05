#!/usr/bin/python3
import sys

# Fonction qui calcule la factorielle d’un nombre de façon récursive
# @n: entier (>= 0) dont on veut calculer la factorielle
# Return: la factorielle de n (n!)
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Appel de la fonction factorial avec une valeur donnée en ligne de commande
# Le résultat est ensuite affiché
f = factorial(int(sys.argv[1]))
print(f)
