from datetime import date

current_date = date.today()
print('Today:', current_date)
try:
    input_date = input('Other date: ' )
    difference_date = date.fromisoformat(input_date)
    dif = difference_date - current_date
    print(f'Difference: {dif.days} days')
except ValueError:
    print(f'{input_date} is not correct date, try again! Format:(YYYY-MM-DD)')