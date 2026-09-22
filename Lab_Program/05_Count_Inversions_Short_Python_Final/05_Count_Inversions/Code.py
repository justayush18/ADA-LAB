import time

a = list(map(int, input("Enter array elements: ").split()))

def brute(a):
    return sum(a[i] > a[j] for i in range(len(a)) for j in range(i+1, len(a)))

def merge(a):
    if len(a) <= 1:
        return a, 0

    m = len(a)//2
    l, x = merge(a[:m])
    r, y = merge(a[m:])
    res, i, j = [], 0, 0

    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            res.append(l[i]); i += 1
        else:
            res.append(r[j]); j += 1
            x += len(l)-i

    return res + l[i:] + r[j:], x+y

t = time.time()
print("Brute Force:", brute(a), time.time()-t)

t = time.time()
print("Merge Sort:", merge(a)[1], time.time()-t)
