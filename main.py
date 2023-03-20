
"""
Main for execution of CSB
"""
acc = {
    "AccNo": "A100",
    "Balance": 20000,
    "Name": "Venkat",
    "Transactions": [{"type": "debit", "amount": 20000, "date": "2023-03-12"}]
}


def deposit():
    amt = int(input("Enter the amount to deposit: "))
    updated = acc["Balance"] + amt
    acc["Balance"] = updated
    print("Transaction completed successfully")
    acc["Transactions"].append({'type': 'debit', 'amount': updated, 'date': '2023-03-12'})
    print("Your New Balance is: {}".format(acc["Transactions"]))


def withdraw():
    amt_1 = int(input("Enter the amount to withdraw: "))
    if acc["Balance"] <= amt_1:
        print("Error, Insufficient Balance")
    else:
        updated = acc["Balance"] - amt_1
        acc["Balance"] = updated
        acc["Transactions"].append({'type': 'debit', 'amount': updated, 'date': '2023-03-12'})
        print("Transaction completed successfully")
        print("Your New Balance is: {}".format(acc["Transactions"]))



def balance():
    print("Your New Balance is: {}".format(acc["Transactions"][-1]))


def mini_statement():

    print("Mini Statement is: {}".format(acc["Transactions"]))


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
    ch = input("Please select option from above: ")

    return ch


if __name__ == '__main__':
    ch_func_mapping = {"1": deposit, "2": withdraw, "3": balance, "4": mini_statement, "5": exit}
    while True:
        ch = show_options()

        if ch in ch_func_mapping:
            if ch == "5":
                print("Logged out Successfully")
                print("Thank you using CareerSoft Banking Application.")
            ch_func_mapping[ch]()
        else:
            print("Invalid Choice, Please enter Valid choice from 1-5")