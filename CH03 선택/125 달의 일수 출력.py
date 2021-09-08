month = int(input('달을 입력하시오: '))

if month == 2:
    days = 29
elif month == 4 or month == 6 or month == 9 or month == 11:
    days = 30
else:
    days = 31

print('월의 날수는', days)
