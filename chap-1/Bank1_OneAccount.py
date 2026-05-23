#Non-OOP 
#Bank v1 
#Single account 

accountName = 'Joe'
accountBalance = 100 
accountPwd = 'soup'

while True:
    print()
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press w to make a withdrawal')
    print('Press s to show the account')
    print('Press q to quit')

    action = input('What do you want to do ?')
    action = action.lower() #force lowercase 
    action = action[0] #first letter 

    if action == 'b':
        print('Get Balance')
        userPass = input('Please enter the password: ')
        if userPass != accountPwd:
            print('Incorrect password')
        else:
            print('Your Balance is:',accountBalance)
    elif action == 'd':
        print('Deposit:')
        userDepositAmount = input('Please enter the amount you want to deposit: ')
        userDepositAmount = int(userDepositAmount)
        userPass = input('Please enter the password: ')
        if userDepositAmount < 0:
            print('You cannot deposit a negative ammount!')
        elif userPass != accountPwd:
            print('Incorrect password')
        else:
            accountBalance = accountBalance + userDepositAmount
            print('Your new balance is:',accountBalance)

    elif action == 's':
        print('Show:')
        print('         Name:',accountName)
        print('         Balance:',accountBalance)
        print('         Password:',accountPwd)
    elif action == 'q':
        break 
    elif action == 'w':
        print('Withdraw:')

        userWithdrawlAmount = input('Please enter the amount to withdraw: ')
        userWithdrawlAmount = int(userWithdrawlAmount)
        userPass = input('Please enter the password: ')
        
        if userWithdrawlAmount < 0:
            print('You cant withdraw a negative number')
        elif userPass != accountPwd:
            print('Incorrect password for this account')
        elif userWithdrawlAmount > accountBalance:
            print('You cannot withdraw more than you have in your account')

        else:
            accountBalance -= userWithdrawlAmount 
            print('Your new balance is:',accountBalance)

print('done')
