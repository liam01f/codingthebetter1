list=[2305782904367341538543267093264322376601,541708901727029876546556747384,504,83749032,954456,8126543,2365,549026781,18245680912,136450234,325970265878740936,10,7,1,6,2,67,22,21,3,4]
import random
list=[]
for k in range(0,10000):
    my_ran_value = random.randint(1,10000)
    list.append(my_ran_value)
y=0
v=len(list)
def shortestnumber(list,y,v):
    y=0
    for j in range(v):
        for i in range(len(list)-1):
            if list[i]>list[y]:
                z=list[i]
                x=list[y]
                list[i]=x
                list[y]=z
        y=y+1
    return(list)
# list=shortestnumber(list,y)
# print(list)
# print(shortestnumber(list,y))
# print(shortestnumber(len(list)))
list=shortestnumber(list,y,v)

print(list)