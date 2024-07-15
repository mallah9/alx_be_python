import sys
from bank_account import BankAccount

def main():
  account = BankAccount(100)  # Example starting balance

  if len(sys.argv) < 2:
    print("Usage: python main.py <command>:<amount>")
    print("Commands: deposit, withdraw, display")
    sys.exit(1)

  command, *params = sys.argv[1].split(':')
  amount = float(params[0]) if params else None

  if command == "deposit":
    if account.deposit(amount):  # Check for successful deposit
      print(f"Deposited: ${amount:.2f}")
    else:
      print("Invalid deposit amount.")
  elif command == "withdraw":
    if account.withdraw(amount):  # Check for successful withdrawal
      print(f"Withdrew: ${amount:.2f}")
    else:
      print("Insufficient funds.")
  elif command == "display":
    account.display_balance()
  else:
    print("Invalid command.")

if __name__ == "__main__":
  main()
