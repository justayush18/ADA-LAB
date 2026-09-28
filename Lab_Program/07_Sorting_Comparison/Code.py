import time
import heapq

def merge(a):
    if len(a) <= 1: return a
    m = len(a)//2
    l, r = merge(a[:m]), merge(a[m:])
    return sorted(l + r)

def quick(a):
    if len(a) <= 1: return a
    p = a[0]
    return quick([x for x in a[1:] if x <= p]) + [p] + quick([x for x in a[1:] if x > p])

def heap(a):
    h = a.copy()
    heapq.heapify(h)
    return [heapq.heappop(h) for _ in h]

a = list(map(int, input("Enter array: ").split()))

for name, sort in [("Merge", merge), ("Quick", quick), ("Heap", heap)]:
    start = time.time()
    print(name, sort(a))
    print("Time:", time.time() - start)
