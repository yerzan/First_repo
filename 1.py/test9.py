from datetime import datetime, timedelta


current_date = datetime.now().strftime('%Y-%m-%d')

end_date_input = input("Введіть дату в форматі 'DD-MM-YYYY' >>> ")

end_date = datetime.strptime(end_date_input, '%d-%m-%Y')

difference = end_date - datetime.strptime(current_date, '%Y-%m-%d')

print('Початкова дата:', current_date)
print('Введена дата:', end_date)

print('Різниця між ними:', difference)
