from Cl213e import Family

def main():
  try:
    with open("data/prog213e.dat", 'r') as f:
      tot = int(f.readline())
      a = 0
      b = 0
      c = 0
      d = 0
      e = 0
      num = 0
      age = 0
      while num != tot:
        age = int(f.readline())
        if age < 20:
          a += 1
        elif age >= 20 and age <= 39:
          b += 1
        elif age >= 40 and age <= 59:
          c += 1
        elif age >= 60 and age <= 79:
          d += 1
        elif age > 79:
          e += 1
        num += 1
      fam = Family(tot, a, b, c, d, e)
      fam.calc()
      print(str(fam))
  except Exception as e:
    print("Error:", e)
  pass

if __name__ == "__main__":
  main()