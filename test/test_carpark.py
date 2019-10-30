import unittest
from app.carpark import Carpark

class TestForCarpark(unittest.TestCase):

  def setUp(self):
    self.carpark = Carpark()

  def test_createParkingLots_method_returns_correct(self):
    res = self.carpark.createParkingLots(4)
    self.assertEqual("Created a parking lot with 4 slots",res)

  def test_createParkingLots_method_returns_error(self):
    self.assertRaises(TypeError,self.carpark.createParkingLots,"four")

if __name__ == '__main__':
  unittest.main()
