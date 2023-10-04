# set does not allow duplicates
s = {10, 20, 30, 'xyz'}
print(type(s))
s.update([88, 99])

print(s)

# no order, no indexing, no slicing, no repetition
s.remove(30)
print(s)

# frozen set
# no update, no remove
f = frozenset(s)
