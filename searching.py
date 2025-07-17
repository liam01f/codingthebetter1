# y=int(input("choose a number from 1 through 10: "))
# list=[10,6,2,7,1,5,3,9,8,4]
# def searching(x):
#     return(x)
# for i in range(0,11):
#     if list[i]==y:
#         print(i)
#         break

list=[1,2,3,4,5,6,7,8,9,10,1000000]
def binarysearch(list,start,end,target):
    x=round((start+end)/2)
    if list[x]==target:
        return(x)
    if list[x]>=target:
        end=x
        return(binarysearch(list,start,end,target))
    if list[x]<=target:
        start=x
        return(binarysearch(list,start,end,target))
print(binarysearch(list,0,10,1000000))