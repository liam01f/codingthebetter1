y=int(input("choose a number"))
def factorial(x):
    if x==0:
        return(1)
    return(x*factorial(x-1))
print(factorial(y))