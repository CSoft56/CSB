"""
Main for execution of CSB
"""
acc = {
    "AccNo": "A550",
    "Balance": 50000,
    "Name": "Mahitha",
    "Transactions": [{"type": "debit", "amount": 50000, "date": "2023-03-13"}]
}


def deposit():
    amt = int(input("Enter the amount to deposit: "))
    acc["Balance"] += amt
    # acc["Balance"] = acc["Balance"] + amt
    print("Transaction completed successfully")
    print("Your New Balance is: {}".format(acc["Balance"]))
    show_options()


def withdraw():
    amt = int(input("Enter the amount to withdraw: "))
    acc["withdraw"] = amt
    # acc["withdraw"] = acc["withdraw"] amt
    print("Transaction completed successfully")
    print("Your New Balance is: {}".format(acc["balance"]))
    show_options()


def balance():
    amt = int(input("Enter the balance amount: "))
    acc["Balance"] += amt
    # acc["Balance"] = acc["Balance"] + amt
    print("Inside Balance amount ")
    print("Your New Balance is: {}".format(acc["Balance"]))
    show_options()


def mini_statement():
    amt = int(input("Enter the mini_statement: "))
    acc["Balance"] += amt
    # acc["Balance"] = acc["Balance"] + amt
    print("Inside mini_statement ")
    print("Your New Balance is: {}".format(acc["Balance"]))
    show_options()



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
