from app.carparkInterface import CarparkInterface
from app.car import Car

class CarparkDisplay:
  def __init__(self):
    self.__interface = CarparkInterface()

  def validate_input(self,inputs,type):
    if len(inputs) > 1:
      if type == 1: # check if inputs[1] exists and type is integer
        if (inputs[1].isnumeric()):
          return True
      if type == 2: # check if inputs has 3 arguments
        if len(inputs) > 2:
          return True
    return False

  def parse_action(self,inputs):
    if inputs[0] == "exit":
      return

    elif inputs[0] == "create_parking_lot":
      if self.validate_input(inputs,1):
        res = self.__interface.create_parking_lots(int(inputs[1]))
        if res > 0:
          return "Created a parking lot with " + str(res) + " slots"
        else:
          return "Parking lot already exists"

    elif inputs[0] == "park":
      if self.validate_input(inputs,2):
        car = Car(inputs[1],inputs[2])
        res = self.__interface.park_car(car)
        if res > 0:
          return "Allocated slot number: " + str(res)
        else:
          return "Sorry, parking lot is full"

    elif inputs[0] == "leave":
      if self.validate_input(inputs,1):
        res = self.__interface.leave_car(int(inputs[1]))
        if res:
          return "Slot number " + inputs[1] + " is free"
        else:
          return "No such slot number in parking lot"

    elif inputs[0] == "status":
      print("Slot No.".ljust(12) + "Registration No".ljust(19) + "Colour")
      res = self.__interface.print_status()
      for line in res:
        print(line)
      return

    elif inputs[0] == "registration_numbers_for_cars_with_colour":
      res = self.__interface.get_regNum_for_colour(inputs[1])
      if len(res) == 0:
        return "Not Found"

      printStr = (",").join(res)
      return printStr

    elif inputs[0] == "slot_numbers_for_cars_with_colour":
      res = self.__interface.get_slotNum_for_colour(inputs[1])
      if len(res) == 0:
        return "Not Found"

      printStr = (",").join(res)
      return printStr

    elif inputs[0] == "slot_number_for_registration_number":
      res = self.__interface.get_slotNum_for_regNum(inputs[1])
      if res > 0:
        return str(res)
      return "Not found"

    return "Invalid Input! Please check your input and try your command again."
