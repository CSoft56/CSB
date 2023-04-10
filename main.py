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
    "Name": "manoj",
    "Transactions": [{"type": "debit", "amount": 20000, "date": today.strftime("%Y-%m-%d %H-%M-%S")}]
}


def signin(uname, password):
    with open('users.txt', 'r') as file:
        l = file.readlines()                # read all lines at once
        for l in l:                       # iterate over each line
            f = l.strip().split(":")        # split the line into fields
            if len(f) == 2:                 # check if there are two fields
                if f[0] == uname and f[1] == password:
                    print("Authentication successful")
                    return True
        return False


if __name__ == '__main__':
    from settings import show_options
    import sys

    print(sys.argv)

    uname = input("Enter username: ")
    password = input("Enter password: ")
    if signin(uname, password):
        pass
    else:
        print("Invalid user name or password.")
        exit()

    my_Obj = CSB()               # Create an instance of the class
    ch_function_mapping = {"1": "deposit", "2": "withdraw", "3": "balance", "4": "mini_statement", "5": exit}
    while True:
        ch = show_options()
        if ch in ch_function_mapping:
            # get the function name from the dictionary
            function_name = ch_function_mapping[ch]
            if ch == "5":
                print("Logged out Successfully")
                print("Thank you using CareerSoft Banking Application.")
                break
            # ch_function_mapping[ch]()
            else:
                # get the fucntion object from the instance and call it
                function = getattr(my_Obj, function_name)
                function()
        else:
            print("Invalid Choice, Please enter Valid choice from 1-5")

