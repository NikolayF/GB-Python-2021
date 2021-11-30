#Задание 3

def my_func(a, b, c):
    sum_num = max(a, b, c) + max(min(a, b), min(a, c), min(c, b))
    print(sum_num)

my_func(1, 2, 3)
