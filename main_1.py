from datetime import date, datetime, timedelta
users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
        {"name": "O Ku", "birthday": datetime(1923, 10, 25).date()}
    ]
# users = []
empty_dict = {}


def get_birthdays_per_week(users):
    # Реалізуйте тут домашнє завдання
    today = date.today()
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    week_delta = timedelta(weeks=1)
    new_week = today+week_delta
    birthday_dict ={}
    birthday_name_list_Monday = []
    birthday_name_list_Tuesday = []
    birthday_name_list_Wednesday = []
    birthday_name_list_Thursday = []
    birthday_name_list_Friday = []
    while users:
        for user in users:
            some_date = (user.get('birthday'))
            new_date = some_date.replace(year=today.year)
            if new_date < today and datetime.strftime(new_date,'%A') in days:
                continue
            if today <= new_date < new_week:
                print('today <= new_date <=new_week')
                if datetime.strftime(new_date,'%A') == days[0]:
                    birthday_name_list_Monday.append(user.get('name').split()[0])
                    print(f'{birthday_name_list_Monday} elif')
                elif datetime.strftime(new_date,'%A') == days[1]:
                    birthday_name_list_Tuesday.append(user.get('name').split()[0])
                    print(f'{birthday_name_list_Tuesday} elif')
                elif datetime.strftime(new_date,'%A') == days[2]:
                    birthday_name_list_Wednesday.append(user.get('name').split()[0])
                    print(f'{birthday_name_list_Wednesday} elif')
                elif datetime.strftime(new_date,'%A') == days[3]:
                    birthday_name_list_Thursday.append(user.get('name').split()[0])
                    print(f'{birthday_name_list_Thursday} elif')
                elif datetime.strftime(new_date,'%A') == days[4]:
                    birthday_name_list_Friday.append(user.get('name').split()[0])
                    print(f'{birthday_name_list_Friday} elif')
                elif datetime.strftime(new_date,'%A') not in days:
                    birthday_name_list_Monday.append(user.get('name').split()[0])
                    print(f'{birthday_name_list_Monday} elif') 
            # elif new_date < today and datetime.strftime(new_date,'%A') in days:
            #     continue
            # else:
            #     print('else')
            #     if datetime.strftime(new_date,'%A') == days[0]:
            #         birthday_name_list_Monday.append(user.get('name').split()[0])
            #         print(birthday_name_list_Monday)
            #     elif datetime.strftime(new_date,'%A') == days[1]:
            #         birthday_name_list_Tuesday.append(user.get('name').split()[0])
            #         print(birthday_name_list_Tuesday)
            #     elif datetime.strftime(new_date,'%A') == days[2]:
            #         birthday_name_list_Wednesday.append(user.get('name').split()[0])
            #         print(birthday_name_list_Wednesday)
            #     elif datetime.strftime(new_date,'%A') == days[3]:
            #         birthday_name_list_Thursday.append(user.get('name').split()[0])
            #         print(birthday_name_list_Thursday)
            #     elif datetime.strftime(new_date,'%A') == days[4]:
            #         birthday_name_list_Friday.append(user.get('name').split()[0])
            #         print(birthday_name_list_Friday)
            #     elif datetime.strftime(new_date,'%A') not in days:
            #         birthday_name_list_Monday.append(user.get('name').split()[0])
            #         print(birthday_name_list_Monday) 
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
            return f'Empty list {empty_dict}'
        
        return f'There are should be something {birthday_dict}'


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")

    print(get_birthdays_per_week([
    {"name": "Bill", "birthday": datetime(1955, 10, 28).date()},
    {"name": "Jan", "birthday": datetime(1981, 10, 28).date()},
    {"name": "Kim", "birthday": datetime(2005, 11, 1).date()},
    {"name": "Maxim", "birthday": datetime(2000, 2, 26).date()},
    {"name": "Anna", "birthday": datetime(2012, 10, 27).date()}
    ]))
    print(get_birthdays_per_week([]))
    print(get_birthdays_per_week([
        {"name": "Bill", "birthday": datetime(1955, 8, 28).date()},
        {"name": "Jan", "birthday": datetime(1981, 5, 28).date()},
        {"name": "Kim", "birthday": datetime(2005, 10, 1).date()},
        {"name": "Maxim", "birthday": datetime(2000, 2, 26).date()},
        {"name": "Anna", "birthday": datetime(2012, 4, 27).date()}
    ]))
    print(get_birthdays_per_week([
        {"name": "Bill", "birthday": datetime(1955, 12, 29).date()},
        {"name": "Jan", "birthday": datetime(1981, 12, 30).date()},
        {"name": "Kim", "birthday": datetime(2005, 1, 2).date()},
        {"name": "Maxim", "birthday": datetime(2000, 2, 26).date()},
        {"name": "Anna", "birthday": datetime(2012, 12, 27).date()}
    ]))