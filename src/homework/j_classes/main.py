import class_a

user_input = str(input("Press Y to roll a die and see the result: ")).lower()
while user_input == 'y':
     dice = class_a.Die()
     dice.roll()
     print(dice)
     user_input = str(input("Press Y to roll the Die again: ")).lower()
     print(" ")