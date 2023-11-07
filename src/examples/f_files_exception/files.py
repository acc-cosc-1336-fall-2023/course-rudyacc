from fileinput import filename


def write_city_list_file():
    cities = ['New York', 'Boston', 'Atlanta', 'Dallas']
    
    out_file = open(filename, 'w')
    for city in cities:
        out_file.write(city + '\n')
        
    out_file.close()
    
def read_city_list_file(file_name):
    in_file = open(file_name, 'r')
    cities = []
    
    for line in in_file:
        cities.append(line.rstrip('\n'))
        
    print(cities)
    

        