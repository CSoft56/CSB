import datetime
from main import today
from main import acc

class Transactions:

    def deposit(self):
        amt = int(input("Enter the amount to deposit: "))
        updated = acc["Balance"] + amt
        acc["Balance"] = updated
        print("Transaction completed successfully")
        acc["Transactions"].append({'type': 'debit', 'amount': updated, 'date': today.strftime("%Y-%m-%d")})
        print("Your New Balance is: {}".format(acc["Transactions"][-1]))

        with open('statement.txt', 'a') as f:
            type = 'deposit'
            Amount = updated
            trans_date = datetime.date.today()
            str_trans_date = '{}-{}-{}'.format(trans_date.year, trans_date.month, trans_date.day)

            trans_str = "\n{trans_type}\t\t\t{amount}\t\t{date_trans}".format(trans_type=type,
                                                                            amount=Amount,
                                                                            date_trans=str_trans_date)
            f.write(trans_str)

    def withdraw(self):
        # amt_1 = int(input("Enter the amount to withdraw: "))
        try:
            amt_1 = int(input("Enter the amount to withdraw: "))
            if acc["Balance"] <= amt_1:
                raise ValueError("Invalid Amount")
        except Exception:
            print("Error, Insufficient Balance")
            return

        # if acc["Balance"] <= amt_1:
        #     print("Error, Insufficient Balance")
        # else:
        #     updated = acc["Balance"] - amt_1
        #     acc["Balance"] = updated
        #     acc["Transactions"].append({'type': 'debit', 'amount': updated, 'date': today.strftime("%Y-%m-%d")})
        #     print("Transaction completed successfully")
        #     print("Your New Balance is: {}".format(acc["Transactions"][-1]))

        updated = acc["Balance"] - amt_1
        acc["Balance"] = updated
        acc["Transactions"].append({'type': 'debit', 'amount': updated, 'date': today.strftime("%Y-%m-%d")})
        print("Transaction completed successfully")
        print("Your New Balance is: {}".format(acc["Transactions"][-1]))



        with open('statement.txt', 'a') as f:
            type = 'withdraw'
            Amount = updated
            trans_date = datetime.date.today()
            str_trans_date = '{}-{}-{}'.format(trans_date.year, trans_date.month, trans_date.day)
            trans_str = "\n{trans_type}\t\t{amount}\t\t{date_trans}".format(trans_type=type,
                                                                            amount=Amount,
                                                                            date_trans=str_trans_date)
            f.write(trans_str)


    def balance(self):
        print("Your New Balance is: {}".format(acc["Transactions"][-1]))


    def mini_statement(self):
        with open('statement.txt', 'r') as f:
            linesList = f.readlines()
            print("Transaction      Amount      Date\n")
            for textline in (linesList[-10:]):
                print(textline, end='')
