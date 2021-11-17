user_num = input('Введите целое положительное число: ')
max_num = 0
user_num_int = -1
try:
    user_num_int = int(user_num)
except ValueError:
    print('Вы ввели не целое число')
if type(user_num_int) == int and user_num_int >= 0:
    while user_num_int > 0:
        search_num = user_num_int % 10
        if search_num >= max_num:
            max_num = search_num
        user_num_int = user_num_int // 10
    print(max_num)
else:
    print('Вы ввели не положительное число')
print('Конец программы')
