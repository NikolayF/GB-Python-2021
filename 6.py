first_day_distance = input('Введите число километров, которое пробежал спортсмен в первый день: ')
total_distance = input('Введите число километров, которое должен достигнуть спортсмен: ')
day_param = 1
try:
    first_day_distance = int(first_day_distance)
except ValueError:
    print('Вы ввели не число, которое пробежал спортсмен в первый день')
try:
    total_distance = int(total_distance)
except ValueError:
    print('Вы ввели не число, которое должен достигнуть спортсмен')
if type(first_day_distance) == int and type(total_distance) == int:
    while first_day_distance < total_distance:
        day_param += 1
        first_day_distance = first_day_distance + (first_day_distance * 0.10)
    print('Спортсмен достиг результата за %s дней' % (day_param))
print('Конец программы')


