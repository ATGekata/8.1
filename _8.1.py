N = int(input("Enter the number of elements N: "))

numbers = []
for _ in range(N):
    num = int(input())
    numbers.append(num)

reversed_numbers = numbers[::-1]

print("Reversed array:")
for num in reversed_numbers:
    print(num)
