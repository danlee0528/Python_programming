# *name: receives a tuple containing the positional arguments; must occur before **name
# **name: receives a dictionary containing all keyword arguments except for those corresponding to a formal parameter

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)

    for arg in arguments:
        print(arg)
    print("-" * 40)
    
    for kw in keywords:
        print(kw, ":", keywords[kw])


cheeseshop(
    "Limburger", "It's very runny, sir.",
    "It's really very, VERY runny, sir.",
    shopkeeper = "Michael Palin",
    client = "John Cleese",
    sketch = "Cheese Shop Sketch"
)


