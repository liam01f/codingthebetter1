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
            if 10<i and i<14:
                i=10
            if i==14:
                i=11
            a=card("dog",i)
            self.list.append(a)
        for j in range(2,15):
            if 10<j and j<14:
                j=10
            if j==14:
                j=11
            b=card("mountian chicken",j)
            self.list.append(b)
        for k in range(2,15):
            if 10<k and k<14:
                k=10
            if k==14:
                k=11
            c=card("pleasing fungus beetle",k)
            self.list.append(c)
        for l in range(2,15):
            if 10<l and l<14:
                l=10
            if l==14:
                l=11
            d=card("chicken turtle",l)
            self.list.append(d)
        for m in range(2,15):
            if 10<m and m<14:
                m=10
            if m==14:
                m=11
            e=card("Spiny Lumpsucker",m)
            self.list.append(e)
        for n in range(2,15):
            if 10<n and n<14:
                n=10
            if n==14:
                n=11
            f=card("Atlantic guitarfish",n)
            self.list.append(f)
    def printdeck(self):
        for g in range(0,78):
          print(self.list[g])
    def drawcard(self):
        return(self.list.pop())
    def shuffle(self):
        for o in range(0,10000000):
            p=random.randint(0,self.length())
            q=random.randint(0,self.length())
            r=self.list[p-1]
            self.list[p-1]=self.list[q-1]
            #self.list[q]=self.list[p]
            self.list[q-1]=r
    def addcard(self,card1):
        self.list.append(card1)
    def length(self):
        return len(self.list)
def totalvalue(playerdeck):
    totalvalue=0
    for q in range(0,playerdeck.length()):
        totalvalue+=playerdeck.list[q].value
    return(totalvalue)

h=deck()
h.createdeck()
h.shuffle()

j=card("dog",10)
k=card("dog",9)
l=card("dog",2)

computerdeck=deck()
computerdeck.addcard(j)
computerdeck.addcard(k)
computerdeck.addcard(l)

z=500
print("you have 500 dollars and you are being forced to go all in every round")
playerhand=deck()
while True:
    h.shuffle()
    o=h.drawcard()
    p=h.drawcard()
    playerhand.addcard(o)
    playerhand.addcard(p)
    print(o)
    print(p)
    if o.value+p.value==21:
        print("tie")
    n=input("do you want to hit")
    while n=="yes":
        help=h.drawcard()
        playerhand.addcard(help)
        print(help)
        print("your total hand is "+str(totalvalue(playerhand)))
        if totalvalue(playerhand)>21:
            print("you lose")
            break
        n=input("do you want to hit")
    if totalvalue(playerhand)>21:
        print("you lose")
        break
    if n=="no":
        #computerdeck.printdeck()
        if totalvalue(computerdeck)>totalvalue(playerhand) and totalvalue(computerdeck)<=21:
            print("you lose")
            print("ha ha I get to keep all of your money")
            z=0
            print(z)
            break
        if totalvalue(computerdeck)<totalvalue(playerhand):
            print("you win")
            print("your money will be doubled")
            z*=2
            print(z)
            break
            #restart game with 1000 dollars
        if totalvalue(computerdeck)==totalvalue(playerhand):
            print("tie")
            print("you get to keep the money")
            print(z)
            break