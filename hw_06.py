from datetime import date, datetime 

users = [
         {"name": "Jan Koum", "birthday": datetime(2023, 11, 1).date()},
    ]


# d = {'coding': 'good', 'thinking': 'better'}
# print(d.get('coding'))

today = date.today()
#print(today)


for birthday in users:
    some_date = (birthday.get('birthday'))
    if some_date.month < today.month:
        print(f'This date {some_date} was in the past')
    else:
        print(f'It will be in future')
        print(datetime.strftime(some_date,'%A'))

# if some_date.month > today.month:
#     print(birthday.get('name'))
    # for value in user.values():
    #     print(user.get('birthday'))

# empty_list = (1,2,3)
# print(len(empty_list))
# if not empty_list:
#     print(False)
# else:
#     print(True)