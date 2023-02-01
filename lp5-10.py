def main():
  num1 = int(input("Enter a number: "))
  num2 = int(input("Enter a second number: "))
  temp = 0

  while num2 > 0:
    temp = num2
    num2 = num1 % num2
    num1 = temp

  print("The GCD is", str(temp))
  pass

if __name__ == "__main__":
  main()