from datetime import datetime, timedelta


def get_birthdays_per_week(users: list):

    output_birthday = {
        'Monday': [],
        'Tuesday': [],
        'Wednesday': [],
        'Thursday': [],
        'Friday': [],
    }

    for user in users:


        # Формируем дату ДР, которая будет в ближайший год
        try:
            birthday_this_year = user['birthday'].replace(year=datetime.now().year)
            if birthday_this_year.date() < datetime.now().date():
                birthday_this_year = birthday_this_year.replace(year=datetime.now().year+1)
        # обработка 29 февраля через увеличение даты ДР на 1
        except ValueError:
            user['birthday'] += timedelta(days=1)
            birthday_this_year = user['birthday'].replace(year=datetime.now().year)
            if birthday_this_year.date() < datetime.now().date():
                birthday_this_year = birthday_this_year.replace(year=datetime.now().year+1)

        # ДР, которые выпадают на выходные, смещаем на понедельник
        if birthday_this_year.weekday() == 5:
            birthday_this_year += timedelta(days=2)
        elif birthday_this_year.weekday() == 6:
            birthday_this_year += timedelta(days=1)

        # Выбираем ДР которые выпадают на ближайшую неделю
        if (birthday_this_year.date() - datetime.now().date()) < timedelta(days=7):
            output_birthday[birthday_this_year.strftime('%A')].append(user['name'])

    # Output
    for day_week, name in output_birthday.items():
        if len(name) > 0:
            print(day_week+':', ', '.join(name))


# =============== m a i n ===========================================
if __name__ == '__main__':

    users = [
        {'name': 'Pavel', 'birthday': datetime(year=1996, month=7, day=25)},
        {'name': 'Nikolay', 'birthday': datetime(year=1991, month=7, day=26)},
        {'name': 'Natasha', 'birthday': datetime(year=1986, month=7, day=27)},
        {'name': 'Svetlana', 'birthday': datetime(year=1985, month=7, day=28)},
        {'name': 'Masha', 'birthday': datetime(year=1999, month=7, day=29)},
        {'name': 'Vasiliy', 'birthday': datetime(year=2001, month=7, day=30)},
        {'name': 'Stepan', 'birthday': datetime(year=2011, month=7, day=31)},
        {'name': 'Irina', 'birthday': datetime(year=2007, month=8, day=1)},
    ]

    get_birthdays_per_week(users)
