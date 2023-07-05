Fail = ""
score = int(input("What is your score? "))

if score < 1 or 100 < score:
  print("Enter a number between 1 and 100")
# it prints out an message when it is out of range. I used an inequality sign to check if it fits in a range. 

else: # if it fits the range it follows the else statement
  if score < 40:
    Fail = "Y" 
  elif 40 <= score <= 100:
    Fail = "N"
  
  if Fail != "N":
    print("Retake required")
# After using statements to determine if it is bigger or smaller, we assign "Y" or "N" in variable Fail. Then the output becomes the value in the variable Fail.

print("\n---------------------------------------------------\n")

grade = ""
score = int(input("What is your score? "))

if score < 1 or 100 < score:
  print("Enter a number between 1 and 100")
# it prints out an message when it is out of range. I used an inequality sign to check if it fits in a range. 

else: # if it fits the range it follows the else statement
  if score < 40:
    grade = "U" 
  elif 40 <= score <= 68:
    grade = "C"
  elif 69 <= score <= 79:
    grade = "B"
  else:
    grade = "A"
  # by using '>', '<', '=' we can find which range the score belongs, and when it fits one range we assign variable grade. 
  
  print(grade)
  # it prints out the grade variable assigned above.