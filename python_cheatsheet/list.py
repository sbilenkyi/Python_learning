cars = ['Alfa Romeo', 'Volvo', 'Lamborghini', 'BMW', 'Toyota']

# make copies of list a
a = [1, 2, 3, 4]
b = a.copy()
c = list(a)
d = a[:]

planets = ['Mercury', 'Jupiter', 'Earth', 'Mars', 'Venus']
# print(len(planets))

s = "Python_is_awesome!"
chars = list(s)
# print(chars)

my_birthday = "18/07/1995"
# print(my_birthday.split('/'))

# print(', '.join(planets))

text_editors = ['Atom', 'Sublime Text']
programming_language = ['Python', 'C', 'JavaScript']
programmers = ['Guido van Rossum', 'Dennis Richie', 'Brendan Eich']
all_info = [text_editors, 'code', programming_language, programmers]
# print(all_info)
# print(all_info[0], all_info[3])
# print(all_info[0][1]) # printing the first element in the first list item

planets.append('Uranus')  # adding item to end of the list
# print(planets)

planets.insert(3, 'Neptune')  # insert an item by index 3
# print(planets)

planets = ['Earth', 'Mars']
satellites = ['Moon', 'Deimos', 'Phobos']  # also we can use += !!<<<<<!!
planets.extend(satellites)
# print(planets)

del planets[-1]  # deleted an item by index
# print(planets)

planets.remove("Mars")  # deleted an item by value
# print(planets)

planets = ['Mercury', 'Jupiter', 'Earth', 'Mars', 'Venus']
planet = planets.pop()  # default index is -1 !!<<<<<!!
# print(planet)
the_second_planet = planets.pop(0)
# print(the_second_planet)

countries = ['England', 'France', 'Italy', 'Ukraine', 'Poland']
# print('Poland' in countries)  # True
# print('Hungary' in countries)  # False

countries_1 = ['England', 'France', 'Italy', 'Ukraine', 'Poland']
# print('Ukraine' not in countries) # False

fruits = ['blueberry', 'grape', 'orange', 'plum', 'pear', 'blueberry', 'pear', 'melon', 'pear']
# print(fruits.count('grape'), fruits.count('peach'), fruits.count('pear'), fruits.count('blueberry'), sep='_')

# <<<<!!!! For sort and sorted all items must be same type !!!!!>>>>>>>>
clothes = ['shirt', 'hat', 'jeans', 'trainers']
sorted_clothes = sorted(clothes)  # sorted does not change original list
# print(clothes, sorted_clothes, sep='\n')

clothes.sort()  # sort changes original list
numbers = list(range(8))
# print(numbers)
numbers.sort(reverse=True)  # reverse sorting
# print(numbers)
# print(clothes)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()  # reverse
# print(cars)


digits = list(range(10))
# print(min(digits), max(digits), sum(digits), sep='\n')
