from datetime import datetime, timedelta

current_day = datetime.now()

user_input = input("Enter a date in format \'Day-Month-Year\' (e.g., 16-10-2006) >>> ")
user_date = datetime.strptime(user_input, '%d-%m-%Y')

difference = current_day - user_date

print (f'Різниця між датами {difference} днів')