x = int(input('max limit'))
if x < 0:
    print('invalid input')
elif x == 0:
    print('0')
else:
    a = 0
    b = 1
    print(a)
    while b <= x:
        print(b)
        c = a + b
        a, b = b, c
