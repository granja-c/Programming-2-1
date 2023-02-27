class lp311:
  def __init__(self, des, cod, deb, tes):
    self.des = des
    self.cod = cod
    self.deb = deb
    self.tes = tes
    self.tot = 0
    self.percents = [0]*4

  def percent(self, number):
    return round((number / self.tot) * 100, 2)

  def calc(self):
    self.tot = self.des + self.cod + self.deb + self.tes
    self.percents[0] = self.percent(self.des)
    self.percents[1] = self.percent(self.cod)
    self.percents[2] = self.percent(self.deb)
    self.percents[3] = self.percent(self.tes)

  def disp(self):
    print("Task\t\t% Time")
    print(f"Designing\t{self.percents[0]}%")
    print(f"Coding\t\t{self.percents[1]}%")
    print(f"Debugging\t{self.percents[2]}%")
    print(f"Testing\t\t{self.percents[3]}%")

def main():
  print("Enter the amount of time spent on the following task:\n")
  des = int(input("Designing: "))
  cod = int(input("Coding: "))
  deb = int(input("Debugging: "))
  tes = int(input("Testing: "))

  time = lp311(des, cod, deb, tes)
  time.calc()
  time.disp()
  pass

if __name__ == "__main__":
  main()