from datetime import date, datetime, timedelta
# users = [
#         {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
#         {"name": "O Ku", "birthday": datetime(1923, 10, 25).date()}
#     ]
users = []
empty_dict = {}

def get_birthdays_per_week(users):
    if not users:
        return {}
    else:
        list_monday = []
        list_tuesday = []
        list_wednesday = []
        list_thursday = []
        list_friday = []
        current_date = date.today()
        next_week = current_date + timedelta(days=7)
        for dicts in users:
            name = dicts['name']
            birthday = dicts['birthday']
            temp_birthday = birthday.replace(year=current_date.year)
            if (temp_birthday < current_date):
                temp_birthday = temp_birthday.replace(year=current_date.year + 1)
            if current_date <= temp_birthday <= next_week:
                day_of_week = temp_birthday.strftime('%A')
                if day_of_week == 'Monday':
                    list_monday.append(name)
                elif day_of_week == 'Tuesday':
                    list_tuesday.append(name)
                elif day_of_week == 'Wednesday':
                    list_wednesday.append(name)
                elif day_of_week == 'Thursday':
                    list_thursday.append(name)
                elif day_of_week == 'Friday':
                    list_friday.append(name)
                elif day_of_week == 'Saturday':
                    list_monday.append(name)
                elif day_of_week == 'Sunday':
                    list_monday.append(name)
        result_dict = {
            'Monday': list_monday,
            'Tuesday': list_tuesday,
            'Wednesday': list_wednesday,
            'Thursday': list_thursday,
            'Friday': list_friday
        }
        for key in list(result_dict.keys()):
            if len(result_dict[key]) == 0:
                del result_dict[key]
    return result_dict




if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
