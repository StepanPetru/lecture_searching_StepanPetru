import time
import random
import matplotlib.pyplot as plt


def linear_search(data, number):
    for i in range(len(data)):
        if data[i] == number:
            return i
    return None


def binary_search(data, number):
    left = 0
    right = len(data) - 1

    while left <= right:
        mid = (left + right) // 2

        if data[mid] == number:
            return mid
        elif data[mid] < number:
            left = mid + 1
        else:
            right = mid - 1

    return None


def main():
    sizes = [1000, 5000, 10000, 50000, 100000]

    linear_times = []
    binary_times = []

    for size in sizes:
        data = [random.randint(0, size) for _ in range(size)]
        sorted_data = sorted(data)
        target = random.choice(sorted_data)

        start = time.perf_counter()
        linear_search(data, target)
        linear_times.append((time.perf_counter() - start) * 1000)

        start = time.perf_counter()
        binary_search(sorted_data, target)
        binary_times.append((time.perf_counter() - start) * 1000)

    plt.plot(sizes, linear_times, label="Linear search")
    plt.plot(sizes, binary_times, label="Binary search")

    plt.xlabel("Velikost seznamu")
    plt.ylabel("Čas (ms)")
    plt.title("Porovnání lineárního a binárního vyhledávání")
    plt.legend()

    plt.show()


if __name__ == "__main__":
    main()
