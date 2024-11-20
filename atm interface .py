class ATM:
    def __init__(self, user_pin, user_balance):
        self.user_pin = user_pin
        self.user_balance = user_balance

    def authenticate_user(self):
        attempts = 3
        while attempts > 0:
            entered_pin = input("Enter your 4-digit PIN: ")
            if entered_pin == self.user_pin:
                print("\nAuthentication successful!")
                return True
            else:
                attempts -= 1
                print(f"Incorrect PIN. You have {attempts} attempts left.")
        print("\nToo many incorrect attempts. Exiting...")
        return False

    def display_menu(self):
        print("\n--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

    def check_balance(self):
        print(f"\nYour current balance is: ₹{self.user_balance}")

    def deposit_money(self):
        try:
            amount = float(input("Enter the amount to deposit: ₹"))
            if amount > 0:
                self.user_balance += amount
                print(f"₹{amount} deposited successfully! New balance: ₹{self.user_balance}")
            else:
                print("Enter a valid amount greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    def withdraw_money(self):
        try:
            amount = float(input("Enter the amount to withdraw: ₹"))
            if amount > 0:
                if amount <= self.user_balance:
                    self.user_balance -= amount
                    print(f"₹{amount} withdrawn successfully! Remaining balance: ₹{self.user_balance}")
                else:
                    print("Insufficient balance.")
            else:
                print("Enter a valid amount greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    def run(self):
        if not self.authenticate_user():
            return
        while True:
            self.display_menu()
            choice = input("\nEnter your choice (1-4): ")
            if choice == "1":
                self.check_balance()
            elif choice == "2":
                self.deposit_money()
            elif choice == "3":
                self.withdraw_money()
            elif choice == "4":
                print("\nThank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


# Initialize the ATM with a sample PIN and balance
atm = ATM(user_pin="1234", user_balance=10000.0)
atm.run()
