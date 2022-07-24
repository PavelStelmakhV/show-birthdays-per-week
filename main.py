from datetime import datetime, timedelta


def get_birthdays_per_week(users: list):

    output_birthday = {
        'Monday': [],
        'Tuesday': [],
        'Wednesday': [],
        'Thursday': [],
        'Friday': [],
    }

    current_datetime = datetime(year=datetime.now().year, month=datetime.now().month, day=datetime.now().day)

    for user in users:

        # Формируем дату ДР, которое будет в ближайший год
        try:
            birthday_this_year = datetime(year=datetime.now().year, month=user['birthday'].month, day=user['birthday'].day)
            if birthday_this_year < current_datetime:
                birthday_this_year = datetime(year=datetime.now().year+1, month=user['birthday'].month, day=user['birthday'].day)
        # обработка 29 февраля через увеличение даты ДР на 1
        except ValueError:
            user['birthday'] += timedelta(days=1)
            birthday_this_year = datetime(year=datetime.now().year, month=user['birthday'].month, day=user['birthday'].day)
            if birthday_this_year < current_datetime:
                birthday_this_year = datetime(year=datetime.now().year + 1, month=user['birthday'].month, day=user['birthday'].day)

        # ДР, которые выпадают на выходные, смещаем на понедельник
        if birthday_this_year.weekday() == 5:
            birthday_this_year += timedelta(days=2)
        elif birthday_this_year.weekday() == 6:
            birthday_this_year += timedelta(days=1)

        # Выбираем ДР которые выпадают на ближайшую неделю
        if (birthday_this_year - current_datetime) < timedelta(days=7):
            output_birthday[birthday_this_year.strftime('%A')].append(user['name'])

    # Output
    for day_week, name in output_birthday.items():
        if len(name) > 0:
            print(day_week+':', ', '.join(name))


# =============== m a i n ===========================================
if __name__ == '__main__':

    users = [
        {'name': 'Pavel', 'birthday': datetime(year=1996, month=7, day=23)},
        {'name': 'Nikolay', 'birthday': datetime(year=1991, month=7, day=24)},
        {'name': 'Natasha', 'birthday': datetime(year=1986, month=7, day=25)},
        {'name': 'Svetlana', 'birthday': datetime(year=1985, month=7, day=26)},
        {'name': 'Masha', 'birthday': datetime(year=1999, month=7, day=27)},
        {'name': 'Vasiliy', 'birthday': datetime(year=2001, month=7, day=28)},
        {'name': 'Stepan', 'birthday': datetime(year=2011, month=7, day=29)},
        {'name': 'Irina', 'birthday': datetime(year=2007, month=7, day=30)},
    ]

    get_birthdays_per_week(users)
