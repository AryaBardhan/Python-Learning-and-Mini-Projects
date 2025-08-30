def show_balance(balance):
    print("******************")
    print(f"Your balance id ${balance:.2f}")
    print("*******************")

    
def deposit():
    print("********************")
    amount = float(input("Enter an amount to be deposited: "))
    print("********************")
    if amount < 0:
        print("********************")
        print("That's not a valid amount")
        print("********************")
        return 0
    else:
        return amount
    
def withdraw(balance):
    print("********************")
    amount = input("Enter amount to be withdrawn: ")
    print("********************")

    if amount > balance:
        print("********************")
        print("Insufficient Funds")
        print("********************")
        return 0
    elif amount < 0:
        print("********************")
        print("Amount must be Greater than 0")
        print("********************")
        return 0
    else:
        return amount


def main():
    balance = 0 
    is_running = True

    while is_running:
        print("********************")
        print("Banking Program")
        
        print("********************")
        print("1. Show Balance")
        
        print("********************")
        print("2. Deposit")
        
        print("********************")
        print("3. Withdraw")
        
        print("********************")
        print("4. Exit")
        
        print("********************")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance += withdraw(balance)
        elif choice  == '4':
            is_running = False
        else:
            print("That is not a valid choice")

    print("Thank You! have a nice day")
    
if __name__ == '__main__':
    main()
