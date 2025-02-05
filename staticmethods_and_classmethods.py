class BankAccount:
    interest_rate = 0.03  # Default interest rate for all accounts

    def __init__(self, account_type, balance):
        self.account_type = account_type
        self.balance = balance

    @staticmethod
    def is_valid_transaction(amount):
        """Check if the transaction amount is valid."""
        return amount > 0

    @classmethod
    def create_savings_account(cls, initial_deposit):
        """Factory method to create a savings account."""
        if not cls.is_valid_transaction(initial_deposit):
            raise ValueError("Initial deposit must be positive.")
        return cls("Savings", initial_deposit)

    @classmethod
    def create_business_account(cls, initial_deposit):
        """Factory method to create a business account with a higher interest rate."""
        if not cls.is_valid_transaction(initial_deposit):
            raise ValueError("Initial deposit must be positive.")
        account = cls("Business", initial_deposit)
        account.interest_rate = 0.05  # Business accounts have a higher interest rate
        return account

# Example usage
try:
    # Utility function
    print(BankAccount.is_valid_transaction(-50))  # Output: False
    print(BankAccount.is_valid_transaction(100))  # Output: True
    b = BankAccount("commercial", 100)
    print(b.is_valid_transaction(100))

    # Creating accounts using class methods
    savings = BankAccount.create_savings_account(1000)
    business = BankAccount.create_business_account(5000)

    print(f"Savings Account - Balance: ${savings.balance}, Interest Rate: {savings.interest_rate}")
    # Output: Savings Account - Balance: $1000, Interest Rate: 0.03

    print(f"Business Account - Balance: ${business.balance}, Interest Rate: {business.interest_rate}")
    # Output: Business Account - Balance: $5000, Interest Rate: 0.05

except ValueError as e:
    print(e)
