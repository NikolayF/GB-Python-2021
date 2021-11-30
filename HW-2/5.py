my_list = [7, 5, 3, 3, 2]
user_num = input('Введите целое число, для добавления в список: ')
try:
    int_num = int(user_num)
except ValueError:
    print('Нужно ввести целое число!')
if type(int_num) == int:
    for index, value in enumerate(my_list):
        if value == int_num:
            my_list.insert(my_list.index(int_num), int_num)
            break
        elif (value >= int_num) == False:
            my_list.insert(my_list.index(value), int_num)
            break
        elif index == len(my_list) - 1:
            my_list.append(int_num)
            break
print(my_list)