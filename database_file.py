import datetime
from main import today


def write_to_transactions(trans_type, trans_amount, trans_date=None):
    with open('transactions.txt', 'a') as f:
        if not trans_date:
            trans_date = datetime.date.today()
            trans_date = '{}-{}-{}'.format(trans_date.year, trans_date.month, trans_date.day)

        trans_str = "\n{trans_type}\t\t{amount}\t\t{date_trans}".format(trans_type=trans_type,
                                                                        amount=trans_amount,
                                                                        date_trans=trans_date)
        f.write(trans_str)


with open('transactions.txt', 'a') as f:
    type = 'Withdraw'
    Amount = 56000
    trans_date = datetime.date.today()
    str_trans_date = '{}-{}-{}'.format(trans_date.year, trans_date.month, trans_date.day)

    trans_str = "\n{trans_type}\t\t{amount}\t\t{date_trans}".format(trans_type=type,
                                                                  amount=Amount,
                                                                  date_trans=str_trans_date)
    f.write(trans_str)
