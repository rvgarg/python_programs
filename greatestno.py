x = int(input())
y = int(input())
z = int(input())
if x>y:
    if x>z:
        print(x,' is greatest')
    else:
        print(z,' is greatest')
else:
    if y>z:
        print(y,' is greatest')
    else:
        print(z,' is greatest')