import src.examples.j_classes.bank_account

class Customer:
    
    list_accounts = []
    
    def __init__(self, checking_balance, saving_balance):       
        self.__list_accounts.append(src.examples.j_classes.bank_account.BankAccount(checking_balance))
        self.__list_accounts.append(src.examples.j_classes.bank_account.BankAccount(saving_balance))
    
    def get_account(self, index):
        return self.__list_accounts[index]
    
    