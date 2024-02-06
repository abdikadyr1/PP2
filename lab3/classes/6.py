x = int(input("Enter the size of the array: "))
array = []
for i in range(x):
    y = int(input())
    array.append(y)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_array = list(filter(lambda num: is_prime(num), array))

print("Prime numbers:", prime_array)