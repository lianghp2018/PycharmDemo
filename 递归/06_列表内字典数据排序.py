students = [
    {'name': 'TOM', 'age': 20},
    {'name': 'Lily', 'age': 21},
    {'name': 'Jack', 'age': 18}
]

# sort(key=lambda...., reverse=bool) reverse默认为False,升序
students.sort(key=lambda a: a['name'])
print(students)
students.sort(key=lambda b: b['age'], reverse=True)
print(students)
