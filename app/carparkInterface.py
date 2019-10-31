from app.carpark import Carpark
from app.car import Car

class CarparkInterface:
  def __init__(self):
    self.__carpark = Carpark()

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
        res = self.create_parking_lots(int(inputs[1]))
        return res
    elif inputs[0] == "park":
      if self.validate_input(inputs,2):
        car = Car(inputs[1],inputs[2])
        res = self.park_car(car)
        return res
    elif inputs[0] == "leave":
      if self.validate_input(inputs,1):
        res = self.leave_car(int(inputs[1]))
        return res
    elif inputs[0] == "status":
      res = self.print_status()
      return
    elif inputs[0] == "registration_numbers_for_cars_with_colour":
      res = self.get_regNum_for_colour(inputs[1])
      return res
    elif inputs[0] == "slot_numbers_for_cars_with_colour":
      res = self.get_slotNum_for_colour(inputs[1])
      return res
    elif inputs[0] == "slot_number_for_registration_number":
      res = self.get_slotNum_for_regNum(inputs[1])
      return res
    return "Invalid Input! Please check your input and try your command again."

  def create_parking_lots(self,numlots):
    parkingLots = self.__carpark.getParkingLots()
    if parkingLots is None:
      numLots = self.__carpark.createParkingLots(numlots)
      return "Created a parking lot with " + str(numLots) + " slots"
    else:
      return "Parking lot already exists"

  def park_car(self,car):
    parkingLots = self.__carpark.getParkingLots()
    numLots = self.__carpark.getNumLots()
    if parkingLots is not None:
      slotNum = self.__carpark.parkCar(car)
      if slotNum > 0:
        return "Allocated slot number: " + str(slotNum)
    return "Sorry, parking lot is full"

  def leave_car(self,slotNum):
    parkingLots = self.__carpark.getParkingLots()
    numLots = self.__carpark.getNumLots()
    left = False
    if type(slotNum) == int and slotNum <= numLots and parkingLots is not None:
      left = self.__carpark.leave(slotNum)
    if left == True:
      return "Slot number " + str(slotNum) + " is free"
    else:
      return "No such slot number in parking lot"

  def print_status(self):
    parkingLots = self.__carpark.getParkingLots()
    numLots = self.__carpark.getNumLots()
    print("Slot No.".ljust(10) + "Registration No".ljust(20) + "Colour".ljust(10))
    if parkingLots is None:
      return
    for i in range(1,numLots+1):
      if parkingLots[i] != None:
        print(str(i).ljust(10) + parkingLots[i].getRegNo().ljust(20) + parkingLots[i].getColour().ljust(10))
    return

  def get_regNum_for_colour(self,colour):
    parkingLots = self.__carpark.getParkingLots()
    numLots = self.__carpark.getNumLots()
    regArray = []
    if parkingLots is None:
      return "Not Found"
    
    for i in range(1,numLots+1):
      if parkingLots[i] != None:
        if parkingLots[i].getColour().upper() == colour.upper():
          regArray.append(parkingLots[i].getRegNo())
    
    if len(regArray) > 0:
      printStr = ""
      for regno in regArray:
        printStr = printStr + regno + ", "
      return printStr[:-2]
    else:
      return "Not Found"

  def get_slotNum_for_colour(self,colour):
    parkingLots = self.__carpark.getParkingLots()
    numLots = self.__carpark.getNumLots()
    slotArray = []
    if parkingLots is None:
      return "Not Found"
    
    for i in range(1,numLots+1):
      if parkingLots[i] != None:
        if parkingLots[i].getColour().upper() == colour.upper():
          slotArray.append(str(i))
    
    if len(slotArray) > 0:
      printStr = ""
      for slotno in slotArray:
        printStr = printStr + slotno + ", "
      return printStr[:-2]
    else:
      return "Not Found"

  def get_slotNum_for_regNum(self,regno):
    parkingLots = self.__carpark.getParkingLots()
    numLots = self.__carpark.getNumLots()
    if parkingLots is None:
      return "Not Found"
    
    slotNum = -1
    for i in range(1,numLots+1):
      if parkingLots[i] != None:
        if parkingLots[i].getRegNo().upper() == str(regno).upper():
          slotNum = i
          break
    
    if slotNum > 0:
      return str(slotNum)
    else:
      return "Not Found"
