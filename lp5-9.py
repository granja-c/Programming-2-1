def main():
  print("x^1\t\t x^2\t\t x^3\t\t x^4\t\t x^5")

  for lcv in range(1, 7):
    lcv2 = lcv ** 2
    lcv3 = lcv ** 3
    lcv4 = lcv ** 4
    lcv5 = lcv ** 5
    print(f"{lcv}\t {lcv2}\t {lcv3}\t {lcv4}\t {lcv5}")
  pass

if __name__ == "__main__":
  main()