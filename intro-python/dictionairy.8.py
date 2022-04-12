d = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
print(d)           # {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
print(d['key1'])   # value1
d['key7'] = 'value7'
print(d)           # {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key7': 'value7'}
del d['key7']
print(d)           # {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
d['key1'] = 'New Value 1'
print(d)           # {'key1': 'New Value 1', 'key2': 'value2', 'key3': 'value3'}
