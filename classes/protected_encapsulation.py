# Encapsulation is used to restrict the direct access to class properties and methods. Protected attibutes and methods just indicate for other programmers that the attributes and methods should not be modified out of the class. Private attributes and methods don't allow modification and access out of the class (but is possible). Protected we type '_' before the name of the attribute or method, and Private we type '__' before them.
class BankAccount:
    def __init__(self):
        self._balance=0
    
    def deposit(self, amount):
        if 0<amount:
            self._balance+=amount
            print(f'Amount of {amount} deposited successfully, now your currently balance is {self._balance}')
        else:
            print('This is an invalid amount, try it again.')
    
    def withdraw(self, amount):
        if 0<amount<=self._balance:
            self._balance-=amount
            print(f'Withdrawal of {amount} successful! Now your currently balance is {self._balance}')
        else:
            print('Invalid amount! Or you do not have enough balance')

    def see_balance(self):
        print(f'Your currently balance is {self._balance}' )
    
# Here is the testing part

account= BankAccount()
account.deposit(1000)
account.withdraw(500)
account.see_balance()
account.withdraw(1001)


