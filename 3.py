user_num = input('Введите целое число: ')
try:
    user_num_int = int(user_num)
except ValueError:
    print('Вы ввели не целое число')
if type(user_num_int) == int:
    value1 = user_num_int
    value2 = int(user_num * 2)
    value3 = int(user_num * 3)
    print(value1 + value2 + value3)
print('Конец программы')
