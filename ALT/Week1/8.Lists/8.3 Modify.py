'''
Reference Link
https://docs.google.com/document/d/1Lf221krWqB0vv5zSaQDvzBi6you6AuKdfn5x1TETh7Q/edit?usp=sharing
'''

'''In the modify tasks, you are given some starter code.
Use the instructions below to make changes to the code.
Comment your changes to explain what you have done.

Adapt the code to:

1- Add 'Minecraft' to the start of the list.

2- Ask the user to input a number between 0 and 4 and store it in a variable.  Output the item at this position in the list.

3- Ask the user to input the name of a video game and store it in a variable.  
  3.1- If this video game is in the list then remove it from the list.
  3.2- If it isn't in the list then add it to the end.
'''

# Starter Code

videoGames = ["Mario", "Sonic", "Joust", "Zelda"]

videoGames.insert(0, "Minecraft") #adds an item to the beginning of a list by specifying its position
num = int(input("Enter a number ")) #assign a variable by getting a input integer
print(videoGames[num]) #print out the selected item in the list

gamename = input("Enter the name of a video game ") #
if gamename in videoGames: #checking if the game name is in the list
  videoGames.remove(gamename) #remove the value that is inputed
else:
  videoGames.append(gamename) #add an item

#print(videoGames)