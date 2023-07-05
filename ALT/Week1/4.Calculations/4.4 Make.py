# Program to calculate the area of a rectangle

# Get input for height & width. Convert to integers and store in variables

# Calculate the area & store the result in the area variable

# Output the area variable (converted to string)

height = int(input("Write the height. "))
width = int(input("Write the width. "))

area = height * width
print("The area of the rectangle is " + str(area) + ".")


'''
Extra Challenges
Perimeter Calc
Create a program that allows the user to enter 2 numbers representing the width and length of a rectangle. The program calculates and displays the perimeter of the rectangle. 
Restaurant Tip Calculator 
Create a program that allows the user to enter the price of a meal at a restaurant. The program calculates the amount of the tip to be paid at 20%. The tip and total price are then displayed separately.
Volume and Surface Calc 
Create a program that allows the user to enter 3 numbers representing the height, width and length of a cuboid. The program calculates and displays the volume and total surface area of the cuboid. 
'''
#Perimeter Calc
height = int(input("Write the height. "))
width = int(input("Write the width. "))
perimeter = (height + width) * 2
print("The perimeter of the rectangle is " + str(perimeter) + ".")

#Restaurant Tip Calculator 
price = float(input("Write the price of a meal! "))
tip = price * 0.2
print("tip : " + str(tip))
print("total price : " + str(price + tip))

#Volume and Surface Calc 
height = int(input("Write the height. "))
width = int(input("Write the width. "))
length = int(input("Write the length. "))
volume = height * width * length
surface_area = 2 * (height * width + height * length + width * length)

print("Volume : " + str(volume) + ", Total surface area : " + str(surface_area))