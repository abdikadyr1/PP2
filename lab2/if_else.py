#Examples

#1
a = 33
b = 200
if b > a:
  print("b is greater than a")
  
#2
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
  
#3
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  
  
#4
a = 2
b = 330
print("A") if a > b else print("B")

#5
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#Exercises

#1
a = 50
b = 10
if a > b:  print("Hello World")

#2
a = 50
b = 10
if a != b:  print("Hello World")

#3
a = 50
b = 10
if a == b:
    print("Yes")
else:  
    print("No")
    
#4
a = 50
b = 10
if a == b:
  print("1")
elif a > b:
  print("2")
else:
  print("3")
  
#5
if a == b and c == d:
  print("Hello")
  
#6
if a == b or c == d:
  print("Hello")
  
#7
if 5 > 2:
    print("YES")

#8
a = 2
b = 5
print("YES") if a == b else print("NO")  

#9
a = 2
b = 50
c = 2
if a == c or b == c:
  print("YES")