from datetime import date

def get_days_from_today(date_string=None):
    if date_string is None:
        date_string = input('Введіть дату в форматі: "YYYY MM DD" >>>  ')
    end_date_parts = date_string.split()
    if len(end_date_parts) != 3:
        print("Некоректний формат дати. Будь ласка, введіть дату у форматі 'YYYY MM DD'.")
        return
    year, month, day = map(int, end_date_parts)
    try:
        end_date = date(year, month, day)
    except ValueError:
        print("Некоректна дата. Перевірте введені значення.")
        return
    
    current_date = date.today()
    delta_days = end_date - current_date
    tg = date.strftime(end_date, '%d %m %Y')
    if delta_days.days >= 0:
        print(f'{delta_days.days} днів до {tg}')
    else:
        end_date = end_date.replace(year=end_date.year + 1)
        delta_days = end_date - current_date
        print(f"{delta_days.days} днів пройшло з {tg}")
    

if __name__ == '__main__':
    get_days_from_today()
