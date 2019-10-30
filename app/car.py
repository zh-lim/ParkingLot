class Car:
  # Assumes that all register numbers and colours are valid
  def __init__(self,regno,colour):
    self.__regno = regno
    self.__colour = colour

  def getRegNo(self):
    return self.__regno

  def getColour(self):
    return self.__colour