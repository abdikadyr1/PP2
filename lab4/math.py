import math
print("#1")
x = float(input('Input degree: '))
print(f'Output radian: {math.radians(x):.6}')

print("#2")
h, a, b = map(float, (input('Height: '), input('Base, first value: '), input('Base, second value: ')))
print('Expected Output:', (a+b)*h/2)

print("#3")
a, b = float(input('Input number of sides: ')), float(input('Input the length of a side: '))

apothem = b/(2*math.tan(math.pi / a)) 
perimeter = b*a
S = apothem * perimeter / 2
print("The area of the polygon is:", round(S))

print("#4")
a, b = float(input('Length of base: ')), float(input('Height of parallelogram: '))
print('Expected Output:', a*b) 