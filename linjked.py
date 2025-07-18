class node:
    def __init__(self,value):
        self.value=value
        self.next=None
    def setnext(self,twonode):
        self.next=twonode
    def getlink(self):
        return(self.next)
    def __str__(self):
        return(str(self.value))
n=node(0)
print(n)
class linkedlist:
    def __init__(self):
        self.head=None
        self.size=0
    def add(self):
        if self.size==0:
            