"""
@author: mahitha
@Date: 03/30/2023
"""
from setting import acc


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

def deposit():
    amt = int(input("Enter the amount to deposit: "))
    acc["Balance"] += amt
    # acc["Balance"] = acc["Balance"] + amt
    print("Transaction completed successfully")
    print("Your New Balance is: {}".format(acc["Balance"]))
    show_options()



def withdraw():
    amt = int(input("Enter the amount to withdraw: "))
    acc["Balance"] = amt - acc["Balance"]
    print("Transaction completed successfully")
    print("Your New Balance is: {}".format(acc["Balance"]))
    show_options()

def balance():
    print("Your New Balance is: {}".format(acc["Balance"]))
    show_options()


def mini_statement():
    print("Your last 10 transactions is: {}".format(acc["Transactions"]))
    show_options()

ch_func_mapping = {"1": deposit, "2": withdraw, "3": balance, "4": mini_statement, "5": exit}
