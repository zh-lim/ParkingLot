import unittest
from app.carpark import Carpark
from app.car import Car

class TestForCarpark(unittest.TestCase):

  def setUp(self):
    self.carpark = Carpark()

  def test_createParkingLots_method_returns_correct(self):
    res = self.carpark.createParkingLots(4)
    self.assertEqual(4,res)

  def test_createParkingLots_method_returns_negvalue_already_exist(self):
    self.carpark.createParkingLots(4)
    res = self.carpark.createParkingLots(2)
    self.assertEquals(-1,res)

  def test_createParkingLots_method_returns_error_input_type(self):
    self.assertRaises(TypeError,self.carpark.createParkingLots,"four")

  def test_parkCar_method_returns_correct(self):
    self.carpark.createParkingLots(2)
    car = Car("KA-01-HH-9988", "Blue")
    res = self.carpark.parkCar(car)
    self.assertEqual(1,res)

if __name__ == '__main__':
  unittest.main()
