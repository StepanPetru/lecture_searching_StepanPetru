import json

def read_data(filer, field):
    allowed_keys = {"ordered_numbers", "unordered_numbers"}

    if field not in allowed_keys:
        return None

    with open(filer, "r", encoding="utf-8") as file:
        data = json.load(file)

    return data.get(field)


def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)


if __name__ == "__main__":
    main()