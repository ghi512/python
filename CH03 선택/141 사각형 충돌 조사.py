p1x = int(input('첫번째 사각형의 p1.x = '))
p1y = int(input('첫번째 사각형의 p1.y = '))
p2x = int(input('첫번째 사각형의 p2.x = '))
p2y = int(input('첫번째 사각형의 p2.y = '))

p3x = int(input('두번째 사각형의 p3.x = '))
p3y = int(input('두번째 사각형의 p3.y = '))
p4x = int(input('두번째 사각형의 p4.x = '))
p4y = int(input('두번째 사각형의 p4.y = '))

overlapped = not (p4y > p1y or
                  p2y > p3y or
                  p4x < p1x or
                  p2x < p3x)

if overlapped == True:
    print('두 개의 사각형이 겹침!')
else:
    print('두 개의 사각형이 겹치지 않음!')
