class BankAccount:
  def __init__(self, initial_balance=0.0):
    self.__balance = initial_balance  # Encapsulate balance attribute

  def deposit(self, amount):
    if amount > 0:  # Ensure positive deposit amount
      self.__balance += amount
      return True  # Indicate successful deposit
    else:
      return False  # Indicate invalid deposit amount

  def withdraw(self, amount):
    if amount > 0 and self.__balance >= amount:  # Ensure positive and sufficient amount
      self.__balance -= amount
      return True  # Indicate successful withdrawal
    else:
      return False  # Indicate invalid or insufficient withdrawal

  def display_balance(self):
    print(f"Current Balance: ${self.__balance:.2f}")