import unittest
from app.carpark import Carpark
from app.car import Car

class TestForCarpark(unittest.TestCase):

  def setUp(self):
    self.carpark = Carpark()

  def test_createParkingLots_method_returns_correct(self):
    res = self.carpark.createParkingLots(4)
    self.assertEqual(4,res)

  def test_createParkingLots_method_returns_error_input_type(self):
    self.assertRaises(TypeError,self.carpark.createParkingLots,"four")

  def test_parkCar_method_returns_correct(self):
    self.carpark.createParkingLots(2)
    car = Car("KA-01-HH-9988", "Blue")
    res = self.carpark.parkCar(car)
    self.assertEqual(1,res)

  def test_parkCar_method_returns_negOne_carpark_full(self):
    self.carpark.createParkingLots(2)
    car1 = Car("KA-01-HH-1234", "Red")
    car2 = Car("KA-01-HH-1235", "Gray")
    car3 = Car("KA-01-HH-1236", "Blue")
    self.carpark.parkCar(car1)
    self.carpark.parkCar(car2)
    res = self.carpark.parkCar(car3)
    self.assertEqual(-1,res)

  def test_parkCar_method_returns_negOne_carpark_not_created(self):
    car3 = Car("KA-01-HH-1236", "Blue")
    res = self.carpark.parkCar(car3)
    self.assertEqual(-1,res)

  def test_leave_method_returns_correct(self):
    self.carpark.createParkingLots(2)
    car1 = Car("KA-01-HH-1234", "Red")
    car2 = Car("KA-01-HH-1235", "Gray")
    self.carpark.parkCar(car1)
    self.carpark.parkCar(car2)
    res = self.carpark.leave(2)
    self.assertEqual(True,res)

if __name__ == '__main__':
  unittest.main()
