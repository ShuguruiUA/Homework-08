from datetime import date, datetime, timedelta

def get_birthdays_per_week(users):
    # Реалізуйте тут домашнє завдання

    if not users: #перевіряємо чи список порожній і повертаємо порожній словник, якщо він порожній
        return {}
    else: #якщо список не порожній
        cureent_date = date.today() # визначаємо поточну дату
        birthday_list_Monday = [] # створюємо порожній словник для усіх іменинників, у яких день народження понеділок, або припадає на вихідний день
        birthday_list_Tuesday = [] # створюємо порожній словник для усіх іменинників, у яких день народження вівторок
        birthday_list_Wednesday = [] # створюємо порожній словник для усіх іменинників, у яких день народження середу
        birthday_list_Thursday = [] # створюємо порожній словник для усіх іменинників, у яких день народження четвер
        birthday_list_Friday = [] # створюємо порожній словник для усіх іменинників, у яких день народження п'ятницю
        work_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'] # створюємо список робочих днів тижня для спрощення перевірки
        users_birthday_dict = {} # створюємо порожній словник іменинників
        week_from_today = cureent_date + timedelta(weeks=1) #додаємо тиждень до поточної дати, щоб обмежити кількість днів народження одним тижнем.
        for user in users: # ітеруємося по словнику у списку users
            name = user.get('name') # отримуємо ім'я користувача за ключем зі словника
            birthday = user.get('birthday') # отримуюємо дату народження за ключем зі словника
            birthday_current_year = birthday.replace(year=cureent_date.year) # замінюємо оригінальний рік народження на поточний для подальшої перевірки дати у поточному році.
            if (birthday_current_year<cureent_date): #Перевіряємо чи дата народження з поточним роком менша за поточну дату
                birthday_current_year = birthday_current_year.replace(year=cureent_date.year+1) # якщо повертається True - збільшуємо поточний рік на одиницю, якщо False - продовжємо ітеруватись.
            if cureent_date <= birthday_current_year <= week_from_today: # Робимо перевірку чи день народження у поточному році більше або дорівнює сьогодні та більше або дорівнює наступному тижню.
                week_day = birthday_current_year.strftime('%A') #надаємо змінній строкове значення назви дня тижня для подальшої перевірки.
                if week_day == work_days[0]: #якщо день тижня (Monday) дорівнює дню тижня зі словника
                    birthday_list_Monday.append(name) #додаємо у список днів народження що припадають на понеділок імена користувачів
                elif week_day == work_days[1]: #якщо день тижня (Tuesday) дорівнює дню тижня зі словника
                    birthday_list_Tuesday.append(name) #додаємо у список днів народження що припадають на вівторок імена користувачів
                elif week_day == work_days[2]: #якщо день тижня (Wednesday) дорівнює дню тижня зі словника
                    birthday_list_Wednesday.append(name) #додаємо у список днів народження що припадають на середу імена користувачів
                elif week_day == work_days[3]: #якщо день тижня (Thursday) дорівнює дню тижня зі словника
                    birthday_list_Thursday.append(name) #додаємо у список днів народження що припадають на четвер імена користувачів
                elif week_day == work_days[4]: #якщо день тижня (Friday) дорівнює дню тижня зі словника
                    birthday_list_Friday.append(name) #додаємо у список днів народження що припадають на п'ятницю імена користувачів
                elif week_day not in work_days: #якщо день тижня (Saturday or Sunday) відсутній у  словнику
                    birthday_list_Monday.append(name) #додаємо у список днів народження що припадають на вихідні дні  імена користувачів
            if birthday_list_Monday: # якщо список днів народження не пустий (True)
                users_birthday_dict.update({work_days[0]: birthday_list_Monday}) # Додаємо назву тижня як ключ та список імен користувачів, які припадають на цей день
            if birthday_list_Tuesday: # якщо список днів народження не пустий (True)
                users_birthday_dict.update({work_days[1]: birthday_list_Tuesday}) # Додаємо назву тижня як ключ та список імен користувачів, які припадають на цей день
            if birthday_list_Wednesday: # якщо список днів народження не пустий (True)
                users_birthday_dict.update({work_days[2]: birthday_list_Wednesday}) # Додаємо назву тижня як ключ та список імен користувачів, які припадають на цей день
            if birthday_list_Thursday: # якщо список днів народження не пустий (True)
                users_birthday_dict.update({work_days[3]: birthday_list_Thursday}) # Додаємо назву тижня як ключ та список імен користувачів, які припадають на цей день
            if birthday_list_Friday: # якщо список днів народження не пустий (True)
                users_birthday_dict.update({work_days[4]: birthday_list_Friday}) # Додаємо назву тижня як ключ та список імен користувачів, які припадають на цей день

    return users_birthday_dict # Повертаємо порожній словник, якщо на вході був порожній список, або дні народження у минулому чи більше ніж за тиждень, та наповнений якщо дні народження припали на робочі дні наступного тижня та, якщо на вихідні дні - на понеділок.


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
        {"name": "Bill", "birthday": datetime(1955, 10, 28).date()},
        {"name": "Jan", "birthday": datetime(1981, 10, 28).date()},
        {"name": "Kim", "birthday": datetime(2005, 11, 1).date()},
        {"name": "Maxim", "birthday": datetime(2000, 2, 26).date()},
        {"name": "Anna", "birthday": datetime(2012, 10, 27).date()}
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
        
