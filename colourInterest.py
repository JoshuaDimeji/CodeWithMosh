name = input("What is your name? ")
colour = input("What is your favorite colour? ")

print(f"{name}'s favourite colour is {colour} ")
year = input("What year are you born? ")
age = 2025 - int(year)
print(f'Today, you are {age} years old') # This is formatted string
print('Today, you are ' + str(age) + ' years old.') # we do a data type conversion for age because we can't concatenate an integer

print(type(name)) # this is to determine the type of variable
print(type(year))
print(type(age))