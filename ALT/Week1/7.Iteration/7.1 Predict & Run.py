# Example code 1

# Add comments to each line to say whehter it is inside or outside the loop and what it does.

# Explain the circumstances in which the loop will run.

print("What is the capital of France?")
answer = input() #variable assign

while answer != "Paris": #if the statement is True it stays inside the loop
  print("Incorrect! Try again.") #inside the loop
  answer = input("What is the capital of France?") 
  #change the value of the variable by input (inside the loop)

print("Correct!") #outside the loop

# Example code 2

counter = 1 #outside the loop, variable assign

while counter < 5: #if the statement is False, it gets out of the loop
  print("This code is inside the loop") #inside the loop
  counter += 1 #inside the loop, the value of variable changes by increasing

