class Car:
  # Assumes that all register numbers and colours are valid
  def __init__(self,regno,colour):
    self.__regno = str(regno)
    self.__colour = str(colour)

  def getRegNo(self):
    return self.__regno

  def getColour(self):
    return self.__colour