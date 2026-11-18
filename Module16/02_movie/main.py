films = [
    'Крепкий орешек',
    'Назад в будущее',
    'Таксист',
    'Леон',
    'Богемская рапсодия',
    'Город грехов',
    'Мементо',
    'Отступники',
    'Деревня'
]

favorite_movies = []
num_movies = int(input('Сколько фильмов хотите добавить? '))

for _ in range(num_movies):
    movie = input('Введите название фильма: ')
    if movie in films:
        favorite_movies.append(movie)
    else:
        print(f'Ошибка: фильма {movie} у нас нет :(')

print('Ваш список любимых фильмов:', ', '.join(favorite_movies))


