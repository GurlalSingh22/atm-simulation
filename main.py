
from atm import ATM

def show_menu():
    print("\n" + "="*38)
    print("       🏧  WELCOME TO PY-BANK ATM")
    print("="*38)
    print("  1. 💰  Check Balance")
    print("  2. 💵  Deposit Money")
    print("  3. 💸  Withdraw Money")
    print("  4. 🧾  Mini Statement")
    print("  5. 🚪  Exit")
    print("="*38)

def main():
    print("\n  🏧 Welcome to PY-BANK!")
    print("  Please enter your PIN to continue.\n")

    correct_pin = "1234"
    attempts = 0

    while attempts < 3:
        pin = input("  🔐 Enter PIN: ")

        if pin == correct_pin:
            print("  ✅ PIN correct! Access granted.\n")
            break
        else:
            attempts = attempts + 1
            remaining = 3 - attempts
            if remaining > 0:
                print(f"  ❌ Wrong PIN! {remaining} attempt(s) remaining.")
            else:
                print("  🔒 Too many wrong attempts. Card blocked!")
                return

    myatm = ATM()

    while True:
        show_menu()
        ch = input("  Enter choice (1-5): ")

        if ch == "1":
            myatm.check_balance()
        elif ch == "2":
            myatm.deposit()
        elif ch == "3":
            myatm.withdraw()
        elif ch == "4":
            myatm.show_statement()
        elif ch == "5":
            print("\n  👋 Thank you for using PY-BANK ATM. Goodbye!\n")
            break
        else:
            print("  ❌ Invalid choice! Please enter 1 to 5.")

if __name__ == "__main__":
    main()
