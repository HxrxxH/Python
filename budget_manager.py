class Budget:
    """
    A class to represent a budget account with functionalities for deposits, withdrawals, balance checks, and transaction history.

    Attributes:
        name (str): The name of the budget account.
        balance (float): The current balance of the account.
        transactions (list): A list of tuples representing transactions, where each tuple is (amount, note).
    """

    def __init__(self, name, balance):
        """
        Initializes a Budget object.

        Args:
            name (str): The name of the budget account.
            balance (float): The initial balance of the account.
        """

        self.name = name
        self.balance = balance
        self.transactions = []

    def deposit(self, amount, note=""):
        """
        Deposits a specified amount into the budget account.

        Args:
            amount (float): The amount to deposit.
            note (str, optional): A note to associate with the deposit transaction. Defaults to "".
        """

        if amount <= 0:
            print("Deposit amount must be positive.")
            return

        self.balance += amount
        self.transactions.append((amount, note))
        print(f"Deposited {amount:.2f}. New balance: {self.balance:.2f}")

    def withdraw(self, amount, note=""):
        """
        Withdraws a specified amount from the budget account, if sufficient funds are available.

        Args:
            amount (float): The amount to withdraw.
            note (str, optional): A note to associate with the withdrawal transaction. Defaults to "".

        Returns:
            bool: True if the withdrawal was successful, False otherwise.
        """

        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False

        if self.check_funds(amount):
            self.balance -= amount
            self.transactions.append((-amount, note))
            print(f"Withdrew {amount:.2f}. New balance: {self.balance:.2f}")
            return True
        else:
            print("Insufficient funds.")
            return False

    def get_balance(self):
        """
        Returns the current balance of the budget account.

        Returns:
            float: The current balance.
        """

        return self.balance

    def check_funds(self, amount):
        """
        Checks if the budget account has sufficient funds for a specified withdrawal amount.

        Args:
            amount (float): The amount to check.

        Returns:
            bool: True if there are sufficient funds, False otherwise.
        """

        return amount <= self.balance

    def get_transactions(self):
        """
        Returns a list of all transactions for the budget account.

        Returns:
            list: A list of tuples representing transactions, where each tuple is (amount, note).
        """

        return self.transactions

# Example usage
my_budget = Budget("My Budget", 1000.00)
my_budget.deposit(500.00, "Salary")
my_budget.withdraw(200.00, "Groceries")
my_budget.deposit(100.00, "Interest earned")
print(f"Current balance: {my_budget.get_balance():.2f}")

transactions = my_budget.get_transactions()
for transaction in transactions:
    amount, note = transaction
    if amount > 0:
        print(f"Deposited {amount:.2f} - {note}")
    else:
        print(f"Withdrew {-amount:.2f} - {note}")
