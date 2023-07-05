# Example Code

number = 5
print("I have thought of a number between 1 and 10")
guess = int(input("Can you guess what it is?"))

if guess == number:
  print("Correct!")
if guess < number:
  print("Too Low!")
if guess > number:
  print("Too High!")

# What happens if you input the guess '2'?
  # Answer: it prints 'Too Low!'.

# What happens if you input the guess '6'?
  # Answer: it prints 'Too High!'.

# What happens if you input the guess '5'?
  # Answer: it prints 'Correct!'

# What happens if you input the guess '-5'?
  # Answer: it prints 'Too Low!'.

# What happens if you input the guess '0'?
  # Answer: it prints 'Too Low!'.

# What do the symbols '<' and '>' mean on lines 9 and 11?
  # Answer: The symbol '<' means that the left value of the symbol is smaller than the right value of the symbol. In contraty, hte symbol '>' means that the left value of the symbol is bigger than the right value of the symbol.

# What happens if you change line 5 to if guess = number: ?
  # Answer: The syntax error occors because the symbol '=' is not used for comparison it is used to assign values into variables. 

# What do you notice about each line that FOLLOWS each IF statement?
  # Answer: The print function is followed to each if statement. 


