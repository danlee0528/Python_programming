def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()       # variables live in an enclosing scope should be rebound there
                        # changed scope_test's binding of spam
    print("After nonlocal assignment:", spam)
    do_global()         # variables live in the global scope should be rebound there
                        # changed the module-level binding
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)