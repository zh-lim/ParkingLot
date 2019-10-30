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
    self.__parkingLots = {}
    for i in range(1,num_lots+1):
      self.__parkingLots[i] = ""

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

  def leave(self,lotnum):
    res = -1
    if self.__parkingLots is not None:
      res = self.__rmCar(lotnum)
    return res

  # function to remove car from indicated slot, 
  # returns slot number if slot is already empty or is being emptied
  # otherwise return -1
  def __rmCar(self,lotnum):
    if lotnum > self.__numLots:
      return -1
    self.__parkingLots[lotnum] = ""
    return lotnum

  def printStatus(self):
    print("Slot No.".ljust(10) + "Registration No".ljust(20) + "Colour".ljust(10))
    if self.__parkingLots is None:
      return
    for i in range(1,self.__numLots+1):
      if self.__parkingLots[i] != "":
        print(str(i).ljust(10) + self.__parkingLots[i].getRegNo().ljust(20) + self.__parkingLots[i].getColour().ljust(10))
    return


