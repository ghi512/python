num = int(input('숫자를 입력하시오: '))

num_list = ['하나', '둘', '셋', '넷', '다섯']

if num <= 5:
    print(num_list[num-1])
else:
    print('많음')
