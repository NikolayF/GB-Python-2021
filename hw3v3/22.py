user_details = {'имя': '', 'фамилия': '', 'год рождения': '', 'город проживания': '', 'email': '', 'телефон': ''}

def user_info(name, last_name, year, city, email, phone):
    print(f'Вас зовут {name}, фамилия {last_name}, год рождения {year}, город {city}, почта {email}, телефон {phone}')

for user_detail in user_details:
    user_details[user_detail] = input(f'Введите {user_detail} - ')

user_info(name = user_details['имя'], last_name = user_details['фамилия'], year = user_details['год рождения'], city = user_details['город проживания'], email = user_details['email'], phone = user_details['телефон'],)
