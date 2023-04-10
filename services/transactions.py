"""
@author: Venkata Mulam
@Date: 03/20/2023
"""
from settings.settings import acc


def show_options():
    """
    Function to show all options
    :return: selected choice
    """
    opts = """
    Welcome To CareerSoft Bank
    1. Deposit
    2. Withdraw
    3. Balance
    4. Mini Statement
    5. Exit
    """
    print(opts)
    try:
        ch = int(input("Please select option from above: "))
    except ValueError:
        print("Invalid choice.. Please enter only integers.")


    return ch


def deposit():
    amt = int(input("Enter the amount to deposit: "))
    acc["Balance"] += amt
    # acc["Balance"] = acc["Balance"] + amt
    print("Transaction completed successfully")
    print("Your New Balance is: {}".format(acc["Balance"]))
    # show_options()


def withdraw():
    print("Inside withdraw()")
    # show_options()


def balance():
    print("Your New Balance is: {}".format(acc["Balance"]))
    # show_options()


def mini_statement():
    print("Inside mini_statement()")
    # show_options()

ch_func_mapping = {1: deposit,
                   2: withdraw,
                   3: balance,
                   4: mini_statement,
                   5: exit}