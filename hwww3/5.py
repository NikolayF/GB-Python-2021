#Задание 5

sum_out = 0
exit_param = ''
while exit_param != '@':
    user_nums = input('Введите числа разделяя их пробелами и нажмите Enter для отображения суммы,\nесли введёте @ программа остановится - ')
    num_list = user_nums.split()
    for num in num_list:
        try:
            exit_param = num
            if num == '@':
                break
            num = int(num)
            sum_out += num
        except ValueError:
            print('Нужно вводить числа!')
    print(sum_out)

