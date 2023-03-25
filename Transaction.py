
from main import acc
from main import today

def deposit():
    amt = int(input("Enter the amount to deposit: "))
    updated = acc["Balance"] + amt
    acc["Balance"] = updated
    print("Transaction completed successfully")
    acc["Transactions"].append({'type': 'debit', 'amount': updated, 'date': today.strftime("%Y-%m-%d")})
    print("Your New Balance is: {}".format(acc["Transactions"]))


def withdraw():
    amt_1 = int(input("Enter the amount to withdraw: "))
    if acc["Balance"] <= amt_1:
        print("Error, Insufficient Balance")
    else:
        updated = acc["Balance"] - amt_1
        acc["Balance"] = updated
        acc["Transactions"].append({'type': 'debit', 'amount': updated, 'date': '2023-03-12'})
        print("Transaction completed successfully")
        print("Your New Balance is: {}".format(acc["Transactions"]))


def balance():
    print("Your New Balance is: {}".format(acc["Transactions"][-1]))


def mini_statement():

    print("Mini Statement is: {}".format(acc["Transactions"]))
