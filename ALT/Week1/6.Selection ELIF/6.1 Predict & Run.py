# Example code 1

number = 7 #variable assign
print("I have thought of a number between 1 and 10") #print sentence
guess = int(input("Can you guess what it is?")) #get an input integer with asking a question and assign it to a variable

if guess == number:
  print("Correct!")
  #judge if the guess is same to number, and if it's same print outs 'Correct!'
elif guess < number: 
  print("Too Low!")
  #
else:
  print("Too High!")
  # if the above two statements are both False, print 'Too High!'

# Example code 2

number1 = int(input("Please enter a number")) #assign a variable by getting a input integer with a question 
number2 = int(input("Please enter another number")) #assign another variable by getting a input integer with a question 

if number1 > number2:
  print("Number 1 is bigger than number 2")
  #if number1 is bigger than number2 it prints out 'Number 1 is bigger than number 2'
elif number2 > number1: 
  print("Number 2 is bigger than number 1")
  #if number1 is smaller than number2 it prints out 'Number 2 is bigger than number 1'
else:
  print("Both numbers are the same")
  # if the above two statements are both False, the output is 'Both numbers are the same'