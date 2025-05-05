#!/usr/bin/python3
import sys

# Fonction qui calcule la factorielle d’un nombre
# @n: entier dont on veut la factorielle
# Return: la factorielle de n
def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

# Appel de la fonction avec un argument passé en ligne de commande
f = factorial(int(sys.argv[1]))
print(f)
