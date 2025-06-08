"""
Here, I'm learning how to handle files in python
I want to open and access a .txt file in my Pycharm IDE
r is to read i.e to just view the contents of the file
w is to write the contents of the file or edit it
"""

file = open("data.txt","r")  # Open the file. Make sure it is in the same directory or simply paste the path to the file
a = file.read()  # Here, we assign the file to a variable...
print(a) # ...and print it out. This is actually a string

split1 = a.split("\n") # here, we do splitting, which is a way of converting a string into an array or list

print(split1)

# Now, I can then access some
for line in split1:          # This for loop then turn each of the data here into a string in each of the array
    split2 = line.split(" ")
    print(split2)

    the_sum = int(split2[1]) + int(split2[2]) + int(split2[3]) # We then sum up the values in index 1 to 3 of the list
    print("The sum is {}".format(the_sum))
    avg = float(the_sum / 3)
    if avg > 50:
        print("Your average score is {} and you passed!".format(avg))
    else:
        print("Your average score is {} and you failed!".format(avg))

