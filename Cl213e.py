class Family:
  def __init__(self, tot, a, b, c, d, e):
    self.tot = tot
    self.a = a
    self.b = b
    self.c = c
    self.d = d
    self.e = e

    self.a1 = 0.0
    self.b1 = 0.0
    self.c1 = 0.0
    self.d1 = 0.0
    self.e1 = 0.0
  def calc(self):
    self.a1 = self.a / self.tot * 100
    self.b1 = self.b / self.tot * 100
    self.c1 = self.c / self.tot * 100
    self.d1 = self.d / self.tot * 100
    self.e1 = self.e / self.tot * 100

  def __str__(self):
    return f"<20\t\t{self.a}\t{round(self.a1, 2)}\n20-39\t{self.b}\t{round(self.b1, 2)}\n40-59\t{self.c}\t{round(self.c1, 2)}\n60-79\t{self.d}\t{round(self.d1, 2)}\n>79\t\t{self.e}\t{round(self.e1, 2)}"
