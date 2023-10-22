from datetime import datetime


def get_days_from_today(date):
    current_date = datetime.now()
    new_date = str(date).split(' ')
    new_new_date = new_date[0]
    user_date = datetime.strptime(new_new_date,'%Y-%m-%d')
    delta_days = current_date - user_date
    print(delta_days.days)
    return delta_days.days