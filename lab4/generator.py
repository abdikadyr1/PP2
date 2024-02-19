def square_g(n):
    for i in n:
        yield i ** 2
x = square_g([1, 2, 3])
print(next(x))
print(next(x))
print(next(x))

def even(n):
    l = []
    for i in range(0, n + 1):
        if i % 2 == 0:
            l.append(i)
    yield l

n = int(input())
print(next(even(n)))

def f(n):
    for i in range(0, n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
y = f(12)    
print(next(y))
print(next(y))

def squares(a, b):
    for i in range(a, b+1):
        yield i*i 


for i in squares(1, 5):
    print(i)
    

def down(n):
    if n==0:
        yield 0
        return
    yield n
    yield from down(n-1)

for i in down(5):
    print(i)