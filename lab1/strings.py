#1
print("Hello")
print('Hello')

#2
a = "Hello"
print(a)

#3
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#4
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#5
b = "Hello, World!"
print(b[2:5])

#6
b = "Hello, World!"
print(b[:5])

#7
a = "Hello, World!"
print(a.upper())

#8
a = "Hello, World!"
print(a.lower())

#9
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#10
a = "Hello"
b = "World"
c = a + b
print(c)

#11
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#12 e
age = 36
txt = "My name is John, I am " + age
print(txt)

#13
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#14
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#15
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

#16 e
#txt = "We are the so-called "Vikings" from the north."

#17
txt = "We are the so-called \"Vikings\" from the north."

#18
'''
\'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace	
\f	Form Feed	
\ooo	Octal value	
\xhh	Hex value
'''
    