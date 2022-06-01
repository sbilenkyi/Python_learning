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


