workHour = float(input('주 근무시간을 입력하시오: '))
hourPay = int(input('시간당 임금을 입력하시오: '))

if workHour > 40:
    overtime = workHour - 40
    monthPay = (40 * hourPay) + (overtime * hourPay * 1.5)
else:
    monthPay = workHour * hourPay

print('총임금은', monthPay)
