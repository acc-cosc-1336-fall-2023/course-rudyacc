from src.examples.j_classes.customer import Customer
class CustomerData:
    
    __file_name = 'customers.data'
    
    def save_customer(self, customer_list):
        
        out_file = open(self.__file_name)
        
        for customer in customer_list:
            out_file.write(customer.get_account(0).get_balance() + ',' + str(customer.get_account(1).get_balance()))+ '\n'
        
            
        
        
    def get_customers(self):
        in_file = open(self.__file_name)
        checking_balance = 0 
        savings_balance = 0 
        
        list_customers = []
        
        for line in in_file:
            balances = line.rstrip('\n').split(',')
            checking_balance = int(balances[0])
            savings_balance = int(balances[1])
            
            customer = Customer(checking_balance, savings_balance)
            list_customers.append(customer)
            
        in_file.close()
        
        return list_customers
    
