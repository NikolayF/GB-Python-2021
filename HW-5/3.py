data_list = []
users_list = []
money_list = []
middle_money = 0
with open('3.txt', 'r', encoding = 'UTF-8') as f:
    file_data = '0'
    while file_data != '':
        file_data = f.readline()
        data_list.append(file_data.replace('\n', ''))
data_list.pop(-1)
for data in data_list:
    money_list.append(int(data.split(' ')[1]))
    if int(data.split(' ')[1]) < 20000:
        users_list.append(data.split(' ')[0])

for money in money_list:
    middle_money += money
print(f'Сотрудники c зарплатой менее 20.000:')
for user in users_list:
    print(user)
print(f'Средняя зарплата сотрудников составляет - {middle_money / len(data_list)}')
