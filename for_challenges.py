

print('\nзадание 1','\n')

names = ['Оля', 'Петя', 'Вася', 'Маша']
name ='\n'.join(names[0:5])
names_one = str(name).split()
for i in names_one:
    print(i)

print('\nзадание 2','\n')

names = ['Оля', 'Петя', 'Вася', 'Маша']
name ='\n'.join(names[0:5])
names_one = str(name).split()
for i in names_one:
    print(i, len(i))

print('\nзадание 3','\n')

is_male = {
  'Оля': False,  # если True, то пол мужской
  'Петя': True,
  'Вася': True,
  'Маша': False,
}


for key, value in is_male.items():
    if value == False:
        print(key, 'female')
    else:
        print(key, 'male')


print('\nзадание 4','\n')

groups = [
    ['Вася', 'Маша'],
    ['Оля', 'Петя', 'Гриша'],
    ]
groups_count = len(groups)

print(f'Всего {groups_count} группы')
for i in range(groups_count):
    print(f'В группе {len(groups[i])} ученика.')


print('\nзадание 5','\n')


groups = [
  ['Вася', 'Маша'],
  ['Оля', 'Петя', 'Гриша'],
]
dots = ', '
str1 = dots.join(groups[0])
str2 = dots.join(groups[1])
for i in range(1):
    print('Группа 1:', str1, end='\n')
    for j in range(1):
        print('Группа 2:', str2, end='\n')
