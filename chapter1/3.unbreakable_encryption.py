# 1.3 Unbreakable encryption
from secrets import token_bytes

def random_key(length: int) -> int:
  # generate `length` random bytes
  tb: bytes = token_bytes(length)
  # convert those bytes into a bit string and return it
  return int.from_bytes(tb, 'big')
