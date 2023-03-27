class Vehicles:
  def __init__(self, name, tires):
    self.name = name
    self.tires = tires
    
class Car(Vehicles):
  def __init__(self, name, tires, val):
    super().__init__(name, tires)
    self.val = val

class Truck(Vehicles):
  def __init__(self, name, tires, miles):
    super().__init__(name, tires)
    self.miles = miles
    self.val = 50000 - self.miles * 0.25

class Bus(Vehicles):
  def __init__(self, name, tires, home):
    super().__init__(name, tires)
    self.home = home
