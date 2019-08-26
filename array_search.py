from array import *
arr = array('i',[])
print('ente 10 values')
for i in range(10):
    arr.append(int(input()))
print('entered elements:')
for i in arr:
    print(i)
x = int(input('enter element to search'))
for i in range(0,10):
    if arr[i] == x:
        print('found at ',i)
        break
else:
    print('not found')