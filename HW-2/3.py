#Решенние через List
# month_list = [1, 'Зима',
#               2, 'Зима',
#               3, 'Весна',
#               4, 'Весна',
#               5, 'Весна',
#               6, 'Лето',
#               7, 'Лето',
#               8, 'Лето',
#               9, 'Осень',
#               10, 'Осень',
#               11, 'Осень',
#               12, 'Зима']
# user_month = input('Введите номер месяца от 1 до 12: ')
# try:
#     num_month = int(user_month)
# except ValueError:
#     print('Нужно ввести целое число!')
# if num_month > 0 and num_month <= 12:
#     print(month_list[num_month * 2 - 1])
# else:
#     print('Номер месяца от 1 до 12! Месяца с номером', num_month, 'не существует!')

#Решение через Dict

month_dict = {1: 'Зима',
              2: 'Зима',
              3: 'Весна',
              4: 'Весна',
              5: 'Весна',
              6: 'Лето',
              7: 'Лето',
              8: 'Лето',
              9: 'Осень',
              10: 'Осень',
              11: 'Осень',
              12: 'Зима'
              }
user_month = input('Введите номер месяца от 1 до 12: ')
try:
    num_month = int(user_month)
except ValueError:
    print('Нужно ввести целое число!')
if num_month > 0 and num_month <= 12:
    print(month_dict[num_month])
else:
    print('Номер месяца от 1 до 12! Месяца с номером', num_month, 'не существует!')