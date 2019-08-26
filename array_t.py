from array import *
ar = array('I',[1,2,3,4])
print(ar)
print(ar.buffer_info())
for i in ar:
    print(i)
na = array(ar.typecode,[i*4 for i in ar])
for i in na:
    print(i)