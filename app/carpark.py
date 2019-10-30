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
