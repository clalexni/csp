import unittest
from varint import Varint

class TestVarint(unittest.TestCase):
  def test_encode(self):
    self.assertEqual(Varint.encode(150), b'\x96\x01')
  
  def test_decode(self):
    encoded_val = Varint.encode(150)
    self.assertEqual(Varint.decode(encoded_val), 150)

if __name__ == '__main__':
  unittest.main()