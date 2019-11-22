import unittest
from app.carparkInterface import CarparkInterface
from app.car import Car

class TestForCarparkInterface(unittest.TestCase):
  def setUp(self):
    self.interface = CarparkInterface()

  def test_create_parking_lots_method_returns_success(self):
    res = self.interface.create_parking_lots(2)
    self.assertEqual(2,res)

  def test_create_parking_lots_method_returns_already_exist(self):
    self.interface.create_parking_lots(4)
    res = self.interface.create_parking_lots(2)
    self.assertEqual(-1,res)

  def test_park_car_method_returns_correct(self):
    self.interface.create_parking_lots(2)
    car = Car("KA-01-HH-9988", "Blue")
    res = self.interface.park_car(car)
    self.assertEqual(1,res)

  def test_park_car_method_returns_carpark_full(self):
    self.interface.create_parking_lots(2)
    car1 = Car("KA-01-HH-1234", "Red")
    car2 = Car("KA-01-HH-1235", "Gray")
    car3 = Car("KA-01-HH-1236", "Blue")
    self.interface.park_car(car1)
    self.interface.park_car(car2)
    res = self.interface.park_car(car3)
    self.assertEqual(-1,res)

  def test_park_car_method_returns_no_parking_lots(self):
    car1 = Car("KA-01-HH-1234", "Red")
    res = self.interface.park_car(car1)
    self.assertEqual(-1,res)

  def test_leave_car_method_returns_correct(self):
    self.interface.create_parking_lots(2)
    car1 = Car("KA-01-HH-1234", "Red")
    car2 = Car("KA-01-HH-1235", "Gray")
    self.interface.park_car(car1)
    self.interface.park_car(car2)
    res = self.interface.leave_car(2)
    self.assertEqual(True,res)

  def test_leave_car_method_returns_fail_slotnum_greater_than_number_of_lots(self):
    self.interface.create_parking_lots(2)
    car1 = Car("KA-01-HH-1234", "Red")
    car2 = Car("KA-01-HH-1235", "Gray")
    self.interface.park_car(car1)
    self.interface.park_car(car2)
    res = self.interface.leave_car(3)
    self.assertEqual(False,res)

  def test_status_returns_array_with_filled_slots(self):
    self.interface.create_parking_lots(2)
    car1 = Car("KA-01-HH-1234", "Red")
    car2 = Car("KA-01-HH-1235", "Gray")
    self.interface.park_car(car1)
    self.interface.park_car(car2)
    res = self.interface.print_status()
    self.assertEqual(["1           KA-01-HH-1234      Red","2           KA-01-HH-1235      Gray"],res)

  def test_status_returns_empty_array_carpark_empty(self):
    self.interface.create_parking_lots(2)
    res = self.interface.print_status()
    self.assertEqual([],res)

  def test_status_returns_empty_array_no_carpark(self):
    res = self.interface.print_status()
    self.assertEqual([],res)

  def test_get_regNum_for_colour_method_returns_correct(self):
    self.interface.create_parking_lots(3)
    car1 = Car("KA-01-HH-1234", "Red")
    car2 = Car("KA-01-HH-1235", "Gray")
    car3 = Car("KA-01-HH-1237", "Gray")
    self.interface.park_car(car1)
    self.interface.park_car(car2)
    self.interface.park_car(car3)
    res = self.interface.get_regNum_for_colour("gray")
    self.assertEqual(["KA-01-HH-1235", "KA-01-HH-1237"],res)

  def test_get_regNum_for_colour_method_returns_not_found(self):
    self.interface.create_parking_lots(3)
    car1 = Car("KA-01-HH-1234", "Red")
    car2 = Car("KA-01-HH-1235", "Gray")
    car3 = Car("KA-01-HH-1237", "Gray")
    self.interface.park_car(car1)
    self.interface.park_car(car2)
    self.interface.park_car(car3)
    res = self.interface.get_regNum_for_colour("black")
    self.assertEqual([],res)

  def test_get_slotNum_for_colour_method_returns_correct(self):
    self.interface.create_parking_lots(3)
    car1 = Car("KA-01-HH-1234", "Red")
    car2 = Car("KA-01-HH-1235", "Gray")
    car3 = Car("KA-01-HH-1237", "Gray")
    self.interface.park_car(car1)
    self.interface.park_car(car2)
    self.interface.park_car(car3)
    res = self.interface.get_slotNum_for_colour("gray")
    self.assertEqual(["2", "3"],res)

  def test_get_slotNum_for_colour_method_returns_not_found(self):
    self.interface.create_parking_lots(3)
    car1 = Car("KA-01-HH-1234", "Red")
    car2 = Car("KA-01-HH-1235", "Gray")
    car3 = Car("KA-01-HH-1237", "Gray")
    self.interface.park_car(car1)
    self.interface.park_car(car2)
    self.interface.park_car(car3)
    res = self.interface.get_slotNum_for_colour("black")
    self.assertEqual([],res)

  def test_get_slotNum_for_regNum_method_returns_correct_slotNo(self):
    self.interface.create_parking_lots(3)
    car1 = Car("KA-01-HH-1234", "Red")
    car2 = Car("KA-01-HH-1235", "Gray")
    car3 = Car("KA-01-HH-1237", "Gray")
    self.interface.park_car(car1)
    self.interface.park_car(car2)
    self.interface.park_car(car3)
    res = self.interface.get_slotNum_for_regNum("KA-01-HH-1237")
    self.assertEqual(3,res)

  def test_get_slotNum_for_regNum_method_returns_not_found(self):
    self.interface.create_parking_lots(3)
    car1 = Car("KA-01-HH-1234", "Red")
    car2 = Car("KA-01-HH-1235", "Gray")
    car3 = Car("KA-01-HH-1237", "Gray")
    self.interface.park_car(car1)
    self.interface.park_car(car2)
    self.interface.park_car(car3)
    res = self.interface.get_slotNum_for_regNum("KA-01-HH-1232")
    self.assertEqual(-1,res)

if __name__ == '__main__':
  unittest.main()