def hanoi(n, a, b, c):
    if n == 1:
        print(a, "->", c)
        return
    hanoi(n - 1, a, c, b)
    print(a, "->", c)
    hanoi(n - 1, b, a, c)

n = int(input("Enter disks: "))
hanoi(n, "A", "B", "C")
print("Moves =", 2 ** n - 1)

# def hanoi(n):
#     rods = {"A": list(range(n, 0, -1)), "B": [], "C": []}
#     moves = 2**n - 1
#     order = [("A", "C"), ("A", "B"), ("B", "C")]

#     if n % 2 == 0:
#         order[0], order[1] = order[1], order[0]

#     for i in range(moves):
#         x, y = order[i % 3]

#         if not rods[x] or (rods[y] and rods[x][-1] > rods[y][-1]):
#             x, y = y, x

#         rods[y].append(rods[x].pop())
#         print(x, "->", y)

# n = int(input("Enter disks: "))
# hanoi(n)