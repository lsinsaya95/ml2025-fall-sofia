# module5_mod.py


class NumberStore:
    def __init__(self):
        self.numbers = []
        print("The list is currently empty.\n")

    def insert(self, value):
        self.numbers.append(value)
        print(f"Number {value} added successfully.")
        print(f"Current numbers: {self.numbers}\n")

    def search_first_index_1based(self, target):
        print(f"Searching for {target} in the list {self.numbers} ...")
        for i, v in enumerate(self.numbers, start=1):
            if v == target:
                print(f"Found {target} at position {i}.")
                return i
        print(f"{target} was not found in the list.")
        return -1

    def show_all(self):
        print(f"Current list of numbers: {self.numbers}\n")
