import random

ran = random.randrange(1,4)
if ran == 1:
    com = '가위'
elif ran == 2:
    com = '바위'
else:
    com = '보'

user = input('(가위, 바위, 보) 중에서 하나를 선택하세요: ')
print('사용자 :', user, '컴퓨터 :', com)


if user == com:
    print('비겼음!')
elif user == '가위':
    if com == '바위':
        print('컴퓨터가 이겼음!')
    else:
        print('사용자가 이겼음!')
elif user == '바위':
    if com == '보':
        print('컴퓨터가 이겼음!')
    else:
        print('사용자가 이겼음!')
else:
    if com == '가위':
        print('컴퓨터가 이겼음!')
    else:
        print('사용자가 이겼음!')
