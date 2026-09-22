class TournamentResult:
    def __init__(self, maximum):
        self.maximum = maximum
        self.defeated = []


comparisons = 0


def find_maximum(arr, left, right):
    global comparisons

    if left == right:
        return TournamentResult(arr[left])

    mid = left + (right - left) // 2

    left_result = find_maximum(arr, left, mid)
    right_result = find_maximum(arr, mid + 1, right)

    comparisons += 1

    if left_result.maximum >= right_result.maximum:
        left_result.defeated.append(right_result.maximum)
        left_result.defeated.extend(right_result.defeated)
        return left_result

    right_result.defeated.append(left_result.maximum)
    right_result.defeated.extend(left_result.defeated)
    return right_result


def second_largest(arr):
    global comparisons

    if len(arr) < 2:
        raise ValueError("Array must contain at least two elements.")

    comparisons = 0

    result = find_maximum(arr, 0, len(arr) - 1)

    second = result.defeated[0]

    for value in result.defeated[1:]:
        comparisons += 1

        if value > second:
            second = value

    return second


def main():
    import time

    n = int(input("Enter number of elements: "))

    if n < 2:
        print("Array must contain at least two elements.")
        return

    arr = list(map(int, input("Enter array elements: ").split()))

    if len(arr) != n:
        print("Number of elements entered does not match n.")
        return

    start = time.perf_counter_ns()
    answer = second_largest(arr)
    execution_time = time.perf_counter_ns() - start

    print()
    print("Second largest element:", answer)
    print("Number of comparisons:", comparisons)
    print("Execution time:", execution_time, "ns")


if __name__ == "__main__":
    main()
