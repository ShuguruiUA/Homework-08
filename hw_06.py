from datetime import date, datetime 

users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

for user in users:
    for key,value in user.items():
        if value < datetime.now():
            print(value)