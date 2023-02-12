
# temp =5
# x=int(input("Enter your candy"))

# i=1

# while i<=x:

#     if i> temp:
#         print("Out of stock")
#         break

#     print("Candy")

#     i =i+1

#------------------------------------------------------------Continue--------------------

for i in range(1,100):

    if i % 3==0 or i % 5==0:
        continue

    print(i)

