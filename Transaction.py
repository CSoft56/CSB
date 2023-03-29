import datetime

from database_file import write_to_transactions
from main import acc
from main import today


def deposit():
    amt = int(input("Enter the amount to deposit: "))
    updated = acc["Balance"] + amt
    acc["Balance"] = updated
    print("Transaction completed successfully")
    acc["Transactions"].append({'type': 'debit', 'amount': updated, 'date': today.strftime("%Y-%m-%d %H-%M-%S")})
    # print("Your New Balance is: {}".format(acc["Transactions"]))


    with open('transaction.txt', 'a') as f:
        type = 'Deposit'
        Amount = updated
        trans_date = datetime.date.today()
        str_trans_date = '{}-{}-{}'.format(trans_date.year, trans_date.month, trans_date.day)

        trans_str = "\n{trans_type}\t\t\t\t\t{amount}\t\t\t\t{date_trans}".format(trans_type=type,
                                                                      amount=Amount,
                                                                      date_trans=str_trans_date)
        f.write(trans_str)



def withdraw():
    amt_1 = int(input("Enter the amount to withdraw: "))
    if acc["Balance"] <= amt_1:
        print("Error, Insufficient Balance")
    else:
        updated = acc["Balance"] - amt_1
        acc["Balance"] = updated
        acc["Transactions"].append({'type': 'debit', 'amount': updated, 'date': today.strftime("%Y-%m-%d %H-%M-%S")})
        print("Transaction completed successfully")
        # print("Your New Balance is: {}".format(acc["Transactions"]))


    with open('transaction.txt', 'a') as f:
        type = 'Withdraw'
        Amount = updated
        trans_date = datetime.date.today()
        str_trans_date = '{}-{}-{}'.format(trans_date.year, trans_date.month, trans_date.day)

        trans_str = "\n{trans_type}\t\t\t\t{amount}\t\t\t\t{date_trans}".format(trans_type=type,
                                                                      amount=Amount,
                                                                      date_trans=str_trans_date)
        f.write(trans_str)


def balance():
    print("Your New Balance is: {}".format(acc["Transactions"][-1]))


def mini_statement():
    print(len["Transactions"])
    if len("Transactions") <= 10:
        print("Mini Statement is: {}".format(acc["Transactions"]))
    else:
        print("Mini Statement is: {}".format(acc["Transactions"][-10]))