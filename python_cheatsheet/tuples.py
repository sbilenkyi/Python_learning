empty_tuple = ()  # tuple
# print(type(empty_tuple))

tuple_with_one_element = "item",  # coma, after!
# print(type(tuple_with_one_element))

tuple_sequence = "item1", "item2", "item3"
# print(tuple_sequence)

a, b, c = tuple_sequence
# print(a, b, c, sep='\n')

currency_units = ["pound", "dollar", "euro"]
currency_units = tuple(currency_units)  # tuple function for type conversion
# print(currency_units)


