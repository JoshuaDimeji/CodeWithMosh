'''
Logical operator is used for processing multiple conditions e.g
If applicant has high income AND good credit
    Eligible for laon
We have the AND, OR, NOT as logical operators
AND: Both conditions should be true
OR: At least one condition should be true
NOT: This inverses any boolean value we give it
'''

has_high_income = True
has_good_credit = False

if has_high_income or has_good_credit:
    print('Eligible for laon')
else:
    print('Not Eligible for laon')