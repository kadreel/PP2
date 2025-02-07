class BankAccount:
    def __init__(self, owner, balance=0):                           #Defaults balance to 0 if undefined, sets owner
        self.owner = owner
        self.balance = balance
        print(f"Welcome, {owner}. Your current balance is: ${balance}")
    
    def deposit(self, amount):
        if amount > 0:                                              #Checks if negative, and adds if is not
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:                                                       #Refuses if negative
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if amount <= self.balance:                                  #Checks if it's possible to withdraw, and does if it is
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:                                                       #Refuses if account balance is too low
            print(f"Insufficient funds for withdrawal. Current balance: ${self.balance}")

# EXAMPLE:

account = BankAccount("John Doe", 100)                              #John Doe starts with $100 on his account
account.deposit(50)                                                 #John Doe deposits $50 on his account. Output: Deposited $50. New balance: $150
account.withdraw(30)                                                #John Doe regrets parting with that $30 and withdraws them. Output: Withdrew $30. New balance: $120
account.withdraw(200)                                               #John Doe sucks at math. Output: Insufficient funds for withdrawal. Current balance: $120
account.deposit(-10)                                                #John Doe really sucks at math. Don't be like John Doe. Output: Deposit amount must be positive

account = BankAccount("Jane Doe")                                   #Jane Doe forgets to do an initial deposit and starts with $0 on her balance