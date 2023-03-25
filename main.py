"""
Main for execution of CSB
"""


if __name__ == '__main__':
    from services.transactions import show_options, ch_func_mapping
    import sys

    print(sys.argv)

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
