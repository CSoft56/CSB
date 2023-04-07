"""
File Operations for transactions
"""
import datetime


def write_to_transactions(trans_type, trans_amount, trans_date=None):
    with open('../data/transactions.txt', 'a') as f:
        if not trans_date:
            trans_date = datetime.date.today()
            trans_date = '{}-{}-{}'.format(trans_date.year, trans_date.month, trans_date.day)

        trans_str = "\n{trans_type}\t\t{amount}\t\t{date_trans}".format(trans_type=trans_type,
                                                                        amount=trans_amount,
                                                                        date_trans=trans_date)
        f.write(trans_str)


with open('../data/transactions.txt', 'a') as f:
    type = 'Withdraw'
    Amount = 56000
    trans_date = datetime.date.today()
    str_trans_date = '{}-{}-{}'.format(trans_date.year, trans_date.month, trans_date.day)

    trans_str = "\n{trans_type}\t\t{amount}\t\t{date_trans}".format(trans_type=type,
                                                                  amount=Amount,
                                                                  date_trans=str_trans_date)
    f.write(trans_str)



"""
OOPS concepts in Python
Classes in Python
Inheritance
Objects
"""
class Transactions:
    def deposit(self):
        print('Inside deposit()')

    def withdraw(self):
        print('Inside withdraw()')

    def balance(self):
        print('Inside balance()')

    def mini_statement():
        print('Inside mini_statement()')


"""
For next class, I need you to:
1. Modules - move code from main.py to different modules
2. Make sure all functionalities are working
3. Move data dict to files (accounts, transactions, users)
4. Update transaction methods to read data from the files
5. Try to use a class for transactions
"""


if __name__ == '__main__':
    obj1 = Transactions()
    obj1.deposit()
    obj1.withdraw()
    obj1.balance()
    obj1.mini_statement()

    obj2 = Transactions()
    obj2.venkat = 'My Name'
    print(obj2.venkat)
    print(obj2.balance())




