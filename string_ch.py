
print('\nзадание 1','\n')
# Вывести количество букв "а" в слове

word = 'Архангельск'
word_a = word.lower()
bykvy = ('а')
count =0
for i in word_a:
    if i in bykvy:
        count +=1
print(count)

print('\nзадание 2','\n')
# Вывести количество гласных букв в слове

word = 'Архангельск'
word_a = word.lower()
bykvy = ('а, у, о, ы, и, э, я, ю, ё, е')
count = 0
for i in word_a:
    if i in bykvy:
        count += 1
print(count)

print('\nзадание 3','\n')
# Вывести количество слов в предложении

sentence = 'Мы приехали в гости'
sentence_len = sentence.split()
print(len(sentence_len))

print('\nзадание 4','\n')
# Вывести первую букву каждого слова на отдельной строке

sentence = 'Мы приехали в гости'
print('\n'.join(sentence[0].lower() for sentence in sentence.split()))


print('\nзадание 5','\n')

# Вывести усреднённую длину слова.

sentence = 'Мы приехали в гости'
count = 0 
sentence_len = sentence.split()
sentence_l = len(sentence_len)
for i in sentence_len:
    count += len(sentence_len)

print(count/sentence_l)
