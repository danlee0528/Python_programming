'''
- Small anonymous functions can be created with the "lambda" keyword.
- This function returns the sume of its two argumentS: lambda a, b: a+b.
'''

def make_incrementor(n):
    return lambda x: x + n


f = make_incrementor(42)
print(f(0))
print(f(1)) 