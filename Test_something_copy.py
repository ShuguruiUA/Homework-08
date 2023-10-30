from datetime import date, datetime, timedelta

# users = [
#         {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
#         {"name": "O Ku", "birthday": datetime(1923, 10, 31).date()},
#         {"name": "M Ond", "birthday": datetime(2023, 10, 29).date()},
#         {"name": "S Und", "birthday": datetime(2023, 10, 30).date()},
#         {"name": "W eek", "birthday": datetime(2012, 11, 6).date()}
#     ]
def get_birthdays_per_week(users):
    today = date.today()
    delta_week = timedelta(weeks=1)
    new_week = today + delta_week
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    birthday_name_list_Monday = []
    birthday_name_list_Tuesday = []
    birthday_name_list_Wednesday = []
    birthday_name_list_Thursday = []
    birthday_name_list_Friday = []
    birthday_dict ={}

    for user in users:
            some_date = (user.get('birthday'))
            new_date = date(today.year, some_date.month, some_date.day)
            if today <= new_date <= new_week:
                if datetime.strftime(new_date,'%A') == days[0]:
                    birthday_name_list_Monday.append(user.get('name').split()[0])
                    #print(birthday_name_list_Monday)
                elif datetime.strftime(new_date,'%A') == days[1]:
                    birthday_name_list_Tuesday.append(user.get('name').split()[0])
                    #print(birthday_name_list_Tuesday)
                elif datetime.strftime(new_date,'%A') == days[2]:
                    birthday_name_list_Wednesday.append(user.get('name').split()[0])
                    #print(birthday_name_list_Wednesday)
                elif datetime.strftime(new_date,'%A') == days[3]:
                    birthday_name_list_Thursday.append(user.get('name').split()[0])
                    #print(birthday_name_list_Thursday)
                elif datetime.strftime(new_date,'%A') == days[4]:
                    birthday_name_list_Friday.append(user.get('name').split()[0])
                    #print(birthday_name_list_Friday)
                elif datetime.strftime(new_date,'%A') not in days:
                    birthday_name_list_Monday.append(user.get('name').split()[0])
                    #print(birthday_name_list_Monday)

            elif new_date < today and new_date in days:
                #continue
                return f'there is no birthdays this week {birthday_dict}'
    if birthday_name_list_Monday:
        birthday_dict.update({days[0]:birthday_name_list_Monday})
        #print(f'{birthday_name_list_Monday} not empty')
    if birthday_name_list_Tuesday:
        birthday_dict.update({days[1]:birthday_name_list_Tuesday})
        #print(f'{birthday_name_list_Tuesday} not empty')
    if birthday_name_list_Wednesday:
        birthday_dict.update({days[2]:birthday_name_list_Wednesday})
        #print(f'{birthday_name_list_Wednesday} not empty')
    if birthday_name_list_Thursday:
        birthday_dict.update({days[3]:birthday_name_list_Thursday})
        #print(f'{birthday_name_list_Thursday} not empty')
    if birthday_name_list_Friday:
        birthday_dict.update({days[4]:birthday_name_list_Friday})
        #print(f'{birthday_name_list_Friday} not empty')               
    return birthday_dict


print(get_birthdays_per_week([
    {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    {"name": "O Ku", "birthday": datetime(1923, 10, 31).date()},
    {"name": "M Ond", "birthday": datetime(2023, 10, 29).date()},
    {"name": "S Und", "birthday": datetime(2023, 10, 30).date()},
    {"name": "W eek", "birthday": datetime(2012, 11, 6).date()}
]))

print(get_birthdays_per_week([
    {"name": "Bill", "birthday": datetime(1955, 10, 28).date()},
    {"name": "Jan", "birthday": datetime(1981, 10, 28).date()},
    {"name": "Kim", "birthday": datetime(2005, 11, 1).date()},
    {"name": "Maxim", "birthday": datetime(2000, 2, 26).date()},
    {"name": "Anna", "birthday": datetime(2012, 10, 27).date()}
]))
#print(get_birthdays_per_week([]))
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