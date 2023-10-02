lst = [10, 20, 'Alina', -10, 30.5]
print(lst)
print(lst[3])
print(lst[3:5])
print(lst * 4)
print(len(lst))

# methods
lst.append(40)
lst.remove("Alina") # remove an element by its value
del(lst[1]) # It is not a function on the list, but it is the inbuilt function in Python
print(lst)

#lst.clear()
#print(lst)

max(lst)
print(max(lst))
print(min(lst))
lst.insert(3, 99) # index, value
print(lst)
lst.sort() # crescator
print(lst)
lst.sort(reverse=True) # descrescator
print(lst)