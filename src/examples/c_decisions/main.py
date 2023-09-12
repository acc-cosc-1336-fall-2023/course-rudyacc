import decisions

result = decisions.is_overtime(40)

if(result == False):
    print('30 is overtime')


if(result):
    print('Is overtime')
else: 
    print("Not overtime")