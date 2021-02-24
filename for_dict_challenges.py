
print('\nзадание 1','\n')

# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.


students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]

names = [student['first_name'] for student in students] #циклическое извлечение  first_name
for name in set(names): # set создание множества
    print(f'{name}: {names.count(name)}')

print('\nзадание 2','\n')
# Дан список учеников, нужно вывести самое часто повторящееся имя.

students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]

names = [student['first_name'] for student in students] #циклическое извлечение  first_name
for name in set(names):
    if names.count(name) > 1:
        print('Самое повторяющиеся имя среди учеников:', name)

print('\nзадание 3','\n')
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.

school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]

names = [student[0]['first_name'] for student in school_students]  #циклическое извлечение  first_name
for name in set(names):
    name ='\n'.join(names[0:3])
    firstname, lastname = map(str, name.split()) 
print(f'Самое повторяющиеся имя среди 1 класса учеников: {firstname}')
print(f'Самое повторяющиеся имя среди 2 класса учеников: {lastname}')

print('\nзадание 4','\n')
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.

school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}

classes = [cl['class'] for cl in school]  #циклическое извлечение  first_name
for classe in set(classes):
    classe ='\n'.join(classes[0:2])
    first, second = map(str, classe.split())

count_man = 0
count_female = 0
count = 0
for key, value in is_male.items():
    for i in range(1):
        if value == False:
            count_female = count_female + 1
            
        else:
            count_man = count_man + 1

print(f'В классе {first} {count_female} девочки и {count} мальчика.')
print(f'В классе {second} {count} девочек и {count_man} мальчика.')

print('\nзадание 5','\n')
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.

print(f'В {first} больше девочек.')
print(f'В {second} больше мальчиков.')
