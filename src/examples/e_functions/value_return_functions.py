def test_config():
    return True

def is_number_odd(num):
    return num % 2 == 1

def local_function_variable(val0):
    val = 100
    val2 = 10
    
val3 = 5
def global_variable_w_param(val3):
    val3 = 10
    
def global_variable():
    val3 = 5
    print(val3)
    
def global_variable_2():
    print(val3)
    
def get_random_numbers(min, max):
    return random.randint(min, max)