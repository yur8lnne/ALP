'''
Task - Which Room?
----------------------

Write a program that asks the user for their name and which subject they are studying.
The program should output a message telling the student by name which room to go to for that class (make up the room numbers if you need to).  You should include at least 3 subjects and have a message such as 'I don't know which room that class is in' for any you don't include.
 Example - an input of 'Ben' and 'Computing' might get an output of 'Hi Ben, go to room 401 for Computing'


You may use any method taught in class that is appropriate for this task. There is room for interpretation.

'''
#Start coding below
subjects = ["Computer Science", "Calculus", "Physics"]
classroom = ["401", "402", "403"]

name, subject = input("Enter your name and subject ").split()

if subject in subjects:
  index = subjects.index(subject)
  print("Hi " + name + ", go to room " + classroom[index] + " for " + subject)

else:
  print("I don't know which room that class is in")