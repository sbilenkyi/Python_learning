def birthday_card():
    print('Happy birthday!')


def echo(anything):
    return anything


# pass - оператор-заглушка, рівноцінний відсутності операції.
def do_nothing():
    pass
# None - це константа, що представляє відсутність значення, тобто означає нічого або порожнє місце.
# Значення None не є булевим значенням False.


# Значення за замовчуванням
def describe_pet(pet_name, animal_type='parrot'):
    print("I have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
#  describe_pet('Jack')


# кортеж
def print_days(*args):
    print('Get ready:', args)
# print_days('hello', 'big', 'sheep')


def print_travel(required1, required2, *args):
    print('For train travel is required:', required1)
    print('For train travel is required too:', required2)
    print('All the rest:', *args)
# print_travel('return ticket', 'train', 'carriage', 'seat', 'luggage rack')


# Ви можете використовувати два символа **, щоб згрупувати іменовані аргументи у словник,
# де імена аргументів стануть ключами, а їх значення - відповідними значеннями у словнику.
def print_character(**kwargs):
    print('Person\'s characteristics:', kwargs)
print_character(emotions='cheerful', sense='happy', look='slim')


# !!><<<<<<<<<<<<<<<<  При використанні символа * не потрібно обов’язково називати кортеж параметрів args,
# аналогічно при використанні символів ** називати словник параметрів kwargs, однак це поширена практика у Python.
# !>>>>>>>>>>>>>>>>>>>>>
