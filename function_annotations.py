"""
- Annotations are stored in the __annotations__ attribute of the function as a dictionary and have no effect on 
any other part of the function

- Return annotations are defined by a literal "->", followed by an expression, between the parameter
list and the colon denoting the end of the "def" statement
"""
def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

f('spam')