import dictionaries
#main program


phonebook = {}#empty dictionary

dictionaries.add_friend_phonebook('Chris', '555-1111', phonebook)
dictionaries.add_friend_phonebook('Katie', '555-2222', phonebook)

for name, value in phonebook.items():
    print(name, value)

print(' \nUpdate Katie \n')
dictionaries.update_friend_phonebook('Katie', '555-2345', phonebook)

for name, value in phonebook.items():
    print(name, value)

print('\nDelete Chris \n')    
dictionaries.delete_friend_phonebook('Chris', phonebook)
    
for name, value in phonebook.items():
        print(name, value)
        
        


    