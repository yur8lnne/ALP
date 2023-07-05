'''
In the modify tasks, you are given some starter code. Use the instructions below to make changes to the code. Comment your changes to explain what you have done.

Run the program to see how it works.
Adapt the code to:

1. Get user input into the number variable.
2. Change the print statement so it outputs 'number' multiplied by 'counter' equals 'product'
3. Make the counter increase by 2 every loop
4. Add a line once the loop has finished to output 'The loop has finished' '''

number = int(input("Enter a number. ")) #assign variable number by getting an input integer.
counter = 1 #assign variable

while counter < 13:
  print(str(number) + " mutilplied by " + str(counter) + " equals " + str(counter * number)) #inside loop
  counter += 2 #the variable counter increases by 2 ever loop using '+='

print("\n-----------------------------------\n")

print("The loop has finished") # added a statement out of the while loop

#Task 3b
number = 7
counter = 1

while counter < 13:
  print(str(counter) + " times " + str(number) + " is " + str(counter*number))
  counter += 1

print("\n-----------------------------------\n")

#EXTRA CHALLENGE
number = int(input("Enter a number. ")) 
counter = 1 
while counter < 13:
  print(str(counter) + " times " + str(number) + " is " + str(counter*number))
  counter += 1