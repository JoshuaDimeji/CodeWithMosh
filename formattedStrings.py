first = 'James'
last = 'Morgan'

print(first + ' [' + last + '] is a medical doctor')
# the above statement can be written in a different way from concatenation using the formatted string

message = f'{first} [{last}] is a medical doctor'
message_new = f'{first} 2{last}2 is a medical doctor'


print(message)
print(message_new)

print(f"Hello, Mr {first} {last}!")
