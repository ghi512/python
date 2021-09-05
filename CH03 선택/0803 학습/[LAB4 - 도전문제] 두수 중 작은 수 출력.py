#어서와 파이썬은 처음이지! p.107 - 도전 문제

#사용자로부터 두 개의 정수를 입력받아서
#둘 중에서 작은 수를 출력하는 프로그램

num1 = int(input('첫 번째 정수: '))
num2 = int(input('두 번째 정수: '))
min= 0

if num1 < num2:
    min = num1
else:
    min = num2

print('작은 수는 {}입니다.'.format(min))
