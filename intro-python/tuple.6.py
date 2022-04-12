t = (1, 2, 3)
print(t)         # (1, 2, 3)
t = 1, 2, 3
print(t)         # (1, 2, 3)
t = (1, 2, 'String', (3, 4, "String 2"), [1, 2, 3])
print(t)         # (1, 2, 'String', (3, 4, 'String 2'), [1, 2, 3])
print(t[4])      # [1, 2, 3]
t[4].extend([2, 3, 4])
print(t)         # (1, 2, 'String', (3, 4, 'String 2'), [1, 2, 3, 2, 3, 4])
l = list(t)
print(l)         # [1, 2, 'String', (3, 4, 'String 2'), [1, 2, 3, 2, 3, 4]]
t = tuple(l)
print(t)         # (1, 2, 'String', (3, 4, 'String 2'), [1, 2, 3, 2, 3, 4])
