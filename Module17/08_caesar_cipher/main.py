def caesar_cipher(text, shift):
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    result = ''
    for char in text:
        if char.lower() in alphabet:
            pos = alphabet.index(char.lower())
            new_pos = (pos + shift) % 33
            new_char = alphabet[new_pos]
            if char.isupper():
                new_char = new_char.upper()
            result += new_char
        else:
            result += char
    return result

message = input("Введите сообщение: ")
shift = int(input("Введите сдвиг: "))
print("Зашифрованное сообщение:", caesar_cipher(message, shift))


