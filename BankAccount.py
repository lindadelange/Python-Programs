class BankAccount(object):
  balance = 0.37
  
  def __init__(self, name): 
    self.name = name
  
  def __repr__(self):
    return "This account belongs to %s. The balance is $%.2f" % (self.name, self.balance)
  
  def show_balance(self):
    print("%s's balance is $%.2f" % (self.name, self.balance))
  
  def deposit(self, amount): 
    if amount <= 0:
      print("Invalid amount.")
      return
    else: 
      print("The balance is $%.2f" % (self.balance))
      self.balance += amount
      self.show_balance

  def withdrawal(self, amount):
    if amount > self.balance:
      print("Invalid amount.")
      return
    else:
      print("Amount withdrawn: $%.2f" % (amount))
      self.balance -= amount
      self.show_balance

my_account = BankAccount("Maxime")

print(my_account)
my_account.show_balance()
my_account.deposit(2000)
my_account.withdrawal(1000)
print(my_account)
