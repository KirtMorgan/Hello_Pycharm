def dough(water, wheat):
    # print(f'Mixing {water} with {wheat}')
    if water == 'water' and wheat == 'wheat':
        return'dough'
    else:
        return'Blob of mixture'

# TDD
# output = (dough('water', 'wheat') == 'dough')
# print(dough('water', 'wheat') == 'dough')

def bake(substance):
    if substance == 'dough':
        return'bread'
    else:
        return'not bread'
# TDD
print(bake('dough')=='bread')

def bread_factory(substance_1, substance_2):
    output_dough = dough(substance_1, substance_2)
    return bake(output_dough)

# Test
# These tests will test the bread factory as a whole
print('testing the factory with water and wheat - expect output to be bread')
print(bread_factory('water', 'wheat') =='bread')
print(bread_factory('water', 'wheat'))

print('testing the factory with water and cement - expect output to be not bread')
print(bread_factory('water', 'cement') =='bread')
print(bread_factory('water', 'cement'))
