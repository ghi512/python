#어서와 파이썬은 처음이지! p.105

#사용자로부터 현재 온도를 입력받는다.
#온도가 30도 이하이면 긴바지 착용을 추천한다
#온도가 30도를 초과하면 반바지 착용을 추천한다
#복장에 대한 추천이 끝나면 '이제 나가서 운동하세요!'를 출력한다.

temp = float(input('현재 온도: '))

if temp <= 30:
    print('긴바지 착용을 추천합니다.')
else:
    print('반바지 착용을 추천합니다.')
print('이제 나가서 운동하세요!')
