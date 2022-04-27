# 6 задач в одной из яндекс практикума
DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}


def format_friends_count(friends_count):
    if friends_count == 1:
        return '1 друг'
    elif 2 <= friends_count <= 4:
        return f'{friends_count} друга'
    else:
        return f'{friends_count} друзей'


def process_query(query):
    tokens = query.split(', ')
    name = tokens[0]
    if name == 'Анфиса':
        return process_anfisa(tokens[1])
    else:
        return process_friend(tokens)


def process_anfisa(query):
    if query == 'сколько у меня друзей?':
        count = format_friends_count(len(DATABASE))
        return f'У тебя {count}.'
    elif query == 'кто все мои друзья?':
        friends_string = ', '.join(DATABASE)
        return f'Твои друзья: {friends_string}'
    elif query == 'где все мои друзья?':
        unique_cities = set(DATABASE.values())
        cities_string = ', '.join(unique_cities)
        return f'Твои друзья в городах: {cities_string}'
    else:
        return '<неизвестный запрос>'


def process_friend(tokens):
    city = DATABASE.get(tokens[0])
    if tokens[1] == 'ты где?' and city is not None:
        return f'{tokens[0]} в городе {city}'
    elif tokens[0] == 'Коля':
        return '<неизвестный запрос>'
    else:
        return f'У тебя нет друга по имени {tokens[0]}'


print('Привет, я Анфиса!')
print(process_query('Анфиса, сколько у меня друзей?'))
print(process_query('Анфиса, кто все мои друзья?'))
print(process_query('Анфиса, где все мои друзья?'))
print(process_query('Анфиса, кто виноват?'))
print(process_query('Соня, ты где?'))
print(process_query('Коля, что делать?'))
print(process_query('Антон, ты где?'))