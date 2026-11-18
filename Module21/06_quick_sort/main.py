site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}
def find_value(data, search_key, max_depth=None):
    if max_depth is not None and max_depth < 1:
        return None
    for current_key, current_value in data.items():
        if current_key == search_key:
            return current_value
        if isinstance(current_value, dict):
            if max_depth is None:
                result = find_value(current_value, search_key)
            else:
                result = find_value(current_value, search_key, max_depth - 1)
            if result is not None:
                return result
    return None
def get_search_parameters():
    search_key = input('Введите искомый ключ: ')
    depth_answer = input('Хотите ввести максимальную глубину? Y/N: ').lower()
    if depth_answer == 'y':
        max_depth = int(input('Введите максимальную глубину: '))
    else:
        max_depth = None
    print('Значение ключа:', find_value(site, search_key, max_depth))
get_search_parameters()
