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


def login(username, password):

    with open('users.txt', 'r') as file:
        for line in file:                       # reading each word
            for word in line.split():           # displaying the words
                if word == uname:
                    for word_ in line.split():
                        if word_ == password:
                            print("Authentication is successful")
                            return True
        return False


if __name__ == '__main__':
    from settings import show_options
    import sys

    print(sys.argv)

    uname = input("Enter username: ")
    password = input("Enter password: ")
    if login(uname, password):
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