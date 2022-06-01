short_list = [1, 2, 3]
position = 5
try:
    short_list[position]
except:
    print('Need a position between 0 and', len(short_list) - 1, 'but got', position)

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide be zero!")

# try:
#     блок коду
# except тип_винятку as назва_змінної:
#     блок коду, коли виникла помилка

predators = ['tiger', 'wolf', 'bear']
# while True:
#    value = input('Position [q to quit]? ')
#    if value == 'q':
#       break
#    try:
#       position = int(value)
#        print(predators[position])
#    except IndexError as err:
#        print('Bad index:', position)
#    except Exception as other:
#        print('Something else broke:', other)


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Division by zero!")
    else:
        print("Result is", result)
    finally:
        print("End of the calculation.")


# divide(2, 1)
# divide(2, 0)


class IsNotTitleException(Exception):
    pass


try:
    rooms = ['Kitchen', 'study', 'Hall', 'Bathroom']
    for room in rooms:
        if room.title() != room:
            raise IsNotTitleException('Fault!')

except IsNotTitleException as exc:
    print(exc)