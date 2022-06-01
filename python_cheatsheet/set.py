empty_set = set()
#  print(empty_set)

numbers = {0, 1, 2, 3, 4, 5, 6}
#  print(numbers)

set_chars = set('python')
#  print(set_chars)

#  print(5 in numbers)

x = {0, 1, 4, 5, 7, 9}  # Створення множини x = {0, 1, 4, 5, 7, 9}.
y = {1, 2, 3, 6, 7, 8, 9}  # Створення множини y = {1, 2, 3, 6, 7, 8, 9}.
x.add(100)  # Додавання до множини x елемента 100 за допомогою функції add.
# print(x)  # Видалення із множини x елемента 100 за допомогою функції remove.
x.remove(100)  #
# print(x)  #
# print(x | y)  # Оператор | об’єднує дві множини і повертає нову множину з унікальними значеннями.
# print(x & y)  # Оператор & повертає нову множину із значеннями, які повторюються в обох множинах.
# print(x - y)  # Оператор - повертає множину із елементами, які є унікальними лише для другої множини y
# print(y - x)  #
# print(x ^ y)  # Оператор ˆ повертає множину елементів, які входять лише в одну із двох множин x і y.

# <<<!!!!!!!!! frozenset >>>>>!!!!!
off = set([0, 1, 2, 3, 4])
on = frozenset(off)


dairy_products = ['butter', 'cheese', 'yoghurt']
vegetables = ['potatoes', 'broccoli', 'carrot', 'cucumber', 'onion']
light_snacks = ['biscuits', 'chocolate', 'nuts']
tuple_of_lists = dairy_products, vegetables, light_snacks
# print(tuple_of_lists)
list_of_lists = [dairy_products, vegetables, light_snacks]
# print(list_of_lists)
dict_of_lists = {'Dairy': dairy_products, 'Vegetables': vegetables, 'Snacks': light_snacks}
# print(dict_of_lists)
sports_equipment = {('1500 metres', 'high jump', 'shot put'): 'Athletics',('goalkeeper', 'foul', 'corner'): 'Football',('handlebars', 'wheels', 'bicycle pump'): 'Cycling'}
# print(sports_equipment)





