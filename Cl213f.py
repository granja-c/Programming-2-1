class Utilities:
  def __init__(self, kw):
    self.kw = kw
    self.tot = 0
  
  def calc(self):
    if self.kw > 0 and self.kw <= 2000:
      self.tot = self.kw * 0.07
    elif self.kw > 2000 and self.kw <= 10000:
      self.tot = 2000 * 0.07 + (self.kw - 2000) * 0.05
    elif self.kw > 10000:
      self.tot = self.kw * 0.04

  def __str__(self):
    return f"The cost of {self.kw} is ${round(self.tot, 2)}"