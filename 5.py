user_income = input('Введите доходы компании: ')
user_expenses = input('Введите расходы компании: ')

try:
    user_income = int(user_income)
except ValueError:
    print('Вы ввели не число в доходы')
try:
    user_expenses = int(user_expenses)
except ValueError:
    print('Вы ввели не число в расходы')
if type(user_income) == int and type(user_expenses) == int:
    if user_income > user_expenses:
        print('Вы работаете в +')
        print('Ваша выручка составляет %s' % (user_income - user_expenses))
        count_employee = input('Введите количество сотрудников фирмы: ')
        try:
            count_employee = int(count_employee)
        except ValueError:
            print('Вы ввели не число в количество сотрудников фирмы')
        if type(count_employee) == int:
            print('Прибыль на каждого сотрудника составляет: %s' % (user_income / count_employee))
            print('Выручка на каждого сотрудника составляет: %s' % ((user_income - user_expenses) / count_employee))
    elif user_income < user_expenses:
        print('Вы работаете в -')
    else:
        print('Вы работаете в 0')
print('Конец программы')
