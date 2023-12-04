"""
base 128 varint
- encode unsigned 64 bit integer using 1 to 10 bytes
- first bit of each bit is the continuous bit
- 7 bits payload
- little-endian 
"""

class Varint:
  def encode(x: int) -> bytes:
    if x == 0:
      return b'\x00'
    out = []
    while x > 0:
      x, part = x // 128, x % 128
      if x > 0:
        part |= 0x80
      out.append(part)
    return bytes(out)

  def decode(x: bytes) -> int:
    result = 0
    for i in range(len(x)):
      has_next = x[i] >> 7 == 1
      payload = x[i] ^ 0x80 if has_next else x[i]
      result += payload * pow(128, i)
      if not has_next:
        break
    return result
  
test_cases = (
  ('1.uint64', b'\x01'),
  ('150.uint64', b'\x96\x01'),
  ('maxint.uint64', b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01')
)

def main() -> None:
  for fname, expected in test_cases:
    with open(fname, 'rb') as f:
      value = int.from_bytes(f.read(), byteorder='big')
      assert Varint.encode(value) == expected
      assert Varint.decode(Varint.encode(value)) == value
      f.close()
  print('Ok.')


if __name__ == '__main__':
  main()