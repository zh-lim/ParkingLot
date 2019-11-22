from app.carpark import Carpark

class CarparkInterface:
  def __init__(self):
    self.__carpark = Carpark()

  def create_parking_lots(self,numlots):
    parkingLots = self.__carpark.getParkingLots()
    numLots = -1
    if parkingLots is None:
      numLots = self.__carpark.createParkingLots(numlots)
    return numLots

  def park_car(self,car):
    parkingLots = self.__carpark.getParkingLots()
    numLots = self.__carpark.getNumLots()
    slotNum = -1
    if parkingLots is not None:
      slotNum = self.__carpark.parkCar(car)
    return slotNum

  def leave_car(self,slotNum):
    parkingLots = self.__carpark.getParkingLots()
    numLots = self.__carpark.getNumLots()
    left = False
    if type(slotNum) == int and slotNum <= numLots and parkingLots is not None:
      left = self.__carpark.leave(slotNum)
    return left

  def print_status(self):
    parkingLots = self.__carpark.getParkingLots()
    numLots = self.__carpark.getNumLots()
    printStr = []
    if parkingLots is None:
      return printStr
    for i in range(1,numLots+1):
      if parkingLots[i] != None:
        printStr.append(str(i).ljust(12) + parkingLots[i].getRegNo().ljust(19) + parkingLots[i].getColour())
    return printStr

  def get_regNum_for_colour(self,colour):
    parkingLots = self.__carpark.getParkingLots()
    numLots = self.__carpark.getNumLots()
    regArray = []
    if parkingLots is None:
      return regArray
    
    for i in range(1,numLots+1):
      if parkingLots[i] != None:
        if parkingLots[i].getColour().upper() == colour.upper():
          regArray.append(parkingLots[i].getRegNo())
    
    return regArray

  def get_slotNum_for_colour(self,colour):
    parkingLots = self.__carpark.getParkingLots()
    numLots = self.__carpark.getNumLots()
    slotArray = []
    if parkingLots is None:
      return slotArray
    
    for i in range(1,numLots+1):
      if parkingLots[i] != None:
        if parkingLots[i].getColour().upper() == colour.upper():
          slotArray.append(str(i))
    
    return slotArray

  def get_slotNum_for_regNum(self,regno):
    parkingLots = self.__carpark.getParkingLots()
    numLots = self.__carpark.getNumLots()
    slotNum = -1
    if parkingLots is None:
      return slotNum
    
    for i in range(1,numLots+1):
      if parkingLots[i] != None:
        if parkingLots[i].getRegNo().upper() == str(regno).upper():
          slotNum = i
          break
    
    return slotNum
