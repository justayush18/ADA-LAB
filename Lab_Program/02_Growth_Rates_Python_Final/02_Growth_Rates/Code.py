import time
import matplotlib.pyplot as plt

def measure(work, n):
    start = time.perf_counter()
    work(n)
    return time.perf_counter() - start

def log_n(n):
    i = 1
    while i < n:
        i *= 2

def linear(n):
    for _ in range(n):
        pass

def n_log_n(n):
    for _ in range(n):
        i = 1
        while i < n:
            i *= 2

def quadratic(n):
    for _ in range(n):
        for _ in range(n):
            pass

def exponential(n):
    if n == 0:
        return
    exponential(n - 1)
    exponential(n - 1)

tests = {
    "O(log n)": (log_n, [10000, 100000, 1000000]),
    "O(n)": (linear, [10000, 100000, 1000000]),
    "O(n log n)": (n_log_n, [1000, 10000, 100000]),
    "O(n²)": (quadratic, [100, 500, 1000]),
    "O(2ⁿ)": (exponential, [5, 10, 15, 20])
}

for name, (work, sizes) in tests.items():
    times = [measure(work, n) for n in sizes]
    print(name)
    for n, t in zip(sizes, times):
        print(f"n = {n}, time = {t:.8f} seconds")
    plt.plot(sizes, times, marker="o", label=name)

plt.xlabel("Input Size (n)")
plt.ylabel("Execution Time (seconds)")
plt.title("Experimental Growth Rates")
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig("growth_rates.png", dpi=300)
plt.show()
