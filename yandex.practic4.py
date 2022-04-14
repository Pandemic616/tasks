# 3 задачи в одной из яндекс практикума
DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}
def process_anfisa(query):
    if query == 'Сколько у меня друзей?':
        count = len(DATABASE)
        return 'У тебя ' + str(count) + ' друзей.'
    elif query == 'Кто все мои друзья?':
        friends_string = ''
        for friend in DATABASE:
             friends_string+=friend+' '
        return('Твои друзья: '+friends_string)
    elif query == 'Где все мои друзья?':
        cities_friends=set(DATABASE.values())
        friends_cities= ' '
        for cities in cities_friends:
            friends_cities+=cities+' '
        return('Твои друзья в городах: '+friends_cities)
    else:
        return '<неизвестный запрос>'
print('Привет, я Анфиса!')
print(process_anfisa('Сколько у меня друзей?'))
print(process_anfisa('Кто все мои друзья?'))
print(process_anfisa('Где все мои друзья?'))