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