user_words = input('Введите слова, разделяя их пробелами: ')
split_words = user_words.split()
for index, value in enumerate(split_words):
    print('Строка номер %s -' % (index + 1), split_words[index][:10])



