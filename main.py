from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    # Реалізуйте тут домашнє завдання
    if not users:
        return {}
    else:
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        birthday_name_list_Monday = []
        birthday_name_list_Tuesday = []
        birthday_name_list_Wednesday = []
        birthday_name_list_Thursday = []
        birthday_name_list_Friday = []
        current_day = date.today()
        week_delta= timedelta(weeks = 1)
        week_from_today = current_day + week_delta
        week_before_today = current_day - week_delta
        for user in users:
            user_birthday = (user.get('birthday'))
            user_name = (user.get('name'))
            user_birthday_current_year = user_birthday.replace(year = current_day.year)
            #print(current_day, user_birthday_current_year, week_from_today)
            #print(user_birthday_current_year < week_from_today and user_birthday_current_year > week_before_today and datetime.strftime(user_birthday_current_year,'%A') not in days)
            # if user_birthday_current_year <= week_from_today and datetime.strftime(user_birthday_current_year,'%A') not in days:
            #     print(user_name,'\n',user_birthday)
            if week_before_today <= user_birthday_current_year <= week_from_today and datetime.strftime(user_birthday_current_year,'%A') not in days:
                #print(f'{user_name} has birthdat {user_birthday_current_year}')
                if datetime.strftime(user_birthday_current_year,'%A') == days[0]:
                    birthday_name_list_Monday.append(user.get('name').split()[0])
                elif datetime.strftime(user_birthday_current_year,'%A') == days[1]:
                    birthday_name_list_Tuesday.append(user.get('name').split()[0])
                elif datetime.strftime(user_birthday_current_year,'%A') == days[2]:
                    birthday_name_list_Wednesday.append(user.get('name').split()[0])
                elif datetime.strftime(user_birthday_current_year,'%A') == days[3]:
                    birthday_name_list_Thursday.append(user.get('name').split()[0])
                elif datetime.strftime(user_birthday_current_year,'%A') == days[4]:
                    birthday_name_list_Friday.append(user.get('name').split()[0])
                elif datetime.strftime(user_birthday_current_year,'%A') not in days:
                    birthday_name_list_Monday.append(user.get('name').split()[0])
            elif user_birthday_current_year <= week_from_today:
                print(f'{user_name} has birthdat {user_birthday_current_year}')
                if datetime.strftime(user_birthday_current_year,'%A') == days[0]:
                    birthday_name_list_Monday.append(user.get('name').split()[0])
                elif datetime.strftime(user_birthday_current_year,'%A') == days[1]:
                    birthday_name_list_Tuesday.append(user.get('name').split()[0])
                elif datetime.strftime(user_birthday_current_year,'%A') == days[2]:
                    birthday_name_list_Wednesday.append(user.get('name').split()[0])
                elif datetime.strftime(user_birthday_current_year,'%A') == days[3]:
                    birthday_name_list_Thursday.append(user.get('name').split()[0])
                elif datetime.strftime(user_birthday_current_year,'%A') == days[4]:
                    birthday_name_list_Friday.append(user.get('name').split()[0])
                elif datetime.strftime(user_birthday_current_year,'%A') not in days:
                    birthday_name_list_Monday.append(user.get('name').split()[0])
        print(birthday_name_list_Monday,'\n',birthday_name_list_Tuesday,'\n',birthday_name_list_Wednesday,'\n',birthday_name_list_Thursday,'\n', birthday_name_list_Friday)


    







    return {}


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
        {"name": "Bill", "birthday": datetime(1955, 10, 28).date()},
        {"name": "Jan", "birthday": datetime(1981, 10, 28).date()},
        {"name": "Kim", "birthday": datetime(2005, 11, 1).date()},
        {"name": "Maxim", "birthday": datetime(2000, 2, 26).date()},
        {"name": "Anna", "birthday": datetime(2012, 10, 27).date()}
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")