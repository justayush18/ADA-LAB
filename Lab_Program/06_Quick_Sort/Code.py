import random
import time

def quick(a, low, high, choice):
    if low >= high:
        return
    if choice == "first":
        p = low
    elif choice == "last":
        p = high
    elif choice == "middle":
        p = (low + high) // 2
    else:
        p = random.randint(low, high)

    a[p], a[high] = a[high], a[p]
    pivot, i = a[high], low

    for j in range(low, high):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1

    a[i], a[high] = a[high], a[i]
    quick(a, low, i - 1, choice)
    quick(a, i + 1, high, choice)

a = list(map(int, input("Enter array: ").split()))

for choice in ["first", "last", "middle", "random"]:
    b = a.copy()
    start = time.time()
    quick(b, 0, len(b) - 1, choice)
    print(choice, b, time.time() - start)
