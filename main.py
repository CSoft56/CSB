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

def login(username, password):
    for user in users:
        if user['user_name'] == username and user['password'] == password:
            return True

    return False


if __name__ == '__main__':
    from services.transactions import show_options, ch_func_mapping
    import sys

    print(sys.argv)

    uname = input("Enter username: ")
    password = input("Enter password: ")
    if login(uname, password):
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
