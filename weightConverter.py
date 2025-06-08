# This program accept users weight in pounds (L) or Kilogram (k)
# It then converts to the other unit and gives you the output
# It's quite tasking but God will help me, I know



weight = input('Enter your weight here: ')

option = input('Choose your unit. L for pounds or K for kilograms: ')

if option == 'L' or option == 'l':
    weight_in_kg = float(weight) * 0.45
    print('Your weight in kg is', weight_in_kg)
elif option == 'K' or option == 'k':
    weight_in_lbs = float(weight) * 2.2
    print('Your weight in lbs is', weight_in_lbs)