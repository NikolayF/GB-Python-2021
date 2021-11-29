num_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [next_el for el, next_el in zip(num_list, num_list[1:]) if el < next_el]

print(new_list)