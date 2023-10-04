# list
countries = ['Romania', 'Italy', 'France']
print(countries)
countries.append('Spain')
print(countries)
# countries.pop(3)
del(countries[3])
print(countries)
countries.insert(2, 'Portugal')
print(countries)

# set
countries = {'Romania', 'Italy', 'France'}
print(countries)
countries.update(['Spain'])
print(countries)
countries.remove('France') # sets do not have index. removing is possible only by values
print(countries)
countries.update(['Portugal']) # sets have no order
print(countries)