user_numbers = ('первое число', 'второе число')
numbers_mass = []
def divide_func(first_num, second_num):
    try:
        first_num = int(first_num)
        second_num = int(second_num)
        if second_num == 0:
            print('Делить на 0 нельзя!')
        else:
            print(f'{first_num} / {second_num} = {first_num / second_num}')
    except ValueError:
        print('Нужно ввести число!')

for user_number in user_numbers:
    numbers_mass.append(input(f'Введите {user_number} - '))

divide_func(numbers_mass[0], numbers_mass[1])

