import datetime

from Settings import show_options
from transaction import *
from datetime import date
today = datetime.datetime.today()
"""
Main for execution of CSB
"""
acc = {
    "AccNo": "A100",
    "Balance": 20000,
    "Name": "Jagdesh",
    "Transactions": [{"type": "debit", "amount": 20000, "date": today.strftime("%Y-%m-%d %H-%M-%S")}]
}


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