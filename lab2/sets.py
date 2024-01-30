#Examples

#1
thisset = {"apple", "banana", "cherry"}
print(thisset)

#2
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

#3
set1 = {"abc", 34, True, 40, "male"}

#Exercises

#1
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")
  
#2
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

#3
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

#4
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

#5
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
  