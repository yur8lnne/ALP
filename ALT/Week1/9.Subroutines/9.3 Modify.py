'''
In the modify tasks, you are given some starter code.
Use the instructions below to make changes to the code.
Comment your changes to explain what you have done.

Adapt the code to:
- Rename the function so that it has a sensible name. Don't forget to rename it when it is called.
- Call the function with the argument 'Sweden'.
- Get the user to input a country. Store it in a variable. Call the function again with the variable as the parameter.
'''
def introduction(country): #create a subroutine and renamed to introduction
  print("I am from " + country)


introduction("Sweden") #calling the funtion created above

yourcountry = int("Enter a country name ") #assign a variable by getting an input value
introduction(yourcountry) #calling the subroutine introduction by using a variable assigned above