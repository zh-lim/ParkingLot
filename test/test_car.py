import unittest
from app.car import Car

class TestForCar(unittest.TestCase):
  def test_carCreation_correct_regno(self):
    car = Car("KA-01-HH-9980", "Black")
    res = car.getRegNo()
    self.assertEquals("KA-01-HH-9980",res)

  def test_carCreation_correct_colour(self):
    car = Car("KA-01-HH-9980", "Black")
    res = car.getColour()
    self.assertEquals("Black",res)

  def test_carCreation_error(self):
    self.assertRaises(TypeError,Car,"KA-01-HH-9980")