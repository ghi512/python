choice = int(input('도형을 입력하시오(1:사각형, 2:삼각형, 3:원) : '))

if choice == 1: #사각형
    w = int(input('가로 : '))
    h = int(input('세로 : '))
    area = w * h
elif choice == 2:
    b = int(input('밑변 : '))
    h = int(input('높이 : '))
    area = b * h / 2
elif choice == 3:
    r = int(input('반지름 : '))
    area = 3.141592 * r ** 2

print('면적 = ', area)
