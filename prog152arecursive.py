import sys
sys.setrecursionlimit(5000)

def sum3(n):
  if n == 3:
    return n
  return n + sum3(n - 3)
  
def main():
  n = int(input("Enter a number: "))
  summ = sum3(n)
  print(f"The sum of the multiples of 3, from 3 to {n}, is {summ}")
  pass

if __name__ == "__main__":
  main()