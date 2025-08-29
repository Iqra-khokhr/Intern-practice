# task3.py

PIN = "1234"
balance = 0.0

def menu():
    global balance
    while True:
        print("\n--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        ch = input("Enter choice: ")

        if ch == "1":
            print(f" Balance: {balance:.2f}")
        elif ch == "2":
            amt = float(input("Enter amount to deposit: "))
            balance += amt
            print(f" Deposited! New Balance: {balance:.2f}")
        elif ch == "3":
            amt = float(input("Enter amount to withdraw: "))
            if amt <= balance:
                balance -= amt
                print(f" Withdrawn! New Balance: {balance:.2f}")
            else:
                print(" Insufficient funds.")
        elif ch == "4":
            print(" Thank you! Exiting...")
            break
        else:
            print(" Invalid choice")

# PIN check
if input("Enter ATM PIN: ") == PIN:
    print(" Correct PIN. Welcome!")
    menu()
else:
    print(" Wrong PIN. Access Denied.")
