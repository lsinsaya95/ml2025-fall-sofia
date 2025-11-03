# module5_call.py
# This is the main interactive program that uses the NumberStore class.

from module5_mod import NumberStore

def main():
    print("Hi, You'll enter a few numbers, and the program will help you find any number you choose")

    store = NumberStore()

    while True:
        try:
            N = int(input("Enter how many numbers do you want on the numberstore (a positive integer): "))
            if N > 0:
                break
            else:
                print("Please enter a number greater than 0")
        except ValueError:
            print(" Invalid input. Please enter an integer again")

    for i in range(1, N + 1):
        while True:
            try:
                num = int(input("Enter number {i}: "))
                store.insert(num)
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")

    store.show_all()

    while True:
        try:
            X = int(input("Now enter the number you want to search for: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    result = store.search_first_index_1based(X)
    print(f"\n👉 Final result : {result}\n")
  

if __name__ == "__main__":
    main()
