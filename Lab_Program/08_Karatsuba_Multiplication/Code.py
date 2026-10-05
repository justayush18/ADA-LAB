import time

def karatsuba(x, y):
    if x < 10 or y < 10: 
        return x * y
    
    n = max(len(str(x)), len(str(y))) // 2
    p = 10**n
    a = x // p
    b = x % p
    c = y // p
    d = y % p

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_bc = karatsuba(a + b, c + d) - ac - bd
    return ac * p * p + ad_bc * p + bd

def normal(x, y):
    return x * y

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

start = time.time()
print("Karatsuba:", karatsuba(x, y))
print("Time:", time.time() - start)

start = time.time()
print("Conventional:", normal(x, y))
print("Time:", time.time() - start)
