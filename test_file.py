# Sort alphabetically
data_base = [
    {'name': 'Susan', 'age': 50},
    {'name': 'Christopher', 'age': 47}
]

data_base.sort(key=lambda item: item['name'])
print('-- alphabetically --')
print(data_base)

# Sort by length of name (shortest to longest)
data_base.sort(key=lambda item: len(item['name']))
print('-- length --')
print(data_base)