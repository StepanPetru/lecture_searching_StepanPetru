import json

def read_data(filename, field):
    allowed_keys = {"ordered_numbers", "unordered_numbers"}

    if field not in allowed_keys:
        return None

    with open(filename, "r", encoding="utf-8") as file:
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


def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)

    number_to_find = 4
    result = linear_search(sequential_data, number_to_find)

    print(result)


if __name__ == "__main__":
    main()