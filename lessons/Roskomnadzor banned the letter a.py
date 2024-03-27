word = input() + ' запретил букву'
alph = [chr(i) for i in range(1072, 1104) if chr(i) != 'ё']
for x in alph:
  if x in word:
    print(word, x)
    word = word.replace(x, '').replace('  ', ' ').strip()


'''
word = input() + ' запретил букву'
alpha = [chr(i) for i in range(1072, 1104)]

for letter in alpha:
    if letter in word:
        print(word, letter)
        word = word.replace(letter, '').replace('  ', ' ').strip()


word = input() + ' запретил букву'
alpha = [chr(i) for i in range(1072, 1104)]

for letter in alpha:
    if letter in word:
        print(word, letter)
        word = word.replace(letter, '').replace('  ', ' ').strip()


word = input() + ' запретил букву'

# Создаем множество для хранения уникальных букв
unique_letters = set(word.replace(' ', ''))  # Игнорируем пробелы во входной строке

# Проходим по каждой букве в отсортированном порядке
for letter in sorted(unique_letters):
    # Выводим предложение с "запретил букву" и текущей буквой
    print(f"{word} {letter}")

    # Удаляем текущую букву из слова
    word = word.replace(letter, '')  # Удаляем только одно вхождение текущей буквы

# Выводим последнюю строку, когда слово стало пустым
print(' '.join(word.strip().split()))

word = input() + ' запретил букву'

# Создаем множество для хранения уникальных букв
unique_letters = set(word.replace(' ', ''))  # Игнорируем пробелы во входной строке

# Проходим по каждой букве в отсортированном порядке
for letter in sorted(unique_letters):
    # Формируем строку без лишних пробелов
    output_string = ' '.join(word.strip().split())

    # Выводим предложение с "запретил букву" и текущей буквой
    print(f"{output_string} {letter}")

    # Удаляем текущую букву из слова
    word = word.replace(letter, '')  # Удаляем только одно вхождение текущей буквы

# Выводим последнюю строку, когда слово стало пустым
print(word)

word = input() + ' запретил букву'
for c in 'абвгдежзийклмнопростуфхцчшщъыьэюя':
    if c in word:
        print(word, c)
        word = word.replace(c, '').strip().replace('  ', ' ')

word = input() + ' запретил букву'
alphabet = ''.join([chr(i) for i in range(1072, 1104)])

for bukva in alphabet:
    #проверяю вхождение буквы алфавита в строку
    if bukva in word:
        print(word.strip() + " " + bukva)
    else:
        continue
    # разбиваю строку на список слов
    spisok = word.split()

    #print(spisok)

    for n in range(len(spisok)):
        if bukva in spisok[n]:
            spisok[n] = spisok[n].replace(bukva,'')

        else:
            continue
    #print(spisok)
    #word = " ".join(spisok)   
    slovo = ''
    for i in range(len(spisok)):
        if len(spisok[i]) == 0:
            continue
        else:
            slovo += spisok[i] + " "

    word = slovo

def bukva(word):
    word1 = 'запретил'
    word2 = 'букву'
    for i in range(1072,1104):
        if chr(i) in word or chr(i) in word1 or chr(i) in word2:
            if word.strip() == '' and word1.strip() == '' and word2.strip() != '':
                    print(word2.strip(), chr(i))
            if word.strip() == '' and word1.strip() != '' and word2.strip() != '':
                print(word1.strip(), word2.strip(), chr(i))
            if word1.strip() == '' and word.strip() != '' and word2.strip() != '':
                print(word.strip(), word2.strip(), chr(i))
            if word.strip() != '' and word1.strip() == '' and word2.strip() == '':
                print(word.strip(), chr(i))
            if word.strip() != '' and word1.strip() != '' and word2.strip() != '':
                print(word.strip(), word1.strip(), word2.strip(), chr(i))
            word = word.replace(chr(i), '').strip()
            word1 = word1.replace(chr(i), '').strip()
            word2 = word2.replace(chr(i), '').strip()

bukva(input())


word = input() + ' запретил букву'
for i in 'абвгдежзийклмнопрстуфхцчшщъыьэюя':
    if i in word:
        print(word, i)
        word = word.replace(i, '').strip().replace('  ', ' ')

def song(word):
    def find_next_letter(check):   # функция поиска следующей буквы
        clean_word = ''.join(check.split())
        return chr(min([ord(i) for i in clean_word]))
    def song_stop(check, symbol):   # функция стоп для цикла while
        clean_word = ''.join(check.split())
        for i in clean_word:
            if i != symbol:
                return False
        return True
    word = word + ' запретил букву'   # цикл вывода на печать
    letter = find_next_letter(word)
    while song_stop(word, letter) is False:
        print(word, letter)
        word = ' '.join(word.replace(letter, '').split())
        letter = find_next_letter(word)
    print(word, letter)
song(input())

for i in sorted(set(w := input()+' запретил букву'))[1:]: print(' '.join(w.split()) + 0*(w := w.replace(i, '')), i)
'''