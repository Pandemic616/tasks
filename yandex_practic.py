# задача из яндекс практикума
def get_together_games(games_1, games_2):
    return set(games_1).intersection(set(games_2))

anfisa_games = [
    'Online-chess',
    'Города',
    'DOOM',
    'Крестики-нолики'
]
alisa_games = [
    'DOOM',
    'Online-chess',
    'Города',
    'GTA',
    'World of tanks'
]
together_games = get_together_games(anfisa_games, alisa_games)
for game in together_games:
    print('👾', game)