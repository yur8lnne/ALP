'''
Answer the questions

'''

# Example code:

names = ["Alex","Anita","Patrick","Atif","Sue"]

print("Enter a number for your choice.")
print("1. Show all")
print("2. Add name")
print("3. Show name")
print("4. Exit")
choice = int(input())

if choice == 1:
  print(names)
elif choice == 2:
  name = input("Enter the name")
  names.append(name)
elif choice == 3:
  print("Enter the index of the name")
  index = int(input())
  print(names[index])
else:
  print("Goodbye")


# What is the identifier for the list in this program?
  # Answer: name (list)

# What would happen if you choose option “3” and entered index “0”? 
  # Answer: it prints out Alex. 

# What would happen if you choose option “3” and entered index “7”?
  # Answer: it prints out none because it doesn't have a index "7" item.

# What would happen if you choose option “2” and entered the name “Stuart”?
  # Answer: "Stuart" will be added to the last to the name list. 

# What is the purpose of int(input()) on line 10 ?
  # Answer: it is to ask the person to choose the function. 

