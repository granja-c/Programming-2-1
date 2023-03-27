def fact(n):
  if n == 1:
    return n
  return n * fact(n - 1)

def main():
  num = int(input('Enter a number: '))
  while num != 0:
    factn = fact(num)
    print(f"The value of {num}! is {factn}")
    num = int(input('Enter a number: '))
    pass
    
  pass

if __name__ == "__main__":
  main()