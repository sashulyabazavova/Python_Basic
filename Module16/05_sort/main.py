numbers = list(map(int, input("Изначальный список: ").strip()[1:-1].split(', ')))

length = len(numbers)
for i in range(length):
    for j in range(0, length - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("Отсортированный список:", numbers)

