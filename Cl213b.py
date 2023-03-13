class Order:
  def __init__(self, amt):
    self.amt = amt
    self.price = 0
    self.tot = 0
    
  def setPrice(self):
    if self.amt > 0 and self.amt <= 99:
      self.price = 5.95
    elif self.amt > 99 and self.amt <= 199:
      self.price = 5.75
    elif self.amt > 199 and self.amt <= 299:
      self.price = 5.40
    elif self.amt >= 300:
      self.price = 5.15

  def calcTot(self):
    self.tot = self.amt * self.price

  def __str__(self):
    return f"{self.amt}\t\t\t{self.price}\t{round(self.tot, 2)}"