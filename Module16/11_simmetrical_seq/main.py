def is_symmetric(seq):
    return seq == seq[::-1]



n = int(input("Количество чисел: "))
sequence = []

for i in range(n):
    num = int(input("Число: "))
    sequence.append(num)

print(f"Последовательность: {sequence}")

numbers_to_add = []
for start_index in range(n):
    if is_symmetric(sequence[start_index:]):
        numbers_to_add = sequence[:start_index][::-1]
        break

count_to_add = len(numbers_to_add)
print(f"Нужно приписать чисел: {count_to_add}")
print(f"Сами числа: {numbers_to_add}")
