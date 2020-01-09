def allFib(n):
  memo = [x for x in range(0, n+1)]
  for i in range(n):
    print(i + ": " + fib(i, memo))
    
'''
At each call to fib(i), we have already computed and stored the values for fib(i-1) and fib(i-2).
We just look up those values, sum them, store the new result, and return.
This takes a constant amount of time; O(n) time
This optimizes exponential time recurisve algorithms, namely, "memoization"
'''
def fib(n, *memo):
  if (n <= 0) return 0
  elif (n ==1 ) return 1
  elif (memo[n] > 0) return memo[n]
  
  memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
  return memo[n]
  
