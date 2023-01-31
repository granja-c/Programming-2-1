import random
guess = int(input("Enter a number between 1 and 20: "))
secret = random.randint(1, 21)
print("Computer's Number: ", str(secret))
print("Player's Number: ", str(guess))

if guess == secret:
  print("You won!")
else:
  print("Better luck next time.")