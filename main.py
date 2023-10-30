from datetime import date, datetime
# users = [
#         {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
#         {"name": "O Ku", "birthday": datetime(1923, 10, 25).date()}
#     ]
users = []
empty_dict = {}

def get_birthdays_per_week(users):
    # Реалізуйте тут домашнє завдання
    today = date.today()
    week_delta = None

    for user in users:
        some_date = (user.get('birthday'))
        if some_date < today:
            #print(f'This date {some_date} was in the past ')
            return empty_dict
    if not users:
        return empty_dict
    
    return users


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
