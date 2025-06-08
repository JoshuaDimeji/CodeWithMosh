# Here, I want to use for loops to create a multiplication table
# Let's see how it goes here

num1 = 1
num2 = int(input('What multiplication table do you want to Know? '))

while num1 <= 12:
    print(f"{num1} x {num2} = {(num1 * num2)}")
    num1 += 1