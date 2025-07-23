class node():
    def __init__(self, data):
        self.data=data
        self.smaller=None
        self.bigger=None
    def setsmaller(self, m):
        self.smaller=m
    def setbigger(self, l):
        self.bigger=l
class tree():
    def __init__(self):
        self.head=None
    def add(self, something):
        if self.head is None:
            self.head=something
        else:
            x=self.head
            while True:
                if something.data > x.data:
                    if x.bigger is None:
                        x.bigger = something
                        return
                    x = x.bigger

                else:
                    if x.smaller is None:
                        x.smaller = something
                        return
                    x = x.smaller
                
t= tree()
to_add = node(1)
t.add(to_add)
print("head", t.head.data)

to_add = node(100000000000)
t.add(to_add)
print("bigger than head", t.head.bigger.data)

to_add = node(500000)
t.add(to_add)
print("smaller than bigger than head", t.head.bigger.smaller.data)

to_add = node(-500000)
t.add(to_add)
print("smaller than head", t.head.smaller.data)
