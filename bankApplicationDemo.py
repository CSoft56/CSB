"""
1.deposit
2.withdraw
3.balance
4.mini statement
5.exit
"""


def deposit(curr_bal, amount, mini, c):
    curr_bal += amount
    mini[c] = [c]
    mini[c].append('xxxxxx1234')
    mini[c].append('deposit')
    mini[c].append('01-01-2023')
    print('Deposit is successful\nYour new balance is {}'.format(curr_bal))
    return curr_bal


def withdraw(curr_bal, amount, mini, c):
    if curr_bal >= amount:
        curr_bal -= amount
        mini[c] = [c]
        mini[c].append('xxxxxx1234')
        mini[c].append('withdraw')
        mini[c].append('01-01-2023')
        print('Transaction is Successful\nYour new balance is {}'.format(curr_bal))
    else:
        print('ERROR: Requested amount is greater than current balance')
    return curr_bal


def balance(curr_bal):
    print('Current account balance is:', curr_bal)


def ministatement(mini):
    print("{:<10} {:<10} {:<20} {:<10}".format('SNo.', 'Acc_no', 'Transaction_type', 'date'))
    for key, value in mini.items():
        sno, acc_no, trans_type, date = value
        print("{:<10} {:<10} {:<20} {:<10}".format(sno, acc_no, trans_type, date))


curr_bal = 20000
c = 1
mini = {}
while True:
    print('Welcome to CareerSoft Bank\n--------------------------------')
    option = int(input('Options:\n1.Deposit\n2.Withdraw\n3.Balance\n4.Mini Statement\n5.Exit\nEnter your option:'))
    if option == 1:
        amount = int(input('Enter the amount to deposit:'))
        curr_bal = deposit(curr_bal, amount, mini, c)
        c += 1
    elif option == 2:
        amount = int(input('Enter the amount to withdraw:'))
        curr_bal = withdraw(curr_bal, amount, mini, c)
        c += 1
    elif option == 3:
        balance(curr_bal)
    elif option == 4:
        ministatement(mini)
    elif option == 5:
        print('Logout Successfully\nThank you for using Careersoft Bank')
        break
    else:
        print('Please enter a valid option')
    print('***********************************')
