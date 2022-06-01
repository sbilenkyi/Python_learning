birds = ['pigeon', 'crow', 'owl', 'eagle']
# for bird in birds:
#    print(bird)

word = 'crab'
# for letter in word:
#    print(letter)

professions = {'business': 'economist', 'tv': 'newsreader', 'it': 'web developer', 'education': 'teacher'}
# for key in professions:  # або for key in professions.keys():
#    print(key)

# for value in professions.values():
#   print(value)

# for item in professions.items():
#    print(item)

# for key, value in professions.items():
#    print('Category', key, 'has a profession', value)

popular_sites = ['Google.com', 'Youtube.com', 'Facebook.com', 'Baidu.com', 'Wikipedia.org', 'Yahoo.com' ,'Amazon.com']
# for index, value in enumerate(popular_sites, 1):
#    print(index, value)

days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['coconut', 'lemon', 'mango']
drinks = ['coffee', 'tea', 'fruit juice']
desserts = ['marmalade', 'ice cream', 'pie', 'pudding']
# for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
#    print(day, ": drink", drink, "eat", fruit, "enjoy", dessert)

english = 'Monday', 'Tuesday', 'Wednesday'
french = 'Lundi', 'Mardi', 'Mercredi'
# print(list(zip(english, french)))

my_str_list = ['1', '2', '3', '4']
my_int_list = list(map(int, my_str_list))
# print(my_int_list)

# [вираз for елемент in ітеративний елемент if умова]
number_list = [number for number in range(1,6)]
# print(number_list)
a_list = [number for number in range(1, 6) if number % 2 == 1]
# print(a_list)

# {ключ: значення for вираз in ітеративний елемент}
letter_counts = {letter: word.count(letter) for letter in word}
# print(letter_counts)
# Наступний спосіб розв’язування задачі більш характерний для Python
# (використовується функція set(), яка свторює множину лише з унікальних літер слова)
word = 'Antarctica'
letter_counts = {letter: word.count(letter) for letter in set(word)}
# print(letter_counts)


