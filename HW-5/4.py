data_list = []
leng_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
output_data = []
with open('4.txt', 'r', encoding = 'UTF-8') as f:
    file_data = '0'
    while file_data != '':
        file_data = f.readline()
        data_list.append(file_data.replace('\n', ''))
data_list.pop(-1)

for data in data_list:
    for leng in leng_dict:
      if data.split(' ')[0] == leng:
          data.split(' ')[0] = leng_dict[leng]
          output_data.append(f'{leng_dict[leng]} {"".join(data.split(" ")[1])} {"".join(data.split(" ")[2])}')

with open('4new.txt', 'w') as f:
    for data in output_data:
        f.write(f'{data}\n')

