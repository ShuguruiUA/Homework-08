from datetime import date, datetime, timedelta

users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
        {"name": "O Ku", "birthday": datetime(1923, 10, 25).date()},
        {"name": "M Ond", "birthday": datetime(2023, 10, 29).date()},
        {"name": "S Und", "birthday": datetime(2023, 10, 30).date()},
    ]

def get_birthdays_per_week(users):
    # Реалізуйте тут домашнє завдання
    today = date.today()
    week_delta = None
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    empty_dict = {}
    birthday_dict ={}
    birthday_name_list_Monday = []
    birthday_name_list_Tuesday = []
    birthday_name_list_Wednesday = []
    birthday_name_list_Thursday = []
    birthday_name_list_Friday = []

    for user in users:
        some_date = (user.get('birthday'))
        new_date = date(today.year, some_date.month, some_date.day)

        if new_date >= today:
            if datetime.strftime(some_date,'%A') == days[0]:
                birthday_name_list_Monday.append(user.get('name').split()[0])
                #print(birthday_name_list_Monday)
            elif datetime.strftime(some_date,'%A') == days[1]:
                birthday_name_list_Tuesday.append(user.get('name').split()[0])
                #print(birthday_name_list_Tuesday)
            elif datetime.strftime(some_date,'%A') == days[2]:
                birthday_name_list_Wednesday.append(user.get('name').split()[0])
                #print(birthday_name_list_Wednesday)
            elif datetime.strftime(some_date,'%A') == days[3]:
                birthday_name_list_Thursday.append(user.get('name').split()[0])
                #print(birthday_name_list_Thursday)
            elif datetime.strftime(some_date,'%A') == days[4]:
                birthday_name_list_Friday.append(user.get('name').split()[0])
                #print(birthday_name_list_Friday)
            elif datetime.strftime(some_date,'%A') not in days:
                birthday_name_list_Monday.append(user.get('name').split()[0])
                #print(birthday_name_list_Monday)
        elif new_date < today:
            #print(f'This date {new_date} was in the past ')
            return f'First{empty_dict}'
    if birthday_name_list_Monday:
        birthday_dict.update({days[0]:birthday_name_list_Monday})
        print(f'{birthday_name_list_Monday} not empty')
    if birthday_name_list_Tuesday:
        birthday_dict.update({days[1]:birthday_name_list_Tuesday})
        print(f'{birthday_name_list_Tuesday} not empty')
    if birthday_name_list_Wednesday:
        birthday_dict.update({days[2]:birthday_name_list_Wednesday})
        print(f'{birthday_name_list_Wednesday} not empty')
    if birthday_name_list_Thursday:
        birthday_dict.update({days[3]:birthday_name_list_Thursday})
        print(f'{birthday_name_list_Thursday} not empty')
    if birthday_name_list_Friday:
        birthday_dict.update({days[4]:birthday_name_list_Friday})
        print(f'{birthday_name_list_Friday} not empty')

    if not users:
        return f'Second {birthday_dict}'
    
    return birthday_dict


if __name__ == '__main__':
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
        {"name": "O Ku", "birthday": datetime(1923, 10, 25).date()},
        {"name": "M Ond", "birthday": datetime(2023, 10, 29).date()},
        {"name": "S Und", "birthday": datetime(2023, 10, 30).date()},
    ]
    print(get_birthdays_per_week(users))