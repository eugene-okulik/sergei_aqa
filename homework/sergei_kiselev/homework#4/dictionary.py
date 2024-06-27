my_dict = {
    'tuple': (1, None, 'three', False, 5.5),
    'list': [0.5, 1, None, True, 'four'],
    'dict': {1: 'am', False: 'is', 2.43: 'is', 'You': 1, 'We': 0},
    'set': {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
}

print(my_dict['tuple'][-1])
(my_dict['list']).append('five')
my_dict['list'].pop(1)
my_dict['dict']['i am a tuple'] = {None, False, 777}
my_dict['dict'].pop(False, 'is')
my_dict['set'].add(6)
my_dict['set'].remove(1)


print(my_dict)
