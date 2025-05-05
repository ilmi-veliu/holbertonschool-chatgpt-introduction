#!/usr/bin/python3

# Fonction qui affiche le plateau du jeu
# @board: liste 2D représentant le plateau de jeu
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Fonction qui vérifie s’il y a un gagnant
# @board: liste 2D représentant le plateau de jeu
# Return: True si un joueur a gagné, sinon False
def check_winner(board):
    # Vérification des lignes
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Vérification des colonnes
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Vérification des diagonales
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

# Fonction principale qui lance une partie de morpion
def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    # Boucle de jeu
    while not check_winner(board):
        print_board(board)

        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))

            # Vérifie que les coordonnées sont valides
            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Invalid coordinates! Try values 0, 1, or 2.")
                continue

            # Vérifie que la case est vide
            if board[row][col] != " ":
                print("That spot is already taken! Try again.")
                continue

            # Placement du symbole
            board[row][col] = player
            player = "O" if player == "X" else "X"

        except ValueError:
            print("Invalid input! Please enter numbers only.")

    print_board(board)
    print("Player " + ("O" if player == "X" else "X") + " wins!")

# Point d'entrée du programme
tic_tac_toe()
