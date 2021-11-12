# 1.1 The Fibonacci sequence
from functools import lru_cache

# lru_cache causes the return of fib function
# to be cached every time it's called

@lru_cache(maxsize=None)
def fib(n: int) -> int:
  # base case
  if n < 2:
    return n
  # recursive case
  return fib(n - 1) + fib(n - 2)

# test
if __name__ == '__main__':
  print(fib(5))
  print(fib(50))
