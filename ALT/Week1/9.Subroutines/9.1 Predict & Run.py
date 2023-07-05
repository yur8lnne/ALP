# Example Code 1

def say_hi():
  print("Why hello there!") 
  #create a subroutine that prints out 'Why hello there!'

def offer_drink():
  print("Would you care for a spot of tea?") 
  #create a subroutine that prints out 'Would you care for a spot of tea?'

def offer_food():
  print("Biscuit?")
  #create a subroutine that prints out 'Biscuit?'

def say_bye():
  print("Cheerio then.")
  #create a subroutine that prints out 'Cheerio then.'

offer_drink() #call the subroutine
say_hi()
offer_food()

# Example code 2
def maths1(): #define a function
  num1 = 50 #assign variable
  num2 = 5 #assign another variable
  return num1 + num2 #when this function is called it retuens the sum of num1 and num2

def maths2(): #define a function
  num1 = 50 #assign variable
  num2 = 5 #assign another variable
  return num1 - num2 #when this function is called it retuens the subtraction of num1 and num2

def maths3(): #define a function
  num1 = 50 #assign variable
  num2 = 5 #assign another variable
  return num1 * num2 #when this function is called it retuens the product of num1 and num2

outputNum = maths2() 
#assign variable with the value of subroutine, assigns (num1 - num2 = 50-5 = 45)
print(outputNum) #prints out the value of the variable

# Example Code 3
def location(country): #create subroutine
  print("I am from " + country)


location("Brazil") #prints out 'I am from Brazil'

