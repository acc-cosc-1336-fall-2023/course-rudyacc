def get_factorial(num):
    product = 1
    if num < 0:
        return "Invalid, you can't factorial negative numbers"
    else:
        for n in range(1,num+1):
            product *= n
        return product
    

def sum_odd_numbers(num):
    sum = 0

    while num > 0:
        if ((num % 2) == 0):
            num = num - 1
        sum += num
        num = num - 2

    return sum

#like i want to get this but its been bugging me that i cant
def sum_odd_numbers():
    print 