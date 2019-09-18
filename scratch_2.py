a = 10


def glob():
    a = 15
    print('local variable', a)
    print('global variable', globals()['a'])


glob()
print('global variable', a)
