number = 7
print("I'm thinking of a number, can you guess it?")
guess = int(input())
while guess != number:
  print("Wrong! Guess again!")
  guess = input()
print("You guessed it!")

# Give the line number where iteration starts.
  # Answer: line4

# What does '!=' mean?
  # Answer: not same

# How many variables are there in the code?
  # Answer: 2

# How can you tell which lines of code are inside the loop?
  # Answer: lien5 and 6 is inside the loop because it is indented under a while statement

# How many times will the loop repeat?
  # Answer: the loop will continue until the guess is same to the number, so if the person got it in n times, the loop will repeat n-1 times.

# What has to happen to make the program run the last line of code?
  # Answer: the while statement should be False and the loop should stop repeating.

#Task 3
secret_number = 10
guess = int(input("Guess the secret number! "))

while secret_number != guess:
  guess = int(input("Guess it again! "))

print("Congratulations!! You got it right")