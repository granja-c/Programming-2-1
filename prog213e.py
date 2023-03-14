from Cl213e import *

def main():
  try:
    with open("data/prog213e.dat", 'r') as f:
      for line in f:
        age = line

  except Exception as e:
    print("Error:", e)
  pass

if __name__ == "__main__":
  main()