
#Main for execution of CSB
acc = {
    "AccNo": "27021999",
    "Balance": 20000,
    "Name": "Harsha",
    "Transactions": [{"type": "debit", "amount": 20000, "date": "2023-03-18"}]
}


def deposit():
    amt = int(input("Enter the amount to deposit: "))
    acc["Balance"] += amt
    # acc["Balance"] = acc["Balance"] + amt
    print("Transaction completed successfully")
    print("Your New Balance is: {}".format(acc["Balance"]))



def withdraw():
    amt = int(input("Enter the amount to withdraw: "))
    acc["Balance"] -= amt
    # acc["Balance"] = acc["Balance"] - amt
    print("Transaction completed successfully")
    print("Your New Balance is: {}".format(acc["Balance"]))




def balance():
    print(acc["Balance"])



def mini_statement():
    print(acc)



def show_options():
    opts = """
    Welcome To CareerSoft Bank
    1. Deposit
    2. Withdraw
    3. Balance
    4. Mini Statement
    5. Exit
    """
    print(opts)
    a = input("Please select option from above: ")

    return a



func_mapping = {"1": deposit, "2": withdraw, "3": balance, "4": mini_statement, "5": exit}
while True:
    b = show_options()

    if b in func_mapping:
        if b == "5":
            print("Logged out Successfully")
            print("Thank you using CareerSoft Banking Application.")
        func_mapping[b]()
    else:
        print("Invalid Choice, Please enter Valid choice from 1-5")

