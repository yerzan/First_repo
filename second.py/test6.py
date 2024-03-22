from datetime import datetime, timedelta
import random

def get_random_birthday(n):
    current_date = datetime.now()
    oldest_date = current_date - timedelta(days=365*80)
    birthday_list = []
    for i in range(n):
        fake_year = random.randrange(oldest_date.year, current_date.year)
        fake_month = random.randint(1,12)
        fake_day = random.randint(1,31)
        try:
            fake_birthday = datetime(year=fake_year,month=fake_month,day=fake_day)
        except ValueError:
            continue
        if current_date >= fake_birthday:
            birthday_list.append(fake_birthday.date())
    return birthday_list
        





if __name__ == '__main__':
    birthday_list = get_random_birthday(10)
    print(random.sample(birthday_list, k=4))