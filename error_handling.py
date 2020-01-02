try:
    raise NameError('custom error')
except NameError: 
    print('An exception triggered!')
    raise       # force a specified exception to occur
else:   # executed if the try caluse doesn't raise an exception
    print('no exception rasied')
finally:
    print('This line is the end of testing, bye!')