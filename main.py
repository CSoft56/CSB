"""
Main for execution of CSB
"""

def show_options():
    opts = """
    Welcome To CareerSoft Bank
    
    1. Deposit
    2. Withdraw
    3. Balance
    4. Mini Statement
    5. Exit
    """

    print(opts)
    ch = input("Please select option from above: ")

    return ch


if __name__ == '__main__':
    ch = show_options()
    print("User selected Option - {}".format(ch))

