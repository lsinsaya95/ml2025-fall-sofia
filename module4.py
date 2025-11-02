# module4.py

N = int(input("Enter how many positive numbers: "))

numbers = []
for i in range(N):
    num = int(input("Enter a number: "))
    numbers.append(num)

X = int(input("Enter the number to search: "))

if X in numbers:
    print( numbers.index (x) + 1)
else:
    print(-1)
