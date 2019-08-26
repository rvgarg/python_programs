import math as m
x = int(input())
prime = True
if x>0:
    for i in range(2,int(m.sqrt(x))+1):
        if x%i == 0:
            prime = False
            break
if x < 2:
    print('not defined')
elif prime:
    print('number is prime')
else:
    print('not prime')