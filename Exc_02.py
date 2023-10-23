from datetime import date


def get_days_in_month(month, year):
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
        print(f"{month} has {month_dict.get(month)} days")
        return month_dict.get(month)
    elif month == 2:
        print(f'{month} has a 29 days')
        return 29
    else:
        print(f"{month} has {month_dict.get(month)} days")
        return month_dict.get(month)
    
print(get_days_in_month(3,2024))