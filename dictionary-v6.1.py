#key value pair

temp={1:"sarath",2:"Dhoni",4:"Stokes"}

print(temp[4])

print(temp.get(2))

print(temp.get(1,'Not found'))

print(temp.get(3,'Not found'))

key=["sarath","bibin","rahul"]

pair=["React","python","java"]

data=dict(zip(key,pair))

data["kiran"]="JS"

del data["kiran"]


print(data)


prgm={"Cricket":"ICC","football":"FIFA","Python":["Pandas","pychamp"],"Java":{"js":"jelo","ps":"helo"}}


print(prgm["Cricket"])

print(prgm["Python"][1])

print(prgm["Java"]["js"])