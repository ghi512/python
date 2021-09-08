x1 = int(input('첫 번째 점의 x좌표 : '))
y1 = int(input('첫 번째 점의 y좌표 : '))
x2 = int(input('두 번째 점의 x좌표 : '))
y2 = int(input('두 번째 점의 y좌표 : '))

if x1 == x2:
    print('직선의 방정식은 x =', x1)
else:
    m = (y2 - y1) / (x2 - x1) #기울기
    q = y1 - m * x1
    print('직선의 방정식은 y =', m, 'x +(', q, ')')
    


