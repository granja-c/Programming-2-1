class Shape:
  def __init__(self, leng, wid):
    self.leng = leng
    self.wid = wid
    self._area = 0
    self._perim =  0

  def calc(self):
    self._area = self.leng * self.wid
    self._perim = self.leng * 2 + self.wid * 2

  def getArea(self):
    return self._area

  def getPerim(self):
    return self._perim

def main():
  len = int(input("Enter length: "))
  wid = int(input("Enter width: "))
  shape = Shape(len, wid)
  shape.calc()
  print("Area:", shape.getArea())
  print("Perimeter:", shape.getPerim())

if __name__ == "__main__":
  main()