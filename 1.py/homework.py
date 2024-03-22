from datetime import datetime

def get_days_from_today(date_string=None):
    if date_string is None:
        date_string = input('Введіть дату в форматі: "YYYY-MM-DD" >>> ')
    try:
        end_date = datetime.fromisoformat(date_string)
    except ValueError:
        print("Некоректна дата. Перевірте введені значення.")
        return
    
    current_date = datetime.today()
    delta_days = end_date - current_date
    if delta_days.days >= 0:
        print(f'{delta_days.days} днів до {end_date.strftime("%Y-%m-%d")}')
    else:
        delta_days = end_date - current_date
        print(f"{delta_days.days} днів пройшло з {end_date.strftime('%Y-%m-%d')}")
    
if __name__ == '__main__':
    get_days_from_today()