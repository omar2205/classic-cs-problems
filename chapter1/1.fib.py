# 1.1 The Fibonacci sequence
from typing import Dict

# base case
memo: Dict[int, int] = {0: 0, 1: 1}

def fib(n: int) -> int:
  if n not in memo:
    # memoization
    memo[n] = fib(n - 1) + fib(n - 2)
  return memo[n]

# test
if __name__ == '__main__':
  print(fib(5))
  print(fib(50))
