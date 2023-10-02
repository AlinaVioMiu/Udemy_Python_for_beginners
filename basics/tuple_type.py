tpl = (20, 30, 40, 20, "xyz")
tpl2 = (1,) # pentru un sg element, punem virgula
print(type(tpl))
print(tpl*3)
print(tpl.count(20))
print(tpl.index("xyz"))

lst = [67, 34, "xyz"]
print(type(lst))
tpl1 = tuple(lst)
print(tpl1)
print(type(tpl1))