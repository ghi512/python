#어서와 파이썬은 처음이지! p.107

#사용자로부터 두 개의 정수를 입력받아서
#둘 중에서 큰 수를 출력하는 프로그램

num1 = int(input('첫 번째 정수: '))
num2 = int(input('두 번째 정수: '))
max = 0

if num1 > num2:
    max = num1
else:
    max = num2

print('큰 수는 {}입니다.'.format(max))
