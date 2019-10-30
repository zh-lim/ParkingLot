class Carpark:
  def __init__(self):
    self.__parkingLots = None
    self.__numLots = 0

  def getNumLots(self):
    return self.__numLots

  def getParkingLots(self):
    return self.__parkingLots

  def createParkingLots(self,num_lots):
    self.__numLots = num_lots
    self.__createSlots(self.__numLots)
    return self.__numLots

  def __createSlots(self,num_lots):
    self.__parkingLots = {}
    for i in range(1,num_lots+1):
      self.__parkingLots[i] = None

  def parkCar(self,car):
    lotnum = self.__allocCar(car)
    return lotnum

  def __allocCar(self,car):
    lotnum = -1
    for i in range(1,self.__numLots+1):
      if self.__parkingLots[i] == None:
        self.__parkingLots[i] = car
        lotnum = i
        break
    return lotnum

  def leave(self,lotnum):
    res = self.__rmCar(lotnum)
    return res

  # function to remove car from indicated slot, 
  # returns slot number if slot is already empty or is being emptied
  # otherwise return -1
  def __rmCar(self,lotnum):
    self.__parkingLots[lotnum] = None
    return True

  # def getRegNoForColour(self,colour):
  #   regArray = []
  #   for i in range(1,self.__numLots+1):
  #     if self.__parkingLots[i] != None:
  #       if self.__parkingLots[i].getColour().upper() == colour.upper():
  #         regArray.append(self.__parkingLots[i].getRegNo())
  #   return regArray

  # def getSlotNoForColour(self,colour):
  #   slotArray = []
  #   for i in range(1,self.__numLots+1):
  #     if self.__parkingLots[i] != None:
  #       if self.__parkingLots[i].getColour().upper() == colour.upper():
  #         slotArray.append(str(i))
  #   return slotArray

  # def getSlotNoForRegNo(self,regno):
  #   slotNum = -1
  #   for i in range(1,self.__numLots+1):
  #     if self.__parkingLots[i] != None:
  #       if self.__parkingLots[i].getRegNo().upper() == regno.upper():
  #         slotNum = i
  #         break
  #   return slotNum