import json as js

data_list = []
firm_dict = {}
average_dict = {}
sum_for_average = 0
count_firm = 0
output_list = []

with open('7.txt', 'r', encoding='utf-8') as f:
    file_data = '0'
    while file_data != '':
        file_data = f.readline()
        data_list.append(file_data.replace('\n', ''))
data_list.pop(-1)
for data in data_list:
    if int(data.split(' ')[2]) > int(data.split(' ')[3]):
        firm_dict.update({str(data.split(' ')[0]): int(data.split(' ')[2])})
    if int(data.split(' ')[2]) < int(data.split(' ')[3]):
        firm_dict.update({str(data.split(' ')[0]): -(int(data.split(' ')[3]) - int(data.split(' ')[2]))})
for firm in firm_dict:
    if firm_dict[firm] > 0:
        sum_for_average += firm_dict[firm]
        count_firm += 1

average_dict.update({'average_profit': int(sum_for_average / count_firm)})
output_list.append(firm_dict)
output_list.append(average_dict)

with open('7.json', 'w') as f:
    js.dump(output_list, f)