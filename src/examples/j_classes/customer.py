import src.examples.j_classes.bank_account

class Customer:
    
    list_accounts = []
    
    def __init__(self):
        
        self.__list_accounts.append(src.examples.j_classes.bank_account.BankAccount(-1))
        self.__list_accounts.append(src.examples.j_classes.bank_account.BankAccount(-1))
    
    def get_account(self, index):
        return self.__list_accounts[index]
    
    