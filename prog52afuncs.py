def calcArea(length, width):
  return length * width

def calcPerim(length, width):
  return length * 2 + width * 2

def areaPerim(length, width):
  area = calcArea(length, width)
  perim = calcPerim(length, width)
  return area, perim

def main():
  length = int(input("Enter length: "))
  width = int(input("Enter width: "))
  a, p = areaPerim(length, width)
  print(f"Area: {a}\nPerim: {p}")

if __name__ == "__main__":
  main()