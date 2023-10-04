students = {'John':['Python', 'Django', 'DRF'], 'Bob':['Java', 'Spring'], 'Jim':['js', 'node', 'react']}
keys = students.keys()
# the first loop will give us one key at a time.
# with the second we are retrieving this list and looping through that list.
for each_Key in keys:
    print('Courses taken by', each_Key, 'are:' )
    for each_course in students[each_Key]:
        print(each_course)
