class Carpark:
  def __init__(self):
    self.__parkingLots = None
    self.__numLots = 0

  def createParkingLots(self,num_lots):
    if self.__parkingLots is None:
      self.__numLots = num_lots
      self.__createSlots(self.__numLots)
      return self.__numLots
    else:
      return -1

  def getNumLots(self):
    return self.__numLots

  def __createSlots(self,num_lots):
    slots = 1
    self.__parkingLots = {}
    for i in range(1,num_lots+1):
      self.__parkingLots[slots] = ""

  def parkCar(self,car):
    lotnum = -1
    if self.__parkingLots is not None:
      lotnum = self.__allocCar(car)
    return lotnum

  def __allocCar(self,car):
    lotnum = -1
    for i in range(1,self.__numLots+1):
      if self.__parkingLots[i] == "":
        self.__parkingLots[i] = car
        lotnum = i
        break
    return lotnum