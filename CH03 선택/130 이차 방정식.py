import math

A = float(input('A = '))
B = float(input('B = '))
C = float(input('C = '))

D = B ** 2 - (4 * A * C)

if A == 0:
    print('x = ', -C/B)
elif D == 0:
    print('x = ', -B/(2*A))
elif D > 0:
    print('x1 = ', (-B + math.sqrt(D))/(2*A))
    print('x2 = ', (-B - math.sqrt(D))/(2*A))
else:
    print('실근이 존재하지 않')
