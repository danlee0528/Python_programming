# Fibonacci numbers mmodule

def fib(n): # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):    # return Fibonacci series upto n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

# Code in the module will be executed as scripts and be used for testing purposes
# or as a convenient user interface to a module
# To call the module, "python fibo.py <arg>"
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))