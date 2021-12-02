import random as r
end_param = 10
count = 0
total_sum = 0
with open('5.txt', 'w') as f:
    while count < end_param:
        f.write(f'{str(r.randint(0, 101))} ')
        count += 1

with open('5.txt', 'r') as f:
    for elem in f.read().split(' '):
        if elem != '':
            total_sum += int(elem)

print(f'Сумма чисел в документе = {total_sum}')