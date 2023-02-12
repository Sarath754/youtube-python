from array import *

var=array('i',[2,3,4,5,6])

new_var=array(var.typecode,(a*a for a in var))

print(new_var)

print(var.buffer_info())#to get the size

for i in var:
    print(i)