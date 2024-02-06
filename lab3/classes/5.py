class Bank_Account:
   def __init__(self,owner,balance):
      (self.owner)  = owner
      self.balance = balance

   def deposit(self,amount):
      if amount > 0:
         self.balance += amount
         print(f"Mister {self.owner} the operation was successful . Your current balanca : {self.balance}")
      else :
         print(f"Mister {self.owner} you cannot send negative deposit!!!")
   def withdraw(self,amount):
      if  amount > 0:
         if amount < self.balance:
            self.balance -= int(amount)
            print(f"Mister {self.owner} the operation was successful . Your current balance : {self.balance}") 
         else :
            print(f"Mister {self.owner} your current balance is : {self.balance} and you cannot take {amount} money!!! ")
      else :
         print(f"Mister {self.owner} you cannot get negative withdraw!!!")

name = str(input("Your name please : "))
balance = int(input("Your balance please : "))
deposit1 = int(input(f"Mister {name} enter your deposit please : "))
withdraw1 = int(input(f"Mister {name} enter your withdraw please : "))
Account = Bank_Account(name,balance)
Account.deposit(deposit1)
Account.withdraw(withdraw1)