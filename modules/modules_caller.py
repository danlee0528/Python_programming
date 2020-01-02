from fibo import fib, fib2 as fib3
import sys

fib(1000)
print(fib3(1000))


# find out which names a module defines
print("dir():", dir())
print("dir(fib):", dir(fib))
print("dir(sys):", dir(sys))