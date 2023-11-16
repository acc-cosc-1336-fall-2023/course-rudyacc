import random, time
from src.examples.j_classes.customer import Customer
from src.examples.j_classes.atm import ATM



def scan_card(customer_list_size):
    random.seed(int(time.time()))
    choice = print('Enter something... ')#pause
    return random.randint(0, customer_list_size-1)

    
    
def display_menu():
    print('COSC Bank')
    print('1-Deposit')
    print('2-Withdraw')
    print('3-Display Balance')
    print('4-Exit')
    
def run_menu():
    
    list_customers = []
    
    random.seed(int(time.time()))
    customer = Customer(-1, -1)
    list_customers.append(customer)
    
    random.seed(int(time.time()))
    customer = Customer(-1, -1)
    list_customers.append(customer)
    
    random.seed(int(time.time()))
    customer = Customer(-1, -1)
    list_customers.append(customer)
        
    while(True):
        menu_choice = 0
        customer_index = scan_card(len(list_customers))
        
        
        customer = list_customers[customer_index]
        print(customer)
        account_index = input("Enter 1 for checking 2 for savings")
        
        account = customer.get_account(account_index)
        print(account)
        atm = ATM(account)
        
        
        
    
        while(menu_choice != '4'):
            display_menu()
            menu_choice = input("Enter choice: ")
        
def handle_menu(menu_choice, atm):
    if(menu_choice == '1'):
        atm.make_deposit()
    elif(menu_choice == '2'):
        atm.make_withdraw()
    elif(menu_choice == '3'):
        atm.display_balance()
    elif(menu_choice == '4'):
        print('Exiting...')
    else:
        print('Invalid Response')