num = int(input('정수를 입력하시오: '))

if num >= 0:
    if num > 0:
        st = '양수'
    else:
        st = '0'
else:
    st = '음수'

print('입력된 정수는 ' + st + '입니다.')
