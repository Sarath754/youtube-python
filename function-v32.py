def helo():
    print("Good Morning")
helo()



def add(a,b):
    x=a+b
    print(x)

add(2,3)



def add_sub(x,y):
    a=x+y
    b=x-y
    return a,b

result1,result2=add_sub(5,5)

print(result1,result2)