import random
list=[]
def merge(list):
    newlist=[]

for k in range(0,10000000):
    my_ran_value = random.randint(1,100000000)
    list.append(my_ran_value)
# def quicksourt(list):
#     L=0
#     R=len(list)-1
#     lists=[]
#     a=list[0]
#     for j in range(0,len(list)):
#         if len(list)==0:
#             break
#         if list[j]<=a:
#             lists.append[j]
#             list.pop(j)
#         if list[j]>a:
#             list[j]=a
# quicksourt(list)
# #print(lists)

def partition(list):
    if len(list) == 1 or len(list) == 0:
        return list
    pivot = list[0]
    greater = []
    less = []
    equalto = []
    for i in range(0,len(list)):
        if len(list)==0:
            break
        if list[i]<pivot:
            less.append(list[i])
        elif list[i]>pivot:
            greater.append(list[i])
        elif list[i]==pivot:
            equalto.append(list[i])
    return partition(less) + equalto + partition(greater)

def overagain(list):
    for i in range(0,len(list)-1):
        list = partition(list)
        list = [0,len(list)//2]
    for i in range(0,len(list)-1):
        list = partition(list)
        list = [len(list)//2,len(list)]
    return list

print(partition(list))