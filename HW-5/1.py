with open('1.txt', 'w') as f:
    user_input = '0'
    while user_input != '':
        user_input = input('Введите строку для добавления в файл или оставьте пустую строку для завершения - ')
        f.writelines(f'{user_input}\n')
