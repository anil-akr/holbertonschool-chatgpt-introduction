#!/usr/bin/python3
"""
Simple Checkbook CLI

This program lets a user manage a checkbook balance from the terminal.
Supported actions:
- deposit  : add money to the balance
- withdraw : remove money from the balance (if enough funds)
- balance  : display the current balance
- exit     : quit the program

Main improvement:
- Robust input handling so the program does not crash when the user enters
  invalid (non-numeric) amounts.
"""

class Checkbook:
    """A minimal checkbook that tracks a balance and supports deposits/withdrawals."""

    def __init__(self):
        """Initialize the checkbook with a zero balance."""
        self.balance = 0.0

    def deposit(self, amount):
        """
        Add money to the balance.

        Args:
            amount (float): Amount to deposit. Must be > 0.

        Returns:
            None
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraw money from the balance if sufficient funds exist.

        Args:
            amount (float): Amount to withdraw. Must be > 0.

        Returns:
            None
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Print the current balance.

        Returns:
            None
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def prompt_amount(prompt):
    """
    Prompt the user for a money amount until a valid positive number is entered.

    This prevents crashes when the user types non-numeric values (e.g., 'test').

    Args:
        prompt (str): The prompt text to show the user.

    Returns:
        float: A valid amount strictly greater than 0.
    """
    while True:
        raw = input(prompt).strip()
        try:
            amount = float(raw)
            if amount <= 0:
                print("Please enter a positive amount.")
                continue
            return amount
        except ValueError:
            print("Invalid amount. Please enter a number (e.g., 10 or 10.50).")


def main():
    """Run the interactive command loop for the checkbook."""
    cb = Checkbook()

    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()

        if action == "exit":
            break

        elif action == "deposit":
            amount = prompt_amount("Enter the amount to deposit: $")
            cb.deposit(amount)

        elif action == "withdraw":
            amount = prompt_amount("Enter the amount to withdraw: $")
            cb.withdraw(amount)

        elif action == "balance":
            cb.get_balance()

        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
