balance = 75991.75
pin = "7683"
transactions = []
#1.           Check pin
def checkpIIin():
    enteredpin = input("Enter your SECRET PIN: ")
    if enteredpin == pin:
        print(" SECRET PIN is correct.")
        return True
    else:
        print(" ENTERED PIN  is wrong .")
        return False
#2.Check balance
def checkbalancEEe():
    print("Your current balance in Rs is .", balance)
#3.    withdrawnbalance
def withdrawmonEEey():
    global balance
    amount = int(input("Enter the amount to withdraw: "))
    if amount <= 0:
        print("Enter amount greater 0 .")
    elif amount > balance:
        print("your balance is not sufficient.")
    elif amount % 100 != 0:
        print("entered amount should be multiple of 100.")
    else:
        balance = balance - amount
        transactions.append("Withdraw: Rs. " + str(amount))
        print(" collect your cash.")
        print("Remaining balance is Rs.", balance)
#4. Deposit money
def depositmonEEey():
    global balance
    amount = int(input("Enter the  amount to deposit: "))
    if amount <= 0:
        print("Entered amount should be greater than 0 .")
    else:
        balance = balance + amount
        transactions.append("Deposit: Rs. " + str(amount))
        print("Your Money has been deposited successfully.")
        print("New balance in Rs is.", balance)
        #4. change pin
def changepIIin():
    global pin
    oldpin = input("Enter your old PIN: ")
    if oldpin == pin:
        newpin = input("Enter your new PIN: ")
        if len(newpin) == 4 and newpin.isdigit():
            pin = newpin
            print("PIN was changed successfully.")
        else:
            print("PIN should not be more than 4 digits.")
    else:
        print("Old PIN is incorrect.")
        #5. Mnin statement
def mini_stateEEment():
    print("\n MINI STATEMENT")
    if len(transactions) == 0:
        print("No transactions available to show.")
    else:
        for transaction in transactions:
            print(transaction)
    print("Current Balance: Rs.", balance)
    #6.Fast cash
def fast_caAAsh():
    global balance
    print("\nFAST CASH ")
    print("1. Rs. 500")
    print("2. Rs. 1000")
    print("3. Rs. 2000")
    print("4. Rs. 5000")
    amnt = input("Choose amount: ")
    if amnt == "1":
        amount = 500
    elif amnt == "2":
        amount = 1000
    elif amnt == "3":
        amount = 2000
    elif amnt == "4":
        amount = 5000
    else:
        print("entered choice is Invalid .")
        return
    if amount > balance:
        print("enterd amount is more than your current balance.")
    else:
        balance = balance - amount
        transactions.append("Fast Cash: Rs. " + str(amount))
        print("Please collect your cash.")
        print("Remaining balance is Rs.", balance)
        #7.Amount
def atm():
    print("        WELCOME TO  VIT ATM :)")
    if checkpIIin():
        while True:
            print("\n----- ATM.MENU -----")
            print("1. Check Balance")
            print("2. Withdraw Money")
            print("3. Deposit Money")
            print("4. Fast Cash")
            print("5. Mini Statement")
            print("6. Change PIN")
            print("7. Exit")
            selection = input("Enter your choice: ")
            if selection == "1":
                checkbalancEEe()
            elif selection == "2":
                withdrawmonEEey()
            elif selection == "3":
                depositmonEEey()
            elif selection == "4":
                fast_caAAsh()
            elif selection == "5":
                mini_stateEEment()
            elif selection == "6":
                changepIIin()
            elif selection == "7":
                print("Thank you for using the ATM :).")
                print("Have a nice day")
                break
            else:
                print("Invalid choice. try again. :(")
atm()