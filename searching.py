import json

def read_data(filer, field):
    allowed_keys = {"ordered_numbers", "unordered_numbers"}

    if field not in allowed_keys:
        return None

    with open(filer, "r", encoding="utf-8") as file:
        data = json.load(file)

    return data.get(field)


def linear_search(sequence, number):
    positions = []
    count = 0

    for i in range(len(sequence)):
        if sequence[i] == number:
            positions.append(i)
            count += 1

    return {
        "positions": positions,
        "count": count
    }


def binary_search(sequence, number):
    left = 0
    right = len(sequence) - 1

    while left <= right:
        middle = (left + right) // 2

        if sequence[middle] == number:
            return middle
        elif sequence[middle] < number:
            left = middle + 1
        else:
            right = middle - 1

    return None


def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)

    number_to_find = 4
    result = linear_search(sequential_data, number_to_find)
    print(result)

    ordered_data = read_data("sequential.json", "ordered_numbers")

    number_to_find = 4
    index = binary_search(ordered_data, number_to_find)
    print(index)


if __name__ == "__main__":
    main()
