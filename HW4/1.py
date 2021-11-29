def price_calc(hours, weight, prime):
    return (hours * weight) + prime

employee_dict = ["часы", "ставку", "премию"]
employee_list = []
errors_count = 0
for i in employee_dict:
    user_input = input(f"Введите {i} сотрудника - ")
    try:
        employee_list.append(float(user_input))
    except ValueError:
        print("Необходимо ввести число!")
        errors_count += 1
        break
if errors_count == 0:
    print(price_calc(*employee_list))


