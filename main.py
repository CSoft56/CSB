"""
Main for execution of CSB
"""

from transaction import *
#from options import show_options
from datetime import date
today = date.today()


acc = {
    "AccNo": "A100",
    "Balance": 20000,
    "Name": "Jagadesh",
    "Transactions": [{"type": "debit", "amount": 20000, "date": today.strftime("%Y-%m-%d %H-%M-%S")}]
}


def login(username, password):
    with open('loggin_info.txt', 'r') as file:
        lines = file.readlines()                # read all lines at once
        for line in lines:                       # iterate over each line
            fields = line.strip().split(":")        # split the line into fields
            if len(fields) == 2:                 # check if there are two fields
                if fields[0] == username and fields[1] == password:
                    print("Authentication successful")
                    return True
        return False
    # Close the file



    # with open("login_credentials.txt", "r") as f:
    #     login_credentials = {}
    #     for line in f:
    #         # Split each line into a username and password pair
    #         username, password = line.strip().split(":")
    #         login_credentials[username] = password
    #
    #     if username in login_credentials:
    #             # If it does, check if the entered password matches the stored password
    #         if login_credentials[username] == password:
    #             print("Login successful!")
    #         else:
    #             print("Incorrect password.")
    #             exit()
            # else:
            #     print("Username not found.")




       # with open('login_credentials.txt', 'r') as file:
       #     for line in file:  # reading each word
       #         for word in line.split():  # displaying the words
       #             if word == username:
       #                 for word_ in line.split():
       #                     if word_ == password:
       #                         print("Authentication is successful")
       #                         return True
       #     return False
    # Check if the username exists in the login credentials dictionary


if __name__ == '__main__':
    from Settings import show_options
    import sys

    print(sys.argv)

    uname = input("Enter username: ")
    password = input("Enter password: ")

    if login(uname, password):
        pass
    else:
        print("Username not found")
        exit()

    x = Transactions()
    ch_func_mapping = {"1": "deposit", "2": "withdraw", "3": "balance", "4": "mini_statement", "5": exit}
    while True:
        ch = show_options()
        if ch in ch_func_mapping:
            opt_func = ch_func_mapping[ch]
            if ch == "5":
                print("Logged out Successfully")
                print("Thank you using CareerSoft banking Application")
                break
            else:
                fun = getattr(x, opt_func)
                fun()
        else:
            print("Invalid Choice, Please enter Valid choice from 1-5")


