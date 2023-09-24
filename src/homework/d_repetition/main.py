from homework.d_repetition.repetition import get_factorial, sum_odd_numbers


def display_menu():
    print("Homework 3 Menu")
    print("Select 1 for Factorial")
    print("Select 2 for the Sum of ODD numbers")
    print("Select 3 to exit")

def run_menu():
    display_menu()
    option = input("Select your option 1, 2, or 3: ")
    if (option != "1" and option != "2" and option != "3"):
        print("Invalid Option, Exiting Program")

    handle_menu_option(option)

def handle_menu_option(option):
    if(option == '1'):
        option_1_selected()
    if(option == '2'):
        option_2_selected()
    if(option == '3'):
        option_3_selected()

def option_1_selected():
    num = -1
    while num < 1 or num > 9:
        while True:
            try:
                num = int(input("Please Enter a Number 1-9: "))
                break
            except ValueError:
                print("That option is invalid. Input an Number 1-9. ")
    
    product = get_factorial(num)
    print("The factorial of",num,"is:",product)
    exit_selected()

def option_2_selected():
    num = -1
    while num < 1 or num > 99:
        while True:
            try:
                num = int(input("Please Enter a Number 1-99: "))
                break
            except ValueError:
                print("That option is invalid. Input an Number 1-99. ")
    sum = sum_odd_numbers(num)
    print("The sum of the odd numbers of",num,"is equal to",sum)
    exit_selected()

def exit_selected():
    while True:
        exit = input("Enter yes if you want to continue. Enter no if you want to exit: ")
        if exit == "yes" or exit == "y" or exit =='Y' or exit == 'YES':
            run_menu()
            break
        elif exit == "no" or exit == "n" or exit == 'N' or exit == 'NO':
            print("Exiting Program")
            break
        else:
            print("Enter either yes/no")

def option_3_selected():
    while True:
        exit = input("Are you sure you want to exit y/n: ")
        if exit == "yes" or exit == "y" or exit =='Y' or exit == 'YES':
            print("Exiting Program")
            break
        elif exit == "no" or exit == "n" or exit == 'N' or exit == 'NO':
            run_menu()
            break
        else:
            print("Enter either yes/no")

