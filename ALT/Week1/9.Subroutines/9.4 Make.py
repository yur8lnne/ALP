def add(a,b):
  return a+b
def subtract(a,b):
  return a-b
def multiply(a,b):
  return a*b
def divide(a,b):
  return a/b

num = int(input("1. add, 2. subtract, 3. multiply, 4. divide "))
if num == 1:
  print(add(10, 5))
elif num == 2:
  print(subtract(10,5))
elif num == 3:
  print(multiply(10,5))
else:
  print(divide(10,5))