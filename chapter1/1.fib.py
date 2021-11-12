# 1.1 The Fibonacci sequence
from typing import Generator

def fib(n: int) -> int:
  # special case
  if n == 0: return n
  # setting initially to fib(0) and fib(1)
  last: int = 0
  next: int = 1
  
  for _ in range(1, n):
    # last = current next
    # next = prev last + current next
    last, next = next, last + next

  return next

def fib_generator(n: int) -> Generator[int, None, None]:
  """Output the entire Fibonacci sequence to n"""
  # special cases 0,1
  yield 0
  if n > 0: yield 1
  # same iterative methid as fib
  last: int = 0
  next: int = 1
  
  for _ in range(1, n):
    last, next = next, last + next
    yield next


# test
if __name__ == '__main__':
  print(fib(5))
  print(fib(50))
  print(fib(150))

  # test fib_generator
  for i in fib_generator(10):
    print(i)
