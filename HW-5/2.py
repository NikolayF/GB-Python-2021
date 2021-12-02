data_list = []
count_rows = 0
count_words = 0
with open('2.txt', 'r', encoding = 'UTF-8') as f:
    file_data = '0'
    while file_data != '':
        file_data = f.readline()
        data_list.append(file_data.replace('\n', ''))

for data in data_list:
    if data == '':
        break
    count_words = len(data.split(' '))
    count_rows += 1
    print(f'В {count_rows} строке содержится {count_words} слов')

print(f'Всего строк в файле {count_rows}')

