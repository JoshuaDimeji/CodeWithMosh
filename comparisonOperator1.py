'''
If name is less than 3 character long,
    name must be at least 3 characters
Otherwise, if it's more than 50 characters long
    name can be a maximum of 50 characters
Otherwise,
    name looks good
'''

name = input("What is your name? ")
name_char = len(name)

if name_char < 3:
    print("Name must be at least 3 characters long")
elif name_char > 50:
    print('Name can be a maximum of 50 characters')
else:
    print('Name looks good')

