#Examples

#1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  
  
#2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#3
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
  
#4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
  
#5
for x in range(6):
  print(x)
  
#6
for x in range(2, 6):
  print(x)
  
#7
for x in range(2, 30, 3):
  print(x)
  
#8
for x in range(6):
  print(x)
else:
  print("Finally finished!")
  
  
#Exercises

#1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  
#2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
  
#3
for x in range(6):
  print(x)
  
#4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)