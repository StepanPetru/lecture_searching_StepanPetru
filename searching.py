import json
import time
import random
import matplotlib.pyplot as plt


def read_data(filename, field):
    allowed_keys = {"ordered_numbers", "unordered_numbers"}

    if field not in allowed_keys:
        return None

    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)

    return data.get(field)


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

    plt.xlabel("Velikost vstupu")
    plt.ylabel("Čas (ms)")
    plt.title("Porovnání lineárního a binárního vyhledávání")
    plt.legend()

    plt.show()

def pattern_search(sekvence, patern):
    pozice = set()

    for i in range(len(sekvence) - len(patern) + 1):
        if sekvence[i:i + len(patern)] == patern:
            positions.add(i)

    return pozice
def pattern_search(sequence, pattern):
    positions = set()

    i = 0
    while i <= len(sequence) - len(pattern):
        match = True

        for j in range(len(pattern)):
            if sequence[i + j] != pattern[j]:
                match = False
                break

        if match:
            positions.add(i)

        i += 1

    return positions

if __name__ == "__main__":
    main()