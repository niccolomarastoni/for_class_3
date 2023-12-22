def descending_number_list(a, b, c):
    return list(range(b, a-1, -c))

def print_descending_number_list(a, b, c):
    print(descending_number_list(a, b, c))

def create_dictionary(list_of_keys, list_of_values):
    '''
    inputs: a list of keys and a list of values
    outputs: a dictionary with the input keys and values
    '''