from array import *

arr=array('i',[])

var=int(input("Enter your range"))

for i in range(var):
    x=int(input("Enter your number"))
    arr.append(x)

print(arr)