# Example code 1
# The value 18 is stored in the variable age. So, age > 18 is False so it doesn't have any output. 

age = 18 
 
if age > 18: 
 print("You are old enough to drive") 

# Example code 2
# The statement num1 == 10 is False because num1 stores a value 1337 which is not 10. As the above statement is False, the code print outs 'This text is output because the condition was false'.

num1 = 1337 
 
if num1 == 10: 
  print("This text is output because the condition was true") 
else:
  print("This text is output because the condition was false") 

# Example code 3
# The variable named guess stores the value wich is an input value. If the input number is smaller than 5, the output is Too Low! because the second if state is True. Same with the other statements, if the guess is bigger or same as 5, the print Too High! and Correct!.
number = 5
print("I have thought of a number between 1 and 10")
guess = int(input("Can you guess what it is?"))

if guess == number:
  print("Correct!")
if guess < number:
  print("Too Low!")
if guess > number:
  print("Too High!")
