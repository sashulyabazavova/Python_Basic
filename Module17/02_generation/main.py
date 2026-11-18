n = int(input("Введите длину списка: "))
result = [1 if i % 2 == 0 else num % 5 for i, num in enumerate(range(n))]
print("Результат:", result)

