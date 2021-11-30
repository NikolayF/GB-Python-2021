#Без цикла
def my_root_func(x, y):
    print(x ** y)

my_root_func(3, 6)

#С циклом
def my_root_func_cycle(x, y):
    cycle_num = 1
    return_num = cycle_num * x
    while cycle_num < y:
        return_num = return_num * x
        cycle_num += 1
    print(return_num)

my_root_func_cycle(3, 6)
