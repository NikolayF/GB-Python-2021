from itertools import count, cycle
#Использование Count
iterator_list_count = []
iterator_list_cycle = []
def iterator_count(num, end_num):
    for i in count(num):
        iterator_list_count.append(i)
        if i == end_num:
            break
        i += 1

iterator_count(4, 10)

#Использование Cycle
data = [1, 2, 3, 4, 5, 6]
def iterator_cycle(list, end_count):
    count = 1
    for i in cycle(list):
        iterator_list_cycle.append(i)
        if count == end_count:
            break
        count += 1

iterator_cycle(data, 10)

print(iterator_list_count)
print(iterator_list_cycle)
