def currency():
    choices=[1,2,3]
    user_choice = 0
    amount=int(input('Enter the amonut to be transfared from egyptian pounds: '))
    while user_choice not in choices:
        user_choice = int(input('Please chose the currency you want to convert from:\n1-USD\n2-Euro\n3-GBP\n'))

    transfer_amount=''

    if user_choice == 1:
        transfer_amount=amount*26
        print('USD\n',amount,'\n' ,'Money in USD is: ',transfer_amount)
    elif user_choice == 2:
        transfer_amount=amount*28
        print('Euro\n', amount, '\n', 'Money in Euro is: ', transfer_amount)
    elif user_choice == 3:
        transfer_amount=amount*31.87
        print('GBP\n', amount, '\n', 'Money in GBP is: ', transfer_amount)

currency()