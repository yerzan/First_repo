from datetime import datetime

def get_days():
    user_input = input("Введіть дату в форматі mm.dd: ")
    user_date = datetime.strptime(user_input, '%d %m')
    current_date = datetime.now()
    user_date = user_date.replace(year=current_date.year)
    delta_days = user_date - current_date
    terget_date = datetime.strftime(user_date, '%d-%B-%Y')
    if delta_days.days > 0:
        print(f"{delta_days.days} days left before {terget_date}")
    else:
        user_date = user_date.replace(year=user_date.year + 1)
        delta_days = user_date - current_date
        print(f"{delta_days.days} days left before {terget_date}")




if __name__ == '__main__':
    get_days()