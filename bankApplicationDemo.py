"""
1.deposit
2.withdraw
3.balance
4.mini statement
5.exit
"""


def deposit(curr_bal, amount, mini, c):
    curr_bal += amount
    mini['Sno'].append(c)
    mini['Acc_no'].append('xxxxxx1234')
    mini['transaction_type'].append('deposit')
    mini['date'].append('01-01-2023')
    print('Transaction is Successful')
    return curr_bal


def withdraw(curr_bal, amount, mini, c):
    if curr_bal >= amount:
        curr_bal -= amount
        mini['Sno'].append(c)
        mini['Acc_no'].append('xxxxxx1234')
        mini['transaction_type'].append('withdraw')
        mini['date'].append('01-01-2023')
        print('Transaction is Successful')
    else:
        print('ERROR: Requested amount is greater than current balance')
    return curr_bal


def balance(curr_bal):
    print('Current account balance is:', curr_bal)


def ministatement(mini):
    print(mini)



curr_bal = 20000
c = 1
mini = {'Sno': [], 'Acc_no': [], 'transaction_type': [], 'date': []}
while True:
    print('Welcome to CareerSoft Bank\n--------------------------------')
    option = int(input('Select an option\n1.Deposit\n2.Withdraw\n3.Balance\n4.Mini Statement\n5.Exit\n'))
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