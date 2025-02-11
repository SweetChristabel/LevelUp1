# WRITE YOUR SOLUTION HERE:
class BankAccount:
    def __init__(self, owner: str, account_number: str, balance: float):
        self.__owner = owner
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount: float):
        if amount >= 0:
            self.__balance += amount
            self.__service_charge()
        else:
            raise ValueError("Amount cannot be negative")

    def withdraw(self, amount: float):
        if amount <= self.__balance:
            self.__balance -= amount
            self.__service_charge()
        else:
            raise ValueError("Not enough funds")

    @property
    def balance(self):
        return self.__balance
    
    def __service_charge(self):
        charge = self.__balance * 0.01
        self.__balance -= charge


if __name__ == "__main__":
    account = BankAccount("Randy Riches", "12345-6789", 1000)
    account.withdraw(100)
    print(account.balance)
    account.deposit(100)
    print(account.balance)