List = []
for i in range(10):
    List.append(input('name'))
fil = list(filter(lambda s:len(s)>3,List))
print(len(fil))
print(fil)
