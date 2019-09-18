def unique_checker(us, n):
    so = sorted(us)
    for i in range(n - 1):
        if so[i] - so[i + 1] == 0:
            print('there are repeated numbers')
            break
    else:
        print('the sequence has unique elements')


n = int(input())
us = []
for i in range(n):
    us.append(int(input()))
unique_checker(us, n)
