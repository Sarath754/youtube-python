#video-5
temp=[1,2,3,4,5]

print(temp[1])

#------------------------------

temp=[25,26,27,28,29]

temp.append(30)

# temp.clear()

temp.insert(2,26.5)

#pop---removing the last value without index

temp.pop(4)

#delete 

del temp[2:]

#extends--to add 2 more values

temp.extend([1,2,3,4])
print(temp)


#inbulid function

temp1=[1,2,13,4,5]

print(min(temp1))

print(max(temp1))

print(sum(temp1))

print(sorted(temp1))