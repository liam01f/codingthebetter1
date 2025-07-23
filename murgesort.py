import random
list=[]
for k in range(0,10000):
    my_ran_value = random.randint(1,10000)
    list.append(my_ran_value)
def mergesourt(list):
    if len(list)<2:
        return list
    a = list[0:len(list)//2]
    b = list[len(list)//2:len(list)]
    c=mergesourt(a)
    d=mergesourt(b)
    return merge(c,d)
def merge(list, alsolist):
    outputlist=[]
    if len(list)==0:
        return alsolist
    if len(alsolist)==0:
        return list
    for i in range(0,len(alsolist)+len(list)):
        if list[0]>=alsolist[0]:
            outputlist.append(alsolist[0])
            alsolist.pop(0)
        elif list[0]<=alsolist[0]:
            outputlist.append(list[0])
            list.pop(0)
        if len(list)==0:
            outputlist+=alsolist
            return outputlist
        if len(alsolist)==0:
            outputlist+=list
            return outputlist
    return outputlist
# print(merge(a, b))
print(mergesourt(list))