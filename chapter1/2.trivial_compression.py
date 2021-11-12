# 1.2 Trivial compression

class CompressGene:
  def __init__(self, gene: str) -> None:
    self._compress(gene)
  def _compress(self, gene: str) -> None:
    self.bit_string: int = 1 # start with sentinel
    for nucleotide in gene.upper():
      self.bit_string <<= 2 # shift left 2 bits
      if nucleotide == 'A':
        self.bit_string |= 0b00
      elif nucleotide == 'C':
        self.bit_string |= 0b01
      elif nucleotide == 'G':
        self.bit_string |= 0b10
      elif nucleotide == 'T':
        self.bit_string |= 0b11
      else:
        raise ValueError(f'Invalid Nucleotide:{nucleotide}')

  def _decompress(self) -> str:
    gene: str = ''
    # - 1 to exclude the sentinel
    for i in range(0, self.bit_string.bit_length() - 1, 2):
      # get just the 2 relevant bits
      bits: int = self.bit_string >> i & 0b11
      if bits == 0b00:
        gene += 'A'
      elif bits == 0b01:
        gene += 'C'
      elif bits == 0b10:
        gene += 'G'
      elif bits == 0b11:
        gene += 'T'
      else:
        raise ValueError(f'Invalid bits:{bits}')
    return gene[::-1] # reverse string

  def __str__(self) -> str:
    return self._decompress()


# test
if __name__ == '__main__':
  from sys import getsizeof
  original: str = (
      'TAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATATAGGGATTAACCGTTATATATATATAGC'
      'CATGGATCGATTATA'
    ) * 100
  print(f'Original is {getsizeof(original)} bytes') # 8649 bytes

  compressed: CompressGene = CompressGene(original)
  print(f'Compressed is {getsizeof(compressed.bit_string)} bytes') # 2320 bytes

  # check if original == compressed
  print('Original and decompressed are ',
    f'the same [{original == compressed._decompress()}]') # True

