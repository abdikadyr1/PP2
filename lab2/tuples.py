#Examples

#1
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#2
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#3
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#4
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#5
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

#Exercises

#1
fruits = ("apple", "banana", "cherry")
print(fruits[0])

#2
fruits = ("apple", "banana", "cherry")
print(len(fruits))

#3
fruits = ("apple", "banana", "cherry")
print(fruits[-1])

#4
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])