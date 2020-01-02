t = 1234, 5678, 'hello!'
print(t[0])
print("tuple:", t)
u = t, (1,2,3,4,5,6)
print("nested tuple:", u)

#sequence unpacking
empty = ()
singleton = 'hello',    # a tuple with one imte is constructed by follwoing a value with a comma
print("empty tuple length:", len(empty))
print("tuple with one item length:", len(singleton))

print('\n' * 2)
print("=== Sets ===")
# A set is an unordered collection with no duplicate elements

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print("Set:", basket)
a = set('abracadabra')
b = set('alacazam')
print(a)        # print unique letters in a 
print(a - b)    # letters in a but not in b 
print(a | b)    # letters in a or b or both
print(a & b)    # letters in both a and b
print(a ^ b)    # letters in a or b but not both

print('\n' * 2)
print("=== Dictionaries ===")
# A set of key: value pairs
tel = {'jack': 4098, 'sape': 4139}
print("Dictionary:",tel)
tel_2 = dict([('jack', 4098), ('sape', 4139)])
print("Dictionary_2:", tel_2)
tel_3 = dict(jack=4098, sape=4139)
print("Dictionary_3:", tel_3)

# When looping through dictionaries
# return the key and corresponding value
print("Printing key and value pairs")
for k, v in tel.items():
    print(k, v)

# when looping through a sequence
# return position index and corresponding value
print("Printing Indexes with corresponding values")
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# when looping over two or more sequences at the same time
# reutrn paired entries
questions = ['name', 'quest', 'favourite colour']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}? It is {1}.'.format(q,a))

