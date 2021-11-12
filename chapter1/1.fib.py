# 1.1 The Fibonacci sequence

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

# test
if __name__ == '__main__':
  print(fib(5))
  print(fib(50))
  print(fib(150))
