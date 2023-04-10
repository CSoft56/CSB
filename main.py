import datetime

from settings import show_options
from transactions import *
from datetime import date


today = datetime.datetime.today()
"""
Main for execution of CSB
"""
acc = {
    "AccNo": "A100",
    "Balance": 20000,
    "Name": "monica",
    "Transactions": [{"type": "debit", "amount": 20000, "date": today.strftime("%Y-%m-%d %H-%M-%S")}]
}


def signup(uname, password):
    with open('applicants.txt', 'r') as file:
        lines = file.readlines()                # read all lines at once
        for line in lines:                       # iterate over each line
            fields = line.strip().split(":")        # split the line into fields
            if len(fields) == 2:                 # check if there are two fields
                if fields[0] == uname and fields[1] == password:
                    print("Authentication successful")
                    return True
        return False


if __name__ == '__main__':
    from settings import show_options
    import sys

    print(sys.argv)

    uname = input("Enter username: ")
    password = input("Enter password: ")
    if signup(uname, password):
        pass
    else:
        print("Invalid user name or password.")
        exit()

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
