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


