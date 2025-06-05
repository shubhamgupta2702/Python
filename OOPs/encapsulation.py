class BankAccount:
  def __init__(self,account_number,balance):
    self.account_number = account_number
    self.__balance = balance
    
  def deposit(self,amount):
    self.__balance += amount
    print(f'Desposited {amount}. New Amount ={self.__balance}')
    
  def getBalance(self):
      return self.__balance
    
account = BankAccount("12455", 2000)

account.deposit(4000)
print(account.getBalance())

#print(account.__balance) #error -- controlled access