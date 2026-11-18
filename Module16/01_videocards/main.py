number_of_cards = int(input("Количество видеокарт: "))

video_cards = []

for i in range(number_of_cards):
    card_model = int(input(f"Видеокарта {i + 1}: "))
    video_cards.append(card_model)

print("\nСтарый список видеокарт:", video_cards)

max_model = max(video_cards)
new_video_cards = [model for model in video_cards if model != max_model]

print("Новый список видеокарт:", new_video_cards)




