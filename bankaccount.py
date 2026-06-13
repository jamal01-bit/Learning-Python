class BankAccount:
  def __init__(self, fname, sname, account_id, account_type, pin, balance):
    self.fname = fname
    self.sname = sname
    self.account_id = account_id
    self.account_type = account_type
    self.pin = pin
    self.balance = balance
  def deposit(self, amount):
    self.balance += amount
    return self.balance

  def withdraw(self, amount):
    self.balance -= amount
    return self.balance
  
  def display_balance(self):
    print(self.balance)

jamal = BankAccount('jamal', 'mohamed', 1000, 'student', 1234,500)
deposit = int(input('How much would you like to deposit: '))
withdraw = int(input('How much would you like to withdraw: '))
jamal.deposit(deposit)
jamal.withdraw(withdraw)
jamal.display_balance()

