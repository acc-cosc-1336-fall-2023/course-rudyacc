def test_config():
    return True

def display_nums_list():
    list1 = [5, 10, 20]
    print(list1)
    
def display_list_w_while():
    list1 = [5, 10, 20]
    
    indx = 0
    
    while(indx < len(list1)):
        print(list1[indx])
        indx += 1
        
def display_reverse_list_w_while():
    list1 = [5, 10, 20]
    
    list_index = len(list1)-1
    
    while(list_index >= 0):
        print(list1[list_index])
        list_index -= 1

def display_list_w_for_range():
    list1 = [5, 10, 20]
    
    for i in range (0, len(list1)):
        
        print(list1[i])
        
        
def display_list_w_for_range():
    list1 = [5, 10, 20, 3, 7, 1, 50]
    
    for i in range (0, len(list1), 2):
        print(list1[i])
        
def display_reverse_list_w_for_range():
    list1 = [5, 10, 20]
    
    for i in range(len(list1), 0, -1):
        
        print(list1[i-1])
    
def search_for_item_in_list(item,list):
    return item in list
    
def get_multiplication_table(max_value):
        table = []
        
        for r in range(1, max_value + 1):
            row = []
            
        for c in range(1, max_value + 1):
            row.append(r * c)
                
            table.append(row)
            
        return table
    
    
        