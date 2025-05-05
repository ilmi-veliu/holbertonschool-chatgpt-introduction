#!/usr/bin/python3

# Classe qui gère un carnet de chèques
class Checkbook:
    def __init__(self):
        self.balance = 0.0

    # Fonction pour déposer de l'argent
    # @amount: montant à déposer
    def deposit(self, amount):
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    # Fonction pour retirer de l'argent
    # @amount: montant à retirer
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    # Fonction pour afficher le solde
    def get_balance(self):
        print("Current Balance: ${:.2f}".format(self.balance))

# Fonction principale
def main():
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                if amount <= 0:
                    print("Amount must be greater than zero.")
                    continue
                cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif action.lower() == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                if amount <= 0:
                    print("Amount must be greater than zero.")
                    continue
                cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

# Point d'entrée du programme
if __name__ == "__main__":
    main()
