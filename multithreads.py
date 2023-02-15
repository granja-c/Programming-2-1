import time
import threading as th
def print_nums(start, end, delay):
  for i in range(start, end):
    time.sleep(delay)
    print(i, " ")

def print_lets(delay):
  for letter in "abcdefghi":
    time.sleep(delay)
    print(letter)

t1 = th.Thread(target=print_nums, args)