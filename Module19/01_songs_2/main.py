violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

song_count = int(input("Сколько песен выбрать? "))
total_duration = 0

for i in range(song_count):
    song_name = input("Название " + str(i + 1) + " песни: ")
    total_duration = total_duration + violator_songs[song_name]

print("Общее время звучания песен: " + str(round(total_duration, 2)) + " минуты")


