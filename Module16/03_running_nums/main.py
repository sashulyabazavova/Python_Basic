k = int(input("Сдвиг: "))
original_list = list(map(int, input("Изначальный список: [").rstrip(']').split(', ')))


length = len(original_list)
if length > 0:
    k = k % length
    shifted_list = original_list[-k:] + original_list[:-k]
else:
    shifted_list = []

print("Сдвинутый список:", shifted_list)
