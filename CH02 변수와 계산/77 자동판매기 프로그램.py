price = int(input("물건값을 입력하시오: "))
note = int(input("1000원 지폐개수: "))
coin500 = int(input("500원 동전개수: "))
coin100 = int(input("100원 동전개수: "))

userPay = note*1000 + coin500*500 + coin100*100
change = userPay - price

#500원 거스름돈 개수
num500 = change // 500
change = change % 500

#100원 거스름돈 개수
num100 = change // 100
change = change % 100

#10원 거스름돈 개수
num10 = change // 10
change = change % 10

#1원 거스름돈 개수
num1 = change

print('500원 = {}, 100원 = {}, 10원 = {}, 1원 = {}'.format(num500, num100, num10, num1))
