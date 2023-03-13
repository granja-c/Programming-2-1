from Cl213f import Utilities

def main():
  try:
    with open("data/prog213f.dat", 'r') as f:
      for line in f:
        kw = int(line)
        if kw > 0:
          bill = Utilities(kw)
          bill.calc()
          print(str(bill))

  except Exception as e:
    print("Error:", e)
  pass

if __name__ == "__main__":
  main()