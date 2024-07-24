my_dict = {'Anna': 1991, 'Alisa': 1995, 'Olga': 1998}
print(my_dict)
print('Existing value:',my_dict['Anna'])
print('Not existing value:',my_dict.get('Ivan'))
(my_dict)['Tanya'] = 1990
(my_dict)['Sofia'] = 1994
del my_dict['Alisa']
print('Modified dictionary:', my_dict)
#
my_set = {1, 2, 3, 5, 8, 2, 1, 'Vlada', True, (7, 8, 9)}
print(my_set)
my_set.discard(2)
my_set.add(0)
print(my_set)
