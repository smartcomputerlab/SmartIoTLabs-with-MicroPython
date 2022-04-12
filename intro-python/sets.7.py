s = {1, "String", ('1', 'Tuple'), 1, 2}
print(s)        # {1, 'String', 2, ('1', 'Tuple')}
s.add(1)
print(s)        # {1, 'String', 2, ('1', 'Tuple')}
s.add(3)
print(s)        # {1, 'String', 3, 2, ('1', 'Tuple')}
s.remove(1)
print(s)        # {'String', 3, 2, ('1', 'Tuple')}
# remove throws an exception and discard just ignores any attempt to remove non existent element
s.discard("Strings")
print(s)        # {'String', 3, 2, ('1', 'Tuple')}
s.pop()
print(s)        # {3, 2, ('1', 'Tuple')}
s.clear()
print(s)        # set()