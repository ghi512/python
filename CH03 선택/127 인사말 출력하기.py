import time
now = time.localtime()
print('현재 시간은', time.asctime())

hour = now.tm_hour
if hour < 11:
    print('Good morning')
elif hour <15:
    print('Good afternoon')
elif hour < 20:
    print('Good evening')
else:
    print('Good night')
