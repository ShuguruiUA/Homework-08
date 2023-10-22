from datetime import date

month = 13
year = 2001

def get_days_in_month(month, year):

    my_tuple = (year,month)
    date = '-'.join(my_tuple)
    print(date)