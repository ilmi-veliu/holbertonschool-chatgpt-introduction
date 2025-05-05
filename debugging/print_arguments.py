#!/usr/bin/python3
import sys

# Script qui affiche tous les arguments passés en ligne de commande
# (excepté le nom du fichier lui-même)

# Boucle à travers tous les arguments à partir du 1er (index 1)
# (index 0 contient le nom du script lui-même)
for i in range(1, len(sys.argv)):
    print(sys.argv[i])
