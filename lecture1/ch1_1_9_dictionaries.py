"""
Python dictionaries and dictonary methods
"""

random_things = {'major': ['sociology', 'economics'],
                 'shincon_schools': ['Sogang', 'Ewha', 'Yonsei', 'Hongik'],
                 'me': 'Keon Sun'
                 }
# a dictionary unlike lists, is a data type which consists of keys and values
# a dictionary is declared with '{}' at each ends.
# {key1: value1, key1: value2, key3: value3... }

print(f'random_things["me"]= {random_things["me"]}')
# you can access dictionary values by its keys!

try:
    somthing = random_things[1]
    print(something)
except KeyError as e:
    print(e)
# but you cannot access dictionary values by indexes!
# there is a key error 1!!
# also another thing! dictionaries are not guaranteed to stay in order!

# dictioary methods .get(), .values(), .keys(), .items(), .pop(), .len()

print(f'.get() method returns the value of a key! \
    random_things["me"] = {random_things.get("me")}')
# the .get() method returns the value of a given key

print(f'the .values() method returns all the values in \
    the dictionary! random_things.values() = {random_things.values()}')

print(f'the .keys() method returns all the keys in\
    the dictionary! random_things.keys() = {random_things.keys()}')

print(f'the .items() method returns all the keys and values in\
	the dictionary! random_things.items() = {random_things.items()}')
# the items method returns a dict_items data type with all the keys and values
# in the data

popped_val = random_things.pop('me')
print(f'the .pop method returns the value of the given key, and removes the\
	key, values set from the dictionary')
print(f'popped_val={popped_val}, random_things={random_things}')


print(f'len(random_things) = {len(random_things)}')
# the len() returns the number of keys in the dictionary!
