from datetime import datetime

date = '2021-05-27 17:08:34.149Z'

def get_str_date(date):
    str_to_iso = datetime.strptime(date,'%Y-%m-%d %H:%M:%S.%f%z')
    format_date = datetime.strftime(str_to_iso,'%A %d %B %Y')
    print(format_date)

get_str_date('2021-05-27 17:08:34.149Z')