# Abstraction: Data hiding (hiding complex proccess from the user and only showing the necessary things)

class Bike:
   key = False
   clutch = False
   acc = False
   
   def start(self):
      self.key=True
      self.clutch = True
      self.acc = True
      print("Bike started")


b1 = Bike()
b1.start()