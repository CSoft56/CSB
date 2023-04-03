import datetime

from settings import show_options
from transac import *
# from Transaction import CSB
from datetime import date


today = datetime.datetime.today()
"""
Main for execution of CSB
"""
acc = {
    "AccNo": "A100",
    "Balance": 20000,
    "Name": "Kapil",
    "Transactions": [{"type": "debit", "amount": 20000, "date": today.strftime("%Y-%m-%d %H-%M-%S")}]
}


if __name__ == '__main__':
    my_Object = CSB()               # Create an instance of the class
    ch_func_mapping = {"1": "deposit", "2": "withdraw", "3": "balance", "4": "mini_statement", "5": exit}
    while True:
        ch = show_options()
        if ch in ch_func_mapping:
            # get the function name from the dictionary
            func_name = ch_func_mapping[ch]
            if ch == "5":
                print("Logged out Successfully")
                print("Thank you using CareerSoft Banking Application.")
                break
            # ch_func_mapping[ch]()
            else:
                # get the fucntion object from the instance and call it
                func = getattr(my_Object, func_name)
                func()
        else:
            print("Invalid Choice, Please enter Valid choice from 1-5")



