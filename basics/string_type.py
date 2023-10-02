s = '   you are awesome   '
print(s)
# That is how we define a string across lines.
s1 = """You are
the creator 
of you destiny"""
print(s1)
# Indexing is the concept of reaching out to a particular character or location in a string for example.
print(s[0])
print(s[2])
# repetition is the process of using the star operator in strings.
print(s*2)
# length function
print(len(s1))
print(len(s))

# slicing
#it does not include the element at the ending index.
print(s[0:5])
print(s[0:])
print(s[:8])
print(s[-3:-1])

# step value
print(s[0:9:2])
print(s[15::-1]) # to reverse the string: -values
print(s[::-1])

# strip function -elimina space-urile
print(s.strip()) # left spaces
print(s.rstrip()) # right spaces

# find function
print(s.find('awe', 0, len(s)))
print(s.find('awe',0,8))
print(s.count('a'))
print(s.replace('awesome', 'super'))
print(s.upper())
print(s.lower())
print(s.title())