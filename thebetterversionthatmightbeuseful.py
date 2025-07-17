import random
class card:
    def __init__(self,suit,value):
        self.suit=suit
        self.value=value
    def __str__(self):
        return(self.suit+" of "+str(self.value))
# a=card("dogs",10)
# print(a)
class deck:
    def __init__(self):
        self.list=[]
    def createdeck(self):
        for i in range(2,15):
            a=card("dog",i)
            self.list.append(a)
        for j in range(2,15):
            b=card("mountian chicken",j)
            self.list.append(b)
        for k in range(2,15):
            c=card("pleasing fungus beetle",k)
            self.list.append(c)
        for l in range(2,15):
            d=card("chicken turtle",l)
            self.list.append(d)
        for m in range(2,15):
            e=card("Spiny Lumpsucker",m)
            self.list.append(e)
        for n in range(2,15):
            f=card("Atlantic guitarfish",n)
            self.list.append(f)
    def printdeck(self):
        for g in range(0,78):
          print(self.list[g])
    def drawcard(self):
        return(self.list.pop())
    def shuffle(self):
        for o in range(0,10000000):
            p=random.randint(0,77)
            q=random.randint(0,77)
            r=self.list[p]
            self.list[p]=self.list[q]
            #self.list[q]=self.list[p]
            self.list[q]=r
    def addcard(self,card1):
        self.list.append(card1)
    def length(self):
        return len(self.list)
h=deck()
h.createdeck()
h.shuffle()
h.printdeck()