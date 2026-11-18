text = input("Введите текст: ")
vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
vowel_list = [char for char in text if char in vowels]
print("Список гласных букв:", vowel_list)
print("Длина списка:", len(vowel_list))

