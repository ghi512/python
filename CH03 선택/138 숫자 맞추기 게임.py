print('숫자 게임에 오신 것을 환영합니다.')
answer = 38
player = int(input('숫자를 맞춰 보세요: '))
if player == answer:
    print('맞추셨습니다!')
elif player > answer:
    print('너무 큼!')
else:
    print('너무 작음!')

print('게임 종료')
