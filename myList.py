office_tools = ['chair', 'table', 'book', 'pen', 'tape']
house_tools = ['Television', 'speaker', 'radio', 'pots']

print(office_tools)
# Now, let me print the items in the list in a single order

for x in office_tools:
    print(x)
new_tool = input('Enter a new tool you want to add to the existing one: ')

office_tools.append('Plug')


office_tools.insert(6,new_tool)
office_tools.remove('pen')
print(office_tools)

total_list = office_tools + house_tools # we concatenate here just like strings
print(f'Here is your total list: {total_list}')