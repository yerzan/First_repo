from datetime import datetime, timedelta
import random

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday_date = datetime.strptime(user['birthday'], "%Y.%m.%d").date()

        if birthday_date < today:
            birthday_date = birthday_date.replace(year=today.year + 1)

        days_until_birthday = (birthday_date - today).days

        if 0 <= days_until_birthday <= 7:

            if birthday_date.weekday() in (5, 6):
                days_until_birthday += (7 - birthday_date.weekday())

            upcoming_birthdays.append({
                 "name": user["name"],
                "birthday_date": (today + timedelta(days=days_until_birthday)).strftime("%Y.%m.%d")
            })

    return upcoming_birthdays

users = [
    {"name": "Andrii Duda", "birthday": "2024.03.27"},
    {"name": "Joe Biden", "birthday": "2024.03.25"}
]

get_upcoming_birthdays = get_upcoming_birthdays(users)
print('Список привітань на цьому тижні:', get_upcoming_birthdays)