class Complex:

    kind = 'canine'     # class variable shared by all instances

    def __init__(self, realpart, imagpart):     # iinvoked for the newly-created class instance
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
print(x.r, x.i)
print(x.kind)

class Complex1:

    val = '0'

    def __init__(self, key, val):
        self.key = key
        self.val = val

class Complex2(Complex, Complex1):
    
    kind = 'canone'
    __spam = 'private variable'

    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

    def get_spam(self):
        return self.__spam

x = Complex2(3.0, -4.5)
print(x.kind)
# print(x.__spam)     # return error
print(x.get_spam())