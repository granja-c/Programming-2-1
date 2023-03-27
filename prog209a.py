from Cl209a import Counting
def main():
  try:
    with open("data/prog215a.dat", 'r') as f:
      more = 0
      less = 0
      cnt = 0
      for line in f:
        num = int(f.readline())
        if num < 500:
          less += 1
        elif num >= 500:
          more += 1
        cnt += 1
      a = Counting(more, less, cnt)
      print(str(a))
        

  except Exception as e:
    print("Error:", e)
  pass

if __name__ == "__main__":
  main()