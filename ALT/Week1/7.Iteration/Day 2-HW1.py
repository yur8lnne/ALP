'''
Task Instructions
You are going to write a program called "Time Reminder"

The user has to enter a number between 0 and 23
If the number is less than 8 display a message saying "too early to get up"
If the number is less than 12 display a message saying "Good morning"
If the number is less than 14 display a message saying "Lunch time!"
If the number is less than 18 display a message saying "Good afternoon"
If the number is equal to 18 display a message saying "Tea Time"
If the number is less than 19 display a message saying "Good evening"
If the number is less than 22 display a message saying "Nearly bedtime"
If the number is 23 display a message saying "Good night!"
Any other number is met with the response “Sorry, I don’t recognise that”


You are free to use any of the methods that we have learned in class.
'''
#Start coding below this line
num = int(input("Enter a number between 0 and 23 "))

if 0 <= num <= 23:
  if num < 8:
    print("too early to get up")
  elif num < 12:
    print("Good morning")
  elif num < 14:
    print("Lunch time!")
  elif num < 18:
    print("Good afternoon")
  elif num == 18:
    print("Tea Time")
  elif num < 19:
    print("Good evening")
  elif num < 22:
    print("Nearly bedtime")
  elif num == 23:
    print("Good night!")

else:
  print("Sorry, I don’t recognise that")