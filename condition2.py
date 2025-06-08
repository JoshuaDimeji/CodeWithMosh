'''
Here is the problem we're giving solution to:
Price of a house is $1M
if buyer has good credit,
    they need to put down 10%
otherwise,
    they need to put down 20%
Print the down payment

'''


price_of_house = 1000000

has_good_credit = True
if has_good_credit:                         # This returns for 10%
    initial_pay = int(price_of_house) * 0.1
    print('You will need to put down 10% which is $' +str(initial_pay))
else:                                   # This returns for 20%
    initial_pay = int(price_of_house) * 0.2
    print('You will need to put down 20% which is $' +str(initial_pay))