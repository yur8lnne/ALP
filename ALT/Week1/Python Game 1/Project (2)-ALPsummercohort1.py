# Players have to guess the correct number within 7 attempts
from random import randrange

num = randrange(101)
cnt = 0
guess = 0
name = input("Enter your name: ")

while guess != num:
  cnt += 1
  guess = int(input("Guess a number between 1 and 100: "))
  if guess > num:
    print("Too high!")
  elif guess < num:
    print("Too low!")

print("Congratulations, "+name+" You guessed the secret number in "+str(cnt)+" guesses.")