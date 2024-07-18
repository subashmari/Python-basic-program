class Bank:
    def __init__(self, pin, name, location):
        self.pin = pin
        self.name = name
        self.location = location
        self.balance = 25000

    def validate_pin(self, entered_pin):
        if entered_pin == self.pin:
            return True
        return False

    def check_balance(self):
        print(f"Your current balance is {self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} has been credited to your account. Your current balance is {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"{amount} has been debited from your account. Your current balance is {self.balance}")
atm = Bank(1234, "Subash M", "Bengalore")
print("Your card number is: XXXX XXXX XXXX 1234 ")
entered_pin = int(input("Enter your PIN: "))
if atm.validate_pin(entered_pin):
    print("PIN validated successfully.")
    print(f"Welcome to the ATM, {atm.name}. You are using the ATM located in {atm.location}.")
    while True:
        print("1. Check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        option = int(input("Enter your choice: "))
        if option == 1:
            atm.check_balance()
        elif option == 2:
            amount = int(input("Enter the amount to deposit: "))
            atm.deposit(amount)
        elif option == 3:
            amount = int(input("Enter the amount to withdraw: "))
            atm.withdraw(amount)
        elif option == 4:
            print("Thank you for using the ATM. Have a great day!")
            break
        else:
            print("Invalid option. Please try again.")
else:
    print("Invalid PIN. Please try again.")
