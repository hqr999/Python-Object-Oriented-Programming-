# Non-OOP
# Bank 2 
# Single Account 

accName = ''
accBalance = 0
accPwd = ''

def newAccount(name, balance, password):
    global accName, accBalance, accPwd 
    accName = name 
    accBalance = balance 
    accPwd = password 


def show():
    global accName, accBalance, accPwd 
    print('     Name',accName)
    print('     Balance:',accBalance)
    print('     Password:',accPwd)


def getBalance(password):
    global accName, accBalance, accPwd
    if password != accPwd:
        print('Incorrect password')
        return None 
    return accBalance 


def deposit(amounToDeposit, password):
    global accName, accBalance, accPwd
    if amounToDeposit < 0: 
        print('You can not deposit a negative amount')
        return None 

    if password != accPwd:
        print('Incorrect password')
        return None 

    accBalance += amounToDeposit
    return accBalance

def withdraw(amountToWithdraw, password):
    global accName, accBalance, accPwd
    if amountToWithdraw < 0:
        print('You can not withdraw a negative amount')
        return None
    if password != accPwd:
        print('Incorrect password for this account')
        return None
    if amountToWithdraw > accBalance:
        print('You can not withdraw more than what you have in your account')
        return None
    accBalance -= amountToWithdraw
    return accBalance




newAccount("Joe", 100, 'soup')

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
        theBalance = getBalance(userPassword)
        if theBalance is not None:
            print('Your balance is:', theBalance)
    elif action == 'd':
        print('Deposit:')
        userDepositAmount = input('Please enter amount to deposit: ')
        userDepositAmount = int(userDepositAmount)
        userPassword = input('Please enter the password: ')
        
        newBalance = deposit(userDepositAmount, userPassword)
        if newBalance is not None:
            print('Your new balance is:', newBalance)
    elif action == 's':
        show()
    elif action == 'w'
        print('Withdraw:')
        userWithdrawAmmount = input('Please enter the amount to withdraw: ')
        userWithdrawAmmount = int(userWithdrawAmmount)
        userPassword = input('Please enter the password: ')
        newBalance = withdraw(userWithdrawAmmount, userPassword)
    elif  action == 'q':
        exit()


print('Done')
