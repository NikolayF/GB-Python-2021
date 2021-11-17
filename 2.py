user_seconds = input('Введите количество секунд: ')
try:
    user_seconds = int(user_seconds)
except ValueError:
    print('Вы ввели не целове число')
if type(user_seconds) == int and user_seconds < 0:
    print('Введите положительное число')
elif type(user_seconds) == int:
    total_hours = user_seconds // 3600
    total_minutes = (user_seconds // 60) % 60
    total_second = user_seconds % 60
    if total_hours < 10:
        total_hours = '0' + str(total_hours)
    if total_minutes < 10:
        total_minutes = '0' + str(total_minutes)
    if total_second < 10:
        total_second = '0' + str(total_second)
    print('%s:%s:%s' % (total_hours, total_minutes, total_second))
print('Конец программы')

