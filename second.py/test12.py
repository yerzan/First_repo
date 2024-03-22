from datetime import datetime

def get_days_from_today(date_stringe = None):
    if date_stringe is None:
        date_stringe = input('Eneter a date in format: "YYYY-MM-DD" >>> ')
    try:
        end_date = datetime.fromisoformat(date_stringe)
    except ValueError:
        print(f"{date_stringe} is not correct. Please try again!")
        return
    
    current_date = datetime.today()
    delta_days = end_date - current_date
    if delta_days.days >= 0:
        print(f"{delta_days.days} days to {end_date.strftime("%Y-%m-%d")}")
    else:
        delta_days = end_date - current_date
        print(f"{delta_days.days} days left from {end_date.strftime('%Y-%m-%d')}")


if __name__ == '__main__':
    get_days_from_today()