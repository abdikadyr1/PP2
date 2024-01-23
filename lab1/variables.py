#1
x = 5
y = "John"
print(x)
print(y)

#2
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#3
x = 5
y = "John"
print(type(x))
print(type(y))

#4
x = "John"
# is the same as
x = 'John'

#5
a = 4
A = "Sally"
#A will not overwrite a

#6
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#7
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#8
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#9
x = "Python is awesome"
print(x)

#10
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#11
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#12
x = 5
y = 10
print(x + y)

#13 e
x = 5
y = "John"
print(x + y)

#14
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#15
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#16
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
