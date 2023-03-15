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
    acc["Balance"] += amt
    # acc["Balance"] = acc["Balance"] + amt
    print("Transaction completed successfully")
    print("Your New Balance is: {}".format(acc["Balance"]))
    show_options()


def withdraw():
    print("Inside withdraw()")
    show_options()


def balance():
    print("Inside balance()")
    show_options()


def mini_statement():
    print("Inside mini_statement()")
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
