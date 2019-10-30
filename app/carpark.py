class Carpark:
  def __init__(self):
    self.__parkingLots = None
    self.__numLots = 0

  def createParkingLots(self,num_lots):
    if self.__parkingLots is None:
      self.__numLots = num_lots
      self.__createSlots(self.__numLots)
      return "Created a parking lot with " + str(self.__numLots) + " slots"
    else:
      return "Parking Lots already exists"

  def __createSlots(self,num_lots):
    slots = 1
    self.__parkingLots = {}
    for i in range(1,num_lots+1):
      self.__parkingLots[slots] = ""

  def getNumLots(self):
    return self.__numLots

