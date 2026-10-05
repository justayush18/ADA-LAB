import time
import heapq

def merge(a):
    if len(a) <= 1:
        return a
    m = len(a)//2
    l, r = merge(a[:m]), merge(a[m:])
    return sorted(l + r)

def quick(a):
    if len(a) <= 1:
        return a
    p = a[0]
    left = []
    right = []

    for x in a[1:]:
        if x <= p:
            left.append(x)
        else:
            right.append(x)
    return quick(left) + [p] + quick(right)

def heap(a):
    h = a.copy()
    heapq.heapify(h)

    result = []
    while h:
        result.append(heapq.heappop(h))

    return result

a = list(map(int, input("Enter array: ").split()))

for name, sort in [("Merge", merge), ("Quick", quick), ("Heap", heap)]:
    start = time.time()
    print(name, sort(a))
    print("Time:", time.time() - start)