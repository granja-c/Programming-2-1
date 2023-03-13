from Cl213b import Order
def main():
  print("Quantity\tPrice\tTotal")
  try:
    with open("data/prog213b.dat", 'r') as f:
      for line in f:
        amt = int(line)

        bill = Order(amt)
        bill.setPrice()
        bill.calcTot()
        print(str(bill))

  except Exception as e:
    print("Error:", e)
  pass

if __name__ == "__main__":
  main()