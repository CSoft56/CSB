"""
Main for execution of CSB
"""
from Transaction import *

LOGGED_IN= False

def login_required(func):
    def helper(*args, **kwargs):
        if not LOGGED_IN:
            login(args[0], args[1])
        else:
            func(*args,*kwargs)
    return helper


    users=[{
        "user_name":"mahitha",
        "password":"manjusha@1695"
 },
        {
            "user_name": "satya",
            "password": "teddy@1695"

        }]

def login(username, password):
    with open('user.txt') as f:
        lines= f.readlines()
        users=lines[1:]

        for user in users:
            data=user.split(" ")
            if user['username'] == username and user['password'] == password:
                return True

    return False



if __name__ == '__main__':
    from Transaction import *
    import sys

    print(sys.argv)

    uname= input("Enter username: ")
    password=input("Enter password: ")
    if login(uname,password):
        pass
    else:
        print("invalid user name or password.")
        exit


    while True:
        ch = show_options()

        if ch in ch_func_mapping:
            if ch == "5":
                print("Logged out Successfully")
                print("Thank you using CareerSoft Banking Application.")
            ch_func_mapping[ch]()
        else:
            print("Invalid Choice, Please enter Valid choice from 1-5")

