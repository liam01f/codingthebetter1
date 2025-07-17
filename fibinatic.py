y=int(input("choose a number"))
def fib(x):
    if x==0 or x==1:
        return(1)
    return(fib(x-2)+fib(x-1))
print(fib(y))