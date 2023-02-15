def calcRadius(diam):
  r = diam / 2.0
  return r

def calcCirc(r):
  pi = 3.14159
  circ = 2 * pi * r
  return circ

def calcArea(r):
  pi = 3.14159
  area = pi * r ** 2
  return area

def main():
  d = int(input("Enter the diameter: "))
  r = calcRadius(d)
  c = calcCirc(r)
  a = calcArea(r)

  print(f"Radius: {r}\nCircumference: {round(c, 3)}\nArea: {round(a, 3)}")

  pass

if __name__ == "__main__":
  main()