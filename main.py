"""
Main for execution of CSB
"""
users = [{
    "user_name": "venkat",
    "password": "csoft"
},
    {
        "user_name": "kapil",
        "password": "csoft123"

    }]

LOGGED_IN = False

def login_required(func):
    def helper(*args, **kwargs):
        global LOGGED_IN
        if not LOGGED_IN:
            if login():
                LOGGED_IN = True
        func(*args, **kwargs)

    return helper


def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    try:
        with open('data/users.txt') as f:
            lines = f.readlines()
            users = lines[1:]

            for user in users:
                data = user.split()
                if data[0] == username and data[1] == password:
                    return True
    except FileNotFoundError:
        print("Users file not found. Please check the path")

    return False


@login_required
def withdraw(amount):
    print('logged in')


    # for user in users:
    #     if user['user_name'] == username and user['password'] == password:
    #         return True
    #
    # return False


if __name__ == '__main__':
    withdraw(100)

    from services.transactions import show_options, ch_func_mapping
    import sys

    print(sys.argv)
    if login():
        pass
    else:
        print("Invalid user name or password.")
        exit()

    while True:
        ch = show_options()

        if ch in ch_func_mapping:
            if ch == "5":
                print("Logged out Successfully")
                print("Thank you using CareerSoft Banking Application.")
            ch_func_mapping[ch]()
        else:
            print("Invalid Choice, Please enter Valid choice from 1-5")


"""
Built-in Modules
1. os

2. sys
3. datetime
4. re 
5. 



"""
