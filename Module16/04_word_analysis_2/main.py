word = input("Введите слово: ").strip().lower()
char_list = list(word)
reversed_list = char_list[::-1]

if char_list == reversed_list:
    print("Слово является палиндромом")
else:
    print("Слово не является палиндромом")
