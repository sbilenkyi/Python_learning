# seasons = ['summer', 'autumn']
# months = ['july', 'november']
#
# movies = {season: month for season, month in zip(seasons, months)}
# print(movies)
# print(dict(zip(seasons, months)))

# activity = {'business': 'manager', 'it': 'software developer', 'science': 'scientist'}
# for key, value in activity.items():
#    print(f"{key} : {value}")

# print(*[i for i in range(13) if i % 2 == 0 and i != 0])

# try:
#     print({key: key ** 2 for key in range(1, 11)})
# except TypeError:
#     print("Нєхуй! Хуйньою займатися...")

# numbers = list(range(1, 1000001))
# print(f"min: {min(numbers)}\nmax: {max(numbers)}\nsum: {sum(numbers)}")


# def trees():
#     return ['poplar', 'willow', 'lime']
#
# print(trees())


class MyException(Exception):
    pass


try:
    result = 5 / 0

except MyException as exc:
    print(exc)