'''
Chat-Bot Challenge

Lots of websites use chat bots to interact with their customers.  These chat bots are often very sophisticated and use AI to learn and adapt to the user.  Our chat bot is going to be a bit simpler.

The chat bot should work like this:

1.Ask the user their name and store it in a variable.
2. Greet the user by name.
3. Ask the user three(or four) questions about themselves and store their responses in three(or four) different suitably named variables.
4. Respond to each of the questions one by one, using the 5. user’s name in the response.
5. Output a summary of all of the user’s answers in a single sentence.

'''

username = input("What is your name? ")
print("Hello nice to meet you " + username + "! \n")

age = input("How old are you? ")
bday = input("When is your birth day? ")
familymem = input("Do you have any siblings? ")

print("Oh " + username + " ,your age is " + age + ", your birthday is " + bday + ", and you have " + familymem + " siblings!")