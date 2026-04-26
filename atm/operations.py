from .statement import Statement

class ATM:

    def __init__(self):
        self.balance = 10000   
        self.stmt = Statement()

    def check_balance(self):
        print("\n" + "="*38)
        print(f"  💰 Your Balance : Rs. {self.balance}")
        print("="*38)

    def deposit(self):
        print("\n  💵 --- DEPOSIT MONEY ---")
        amt = input("  Enter amount to deposit: Rs. ")

       
        if amt.isdigit() == False:
            print("  ❌ Invalid input! Please enter a number.")
            return

        amt = int(amt)

        if amt <= 0:
            print("  ❌ Amount should be more than 0!")
        else:
            self.balance = self.balance + amt
            self.stmt.add_record("Deposit", amt, self.balance)
            print(f"  ✅ Rs. {amt} deposited successfully!")
            print(f"  💰 Updated Balance : Rs. {self.balance}")

    def withdraw(self):
        print("\n  💸 --- WITHDRAW MONEY ---")
        amt = input("  Enter amount to withdraw: Rs. ")

       
        if amt.isdigit() == False:
            print("  ❌ Invalid input! Please enter a number.")
            return

        amt = int(amt)

        if amt <= 0:
            print("  ❌ Amount should be more than 0!")
        elif amt > self.balance:
            print(f"  ❌ Insufficient balance! Available: Rs. {self.balance}")
        else:
            self.balance = self.balance - amt
            self.stmt.add_record("Withdrawal", amt, self.balance)
            print(f"  ✅ Rs. {amt} withdrawn successfully!")
            print(f"  💰 Remaining Balance : Rs. {self.balance}")

    def show_statement(self):
        self.stmt.show()
