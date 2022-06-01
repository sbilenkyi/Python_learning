add = lambda x, y: x + y
print(add(2, 5))
# Та ж сама функція add може бути визначена за допомогою ключового слова def:
def add(x, y):
    return x + y
print(add(2, 5))
# <<<!!!Крім цього, анонімну функцію не обов’язково присвоювати змінній <<<<!!!
print((lambda x, y: x + y)(5, 12))


months = [(1, 'January'), (9, 'September'), (7, 'July'), (4, 'March')]
print(sorted(months, key=lambda x: x[1])) # сотрування відбувається за літерами
print(sorted(months))




