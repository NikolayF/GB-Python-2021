user_goods_cort = ()
user_goods_dict = {}
user_good_list = []
name_list = []
price_list = []
count_list = []
ed_list = []
group_goods_dict = {}
group_count = 0
count_param = 1
input_param_end = ''
while input_param_end != '-1':
    input_param_name = input('Введите название товара: ')
    input_param_price = input('Введите цену товара: ')
    input_param_count = input('Введите количество товара: ')
    input_param_ed = input('Введите в чем измеряется товар: ')
    user_goods_dict = {'Название': input_param_name, 'Цена':input_param_price, 'Количество':input_param_count, 'Ед':input_param_ed}
    user_goods_cort = (count_param, user_goods_dict)
    user_good_list.append(user_goods_cort)
    count_param += 1
    input_param_end = input('Введите -1 для завершения или нажмите Enter для продолжения ввода товаров ')
    if input_param_end == '-1':
        break
print('Готовая структура, которую вы ввели: ', user_good_list)
for i in user_good_list:
    name_list.append(user_good_list[group_count][1]['Название'])
    price_list.append(user_good_list[group_count][1]['Цена'])
    count_list.append(user_good_list[group_count][1]['Количество'])
    ed_list.append(user_good_list[group_count][1]['Ед'])
    group_count += 1
group_goods_dict = {'Название': name_list, 'Цена':price_list, 'Количество':count_list, 'Ед':ed_list}
print('Аналитический словарь: ', group_goods_dict)
