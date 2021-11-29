user_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [param for param in user_list if user_list.count(param) == 1]
print(new_list)

