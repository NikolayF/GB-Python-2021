def int_func(word):
    return(word[0].upper() + word[1:])
out_list = []
user_words = input('Введите слова в нижнем регистре, разделяя их пробелами - ')
words_list = user_words.split()
for word in words_list:
    out_list.append(int_func(word))

print(' '.join(out_list))
