empty_dict = {}

mydog = {'name': 'Australian Shepherd', 'training': '5', 'intelligence': 5, 'type': 'Companion'}
# print(mydog)

# conversion to dictionary
couple = [['a', 'b'], ['c', 'd'], ['e', 'f']]
# print(dict(couple))
info = dict([('name', 'Alex'), ('age', 38)])
# print(info)

languages_programmers = {
    'JavaScript': 'Brendan Eich',
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
    'Scala': 'Martin Odersky'
}
languages_programmers['C'] = 'Denic MacAlistair Ritchie'  # added an item
# print(languages_programmers)
languages_programmers['C'] = 'Dennis Ritchie'  # changed value by key 'C'
# print(languages_programmers)

others = {'C++': 'Bjarne Stroustrup', 'Swift': 'Chris Lattner'}
languages_programmers.update(others) # added another dictionary
# print(languages_programmers)

del languages_programmers['Swift']  # deleted an item by the key
# print(languages_programmers)

languages_programmers.clear()
# print(languages_programmers)

languages_programmers = {'JavaSript': 'Brendan Eich', 'Python': 'Guido van Rossum', 'Ruby': 'Yukihiro Matsumoto'}
# print('Ruby' in languages_programmers)  # True
# print(languages_programmers['Ruby'])  # printing value by the key

# print(languages_programmers.get('Ruby'))  # To avoid errors we can use get()
# print(languages_programmers.get('PHP', 'PHP not in dictionary.'))  # Also we can use optional value
# print(languages_programmers.get('PHP')) # Else we get None

light_signals = {'green': 'go', 'yellow': 'get ready', 'red': 'stop'}
interactive_presentation_of_keys = light_signals.keys()  # getting keys
list_of_keys = list(light_signals.keys())  # getting keys and save them to list
# print(interactive_presentation_of_keys)
# print(list_of_keys)

list_of_values = list(light_signals.values())  # getting values
# print(list_of_values)
list_of_dict_items = list(light_signals.items())
# print(list_of_dict_items)

periodic_table = {'Hydrogen': 1, 'Helium': 2}
print(periodic_table)
carbon = periodic_table.setdefault('Ferrum', 26)  # If 'Ferrum' is not in the dict, it will be added to.
print(periodic_table)
print(carbon)

