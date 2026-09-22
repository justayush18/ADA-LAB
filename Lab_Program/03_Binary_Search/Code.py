import time
import sys

def recursive(a, x, l, r, depth=1):
    global rc, rd
    rd = max(rd, depth)
    if l > r:
        return -1
    rc += 1
    m = (l + r) // 2
    if a[m] == x:
        return m
    if x < a[m]:
        return recursive(a, x, l, m - 1, depth + 1)
    return recursive(a, x, m + 1, r, depth + 1)

def iterative(a, x):
    global ic
    l, r = 0, len(a) - 1
    while l <= r:
        ic += 1
        m = (l + r) // 2
        if a[m] == x:
            return m
        if x < a[m]:
            r = m - 1
        else:
            l = m + 1
    return -1

n = int(input("Enter number of elements: "))
a = list(map(int, input("Enter sorted array: ").split()))
x = int(input("Enter element to search: "))

if len(a) != n or a != sorted(a):
    print("Enter exactly n elements in sorted order.")
    sys.exit()

rc = ic = rd = 0

start = time.perf_counter_ns()
r1 = recursive(a, x, 0, n - 1)
rt = time.perf_counter_ns() - start

start = time.perf_counter_ns()
r2 = iterative(a, x)
it = time.perf_counter_ns() - start

print("\nRecursive Binary Search")
print("Index:", r1, "Comparisons:", rc, "Depth:", rd, "Time:", rt, "ns")

print("\nIterative Binary Search")
print("Index:", r2, "Comparisons:", ic, "Depth: O(1)", "Time:", it, "ns")
