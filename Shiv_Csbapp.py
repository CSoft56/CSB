import datetime

acc = {
    "AccNo": "CSB100",
    "Balance": 20000,
    "Name": "Shivani",
    "Transactions": [{"type": "debit", "amount": 20000, "date": "2023-03-12"}]
}

def options():
    opts = """
         Welcome To CareerSoft Bank
            1. Deposit
            2. Withdraw
            3. Balance
            4. Mini Statement
            5. Exit
            """

    print(opts)
    choice = int(input("Please select option from above: "))
    return choice

#loop = True
while True:
    choice = options()

    if choice == 1:
        userdepamt = int(input("Please enter the amount you like to deposit: "))
        current_date = datetime.date.today()
        acc["Transactions"].append({"type": "credit", "amount": userdepamt, "date": current_date.strftime("%Y-%m-%d")})
        acc["Balance"] = acc["Balance"] + userdepamt
        print("Your transaction has been successfully completed." "Your current new balance is {}". format(acc["Balance"]))

    elif choice == 2:
        userwdamt = int(input("Please enter the amount to withdraw: "))
        if userwdamt <= acc["Balance"]:
            current_date = datetime.date.today()
            acc["Transactions"].append({"type": "debit", "amount": userwdamt, "date": current_date.strftime("%Y-%m-%d")})
            acc["Balance"] = acc["Balance"] - userwdamt
            print("Your transaction has been successfully completed and current new balance is {}".format(acc["Balance"]))
        else:
            print("""
                     Your withdraw amount limit exceeds your current balance.
                     Please check the balance before deduction.
                     Transaction cancelled, please try again.11
                    """)
    elif choice == 3:
        print("Your current balance is {}". format(acc["Balance"]))
    elif choice == 4:
        print("Here are your last 10 transactions-{}".format(acc["Transactions"][-11:]))
    elif choice == 5:
        print("""
        Logged Out Successfully.
        Thankyou For Choosing CareerSoft Bank.
              """)
        break
    else:

        print("""
               Invalid Option.
                     """)
