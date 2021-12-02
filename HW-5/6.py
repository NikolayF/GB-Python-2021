data_list = []
output_dict = {}
sum_hours = 0
with open('6.txt', 'r', encoding = 'UTF-8') as f:
    file_data = '0'
    while file_data != '':
        file_data = f.readline()
        data_list.append(file_data.replace('\n', ''))
data_list.pop(-1)
for data in data_list:
    sum_hours = 0
    for item in data.split(' '):
        if item.split('(')[0].isdigit():
            sum_hours += int(item.split('(')[0])
        output_dict.update({str(data.split(' ')[0]): str(sum_hours)})
print(output_dict)