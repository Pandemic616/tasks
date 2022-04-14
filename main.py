# первый комит
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# x = 0
# for i in lst:
#     x += i
# print(x)
# import random
#
# lst = [x for x in range(5,30)]
# random.shuffle(lst)
# m=lst[0]
# n=lst[0]
# for i in lst:
#     if i < m:
#         m = i
#     elif i > n:
#         n = i
# print(m, n)
# def calc_cube_perimeter(side):
#     return side * 12
#
# def calc_cube_area(side):
#     one_face = side * side
#     cube_area = one_face * 6
#     return cube_area
#
# def calc_cube(side, amount):
#     one_cube_perimeter = calc_cube_perimeter(side)
#     full_length = one_cube_perimeter * amount
#     one_cube_area = calc_cube_area(side)
#     full_area = one_cube_area * amount
#     print('Для', amount, 'кубов понадобится палок (м):', full_length, 'и стекла (кв.м):', full_area)
#
# calc_cube(int(input()), int(input()))

# # задача из яндекс практикума
# def get_together_games(games_1, games_2):
#     return set(games_1).intersection(set(games_2))
#
# anfisa_games = [
#     'Online-chess',
#     'Города',
#     'DOOM',
#     'Крестики-нолики'
# ]
# alisa_games = [
#     'DOOM',
#     'Online-chess',
#     'Города',
#     'GTA',
#     'World of tanks'
# ]
# together_games = get_together_games(anfisa_games, alisa_games)
# for game in together_games:
#     print('👾', game)