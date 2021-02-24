

print('\nзадание 1','\n')
# Необходимо вывести имена всех учеников из списка с новой строки

names = ['Оля', 'Петя', 'Вася', 'Маша']
name ='\n'.join(names[0:5])
names_one = str(name).split()
for i in names_one:
    print(i)

print('\nзадание 2','\n')
# Необходимо вывести имена всех учеников из списка, рядом с именем показать количество букв в нём.

names = ['Оля', 'Петя', 'Вася', 'Маша']
name ='\n'.join(names[0:5])
names_one = str(name).split()
for i in names_one:
    print(i, len(i))

print('\nзадание 3','\n')
# Необходимо вывести имена всех учеников из списка, рядом с именем вывести пол ученика


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
# Даны группу учеников. Нужно вывести количество групп и для каждой группы – количество учеников в ней
# Пример вывода:
# Всего 2 группы.
# В группе 2 ученика.
# В группе 3 ученика.

groups = [
    ['Вася', 'Маша'],
    ['Оля', 'Петя', 'Гриша'],
    ]
groups_count = len(groups)

print(f'Всего {groups_count} группы')
for i in range(groups_count):
    print(f'В группе {len(groups[i])} ученика.')


print('\nзадание 5','\n')
# Для каждой пары учеников нужно с новой строки перечислить учеников, которые в неё входят.
# Пример:
# Группа 1: Вася, Маша
# Группа 2: Оля, Петя, Гриша


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
