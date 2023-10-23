from datetime import date


"""
Завдання №2
"""
"""

"""
"""
month_dict = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}
month = 2
year = 2024
d1 = date(year,month,1)
def leap_year(year: int):
    if (year % 400 == 0) and (year % 100 == 0):
        print(f'{year} is a leap year')
        return True
    elif (year %4 == 0) and (year % 100 != 0):
        print(f'{year} is a leap year')
        return True
    else:
        print(f'{year} is not a leap year')
        return False
    
if leap_year(year) == False:   
    print(f"{month} has {month_dict.get(month)} days11")
elif month == 2:
    print(f'{month} has a 29 days')
else:
    print(f"{month} has {month_dict.get(month)} days")


#leap_year(1985)
"""
"""
Завдання №1
"""
"""


current_date = datetime.now()

date = datetime(year=2021, month=10, day=9)
new_date = str(date).split(' ')
new_new_date = new_date[0]
# new_new_date = new_new_date.split('-')
# print(new_new_date)
user_date = datetime.strptime(new_new_date,'%Y-%m-%d')
print(user_date.date())

delta_days = current_date - user_date
print(delta_days.days)
#print(type(user_date))
"""