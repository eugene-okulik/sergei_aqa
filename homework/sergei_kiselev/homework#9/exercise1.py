import datetime

such_a_date = 'Jan 15, 2023 - 12:05:33'

new_date = datetime.datetime.strptime(such_a_date, '%b %d, %Y - %H:%M:%S')
new_date_month = new_date.strftime('%B')
new_date_python = new_date.strftime('%B')
new_new_date = new_date.strftime('%d.%m.%Y, %H:%M')
print(new_date_month)
print(new_date)
print(new_new_date)

