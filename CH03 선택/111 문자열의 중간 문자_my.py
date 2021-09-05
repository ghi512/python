str = input('문자열을 입력하시오: ')
len = len(str)

if (len%2 != 0): #문자열의 길이가 홀수 개인 경우
    len = len//2
    center = str[len]
else:
    len = int(len/2)
    center = str[len-1] + str[len]

print('중앙 글자는 ', center)
