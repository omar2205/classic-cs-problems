# 1.1 The Fibonacci sequence

def fib(n: int) -> int:
  # base case
  if n < 2:
    return n
  # recursive case
  return fib(n - 1) + fib(n - 2)

# test
if __name__ == '__main__':
  print(fib(5))
