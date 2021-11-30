#user_list = ['Первый элемент', 'Второй элемент', 3, 4, 5.55, 6.66, True, False, 123]
user_list = []
input_param = ''
while input_param != '-1':
    input_param = input('Введите элемент списка или для завершения введите -1: ')
    if input_param == '-1':
        break
    user_list.append(input_param)
list_len = len(user_list)
start_index = 0
print('Таким список был до изменений: ', user_list)
while start_index < list_len:
    first_elem = user_list[start_index]
    try:
        second_elem = user_list[start_index + 1]
        user_list[start_index] = second_elem
        user_list[start_index + 1] = first_elem
    except IndexError:
        print('Лист нечетный, последний элемент останется на месте')
    start_index += 2
print('Список после изменений: ', user_list)

