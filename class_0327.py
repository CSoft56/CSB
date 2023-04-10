###
# File Opperation for transaction
###
import datetime

def write_to_transactions(trans_type, trans_amount, trans_date=None, str_trans_date=None):
    with open('date/tranx.txt','a') as f:
        if not trans_date:
            trans_date = datetime.date.today()
            trans_date = '{}-{}-{}'.format(trans_date.year, trans_date.month, trans_date.day)

        trans_str = "\n{trans_type}\t\t{amount}\t\t{date_trans}".format(trans_type=type,
                                                                    amount=trans_amount,
                                                                    date_trans=str_trans_date)
        f.write(trans_str)

with open('tranx.txt', 'a') as f:
    import datetime
    type= 'deposit'
    amount=3000
    trans_date = datetime.date.today()  # trans_date:03-30-2023
    str_trans_date = '{}-{}-{}'.format(trans_date.year, trans_date.month,trans_date.day)

    trans_str = "/n{trans_type}\t\t{amount}\t\t{date_trans}".format(trans_type=type,
                                                                    amount=amount,
                                                                    date_trans=str_trans_date)


    f.write(trans_str)

with open('tranx.txt', 'a') as f:
    import datetime
    type = 'withdraw'
    amount=15000
    trans_date = datetime.date.today()  # trans_date:03-30-2023
    str_trans_date = '{}-{}-{}'.format(trans_date.year, trans_date.month, trans_date.day)

    trans_str = "/n{trans_type}\t\t\t{amount}\t\t\t{date_trans}".format(trans_type=type,
                                                                        amount=amount,
                                                                        date_trans=str_trans_date)

    f.write(trans_str)




