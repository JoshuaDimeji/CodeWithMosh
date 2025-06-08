# Here, let's see some crazy stuffs we can do with strings in Python

message = 'Python for beginners'
print(len(message)) #this gives us the lenght of the string or number of characters there in the string

print(message.upper()) # convert the string to capital letter
print(message.lower()) # convert the string to lowercase

print(message.find('h')) # this returns the index of the character, where it is first seen
print(message.find('n'))
print(message.replace('for', 'and')) # as the name implies, it changes a character or word for another

print('for' in message) # a boolean expression to check if a character is in a string. Result here is True
print('of' in message)