# Non-OOP
# Bank 3 
# Two Accounts 

acc0Name = ''
acc0Balance = 0
acc0Pwd = ''

acc1Name = ''
acc1Balance = 0
acc1Pwd = ''


def newAccount(accountNumber,name, balance, password):
    global acc0Name, acc0Balance, acc0Pwd 
    if accountNumber = 0 
        acc0Name = name 
        acc0Balance = balance 
        acc0Pwd = password 
    
    global acc1Name, acc1Balance, acc1Pwd 
    if accountNumber == 1:
        acc1Name = name 
        acc1Balance = balance 
        acc1Pwd = password 


def show():

    global acc0Name, acc0Balance, acc0Pwd 
    if acc0Name != '':
        print('     Name',acc0Name)
        print('     Balance:',acc0Balance)
        print('     Password:',acc0Pwd)
    if acc1Name != '':
        print('     Name',acc1Name)
        print('     Balance:',acc1Balance)
        print('     Password:',acc1Pwd)
    



def getBalance(accountNumber,password):
    global acc0Name, acc0Balance, acc0Pwd 
    if accountNumber == 0:
        if password != acc0Pwd:
            print('Incorrect password')
            return None 
        return acc0Balance 
    if accountNumber == 1:
        if password != acc1Pwd:
            print('Incorrect password')
            return None 
        return acc1Balance 



def deposit(accountNumber,amounToDeposit, password):
    global acc0Name, acc0Balance, acc0Pwd 
    global acc1Name, acc1Balance, acc1Pwd
    if accountNumber == 0:
        if amounToDeposit < 0: 
            print('You can not deposit a negative amount')
            return None 

        if password != acc0Pwd:
            print('Incorrect password')
            return None 

        acc0Balance += amounToDeposit
        return acc0Balance
    if accountNumber == 0:
        if amounToDeposit < 0: 
            print('You can not deposit a negative amount')
            return None 

        if password != acc1Pwd:
            print('Incorrect password')
            return None 

        acc1Balance += amounToDeposit
        return acc1Balance



def withdraw(accountNumber,amountToWithdraw, password):
    global acc0Name, acc0Balance, acc0Pwd
    global acc1Name, acc1Balance, acc1Pwd 

    if accountNumber == 0:
        if amountToWithdraw < 0:
            print('You can not withdraw a negative amount')
            return None
        if password != acc0Pwd:
            print('Incorrect password for this account')
            return None
        if amountToWithdraw > acc0Balance:
            print('You can not withdraw more than what you have in your account')
            return None
        accBalance -= amountToWithdraw
        return accBalance
    
    if accountNumber == 1:
        if amountToWithdraw < 0:
            print('You can not withdraw a negative amount')
            return None
        if password != acc1Pwd:
            print('Incorrect password for this account')
            return None
        if amountToWithdraw > acc1Balance:
            print('You can not withdraw more than what you have in your account')
            return None
        acc1Balance -= amountToWithdraw
        return acc1Balance
    


newAccount(1,"Joe", 100, 'soup')

while True:
    print()
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press w to make a withdrawal')
    print('Press s to show the account')
    print('Press q to quit')
    print()
    action = input('What do you want to do? ')
    action = action.lower() # force lowercase
    action = action[0] # just use first letter
    print()
    if action == 'b':
        print('Get Balance:')
        userPassword = input('Please enter the password: ')
        theBalance = getBalance(1,userPassword)
        if theBalance is not None:
            print('Your balance is:', theBalance)
    elif action == 'd':
        print('Deposit:')
        userDepositAmount = input('Please enter amount to deposit: ')
        userDepositAmount = int(userDepositAmount)
        userPassword = input('Please enter the password: ')
        
        newBalance = deposit(1,userDepositAmount, userPassword)
        if newBalance is not None:
            print('Your new balance is:', newBalance)
    elif action == 's':
        show()
    elif action == 'w'
        print('Withdraw:')
        userWithdrawAmmount = input('Please enter the amount to withdraw: ')
        userWithdrawAmmount = int(userWithdrawAmmount)
        userPassword = input('Please enter the password: ')
        newBalance = withdraw(1,userWithdrawAmmount, userPassword)
    elif  action == 'q':
        exit()


print('Done')
