from datetime import datetime

date = '2021-05-27 17:08:34.149Z'

def get_str_date(date):
    format_date = datetime.fromisoformat(date)
    format_date = datetime.strftime(format_date,'%A %d %B %Y')
    print(format_date)

get_str_date('2021-05-27 17:08:34.149Z')