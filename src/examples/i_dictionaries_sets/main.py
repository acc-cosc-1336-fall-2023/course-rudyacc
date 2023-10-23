#main program
phonebook = {'Chris': '555-1111', 'Katie': '555-2222', 'Joanne': '555-3333'}
#print(phonebook)

#print(phonebook['Chris'])
#print(phonebook['Katie'])

for key in phonebook:
    print(phonebook[key])
    
print("values only")
for value in phonebook.values():
    print(value)
    
print("dictionary item")
for item in phonebook.items():
    print(item)
    