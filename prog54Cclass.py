# ik the assignment is lang54b but that has to do with sums and averages and the assignment description talks about circles soooo

class Circle:
  def __init__(self, diam):
    self.diam = diam
    self.rad = self.diam / 2.0
    self.PI = 3.14159
    self.area = 0
    self.circumf = 0

  def calc(self):
    self.area = round((self.PI * self.rad ** 2), 3)
    self.circumf = round((self.PI * self.rad * 2), 3)

  def getArea(self):
    return self.area

  def getCircumf(self):
    return self.circumf

  
def main():
  diam = int(input("Diameter: "))
  circ = Circle(diam)
  circ.calc()
  print("Area: ", circ.getArea())
  print("Circumference: ", circ.getCircumf())
  pass

if __name__ == "__main__":
  main()