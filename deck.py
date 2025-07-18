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
            b=card("mountain chicken",j)
            self.list.append(b)
        for k in range(2,15):
            c=card("pleasing fungus beetle",k)
            self.list.append(c)
        for l in range(2,15):
            d=card("chicken turtle",l)
            self.list.append(d)
        for m in range(2,15):
            e=card("spiny lumpsucker",m)
            self.list.append(e)
        for n in range(2,15):
            f=card("atlantic guitarfish",n)
            self.list.append(f)
    def printdeck(self):
        for g in range(0,39):
            print(self.list[g])
    def drawcard(self):
        return(self.list.pop())
    def shuffle(self):
        for o in range(0,10000000):
            p=random.randint(0,len(self.list)-1)
            q=random.randint(0,len(self.list)-1)
            r=self.list[p]
            self.list[p]=self.list[q]
            #self.list[q]=self.list[p]
            self.list[q]=r
    def addcard(self,card1):
        self.list.append(card1)
    def length(self):
        return len(self.list)
#h=deck()
#h.createdeck()
#h.shuffle()
#h.printdeck()

playerdeck=deck()
computerdeck=deck()

suits=["dog","mountain chicken","spiny lumpsucker","atlantic gatarfish","chicken turtle","pleasing fungus beetle"]
for s in range(0,6):
    t=card(suits[s],2)
    u=card(suits[s],3)
    v=card(suits[s],4)
    w=card(suits[s],5)
    x=card(suits[s],6)
    y=card(suits[s],7)
    playerdeck.addcard(t)
    playerdeck.addcard(u)
    playerdeck.addcard(v)
    playerdeck.addcard(w)
    playerdeck.addcard(x)
    playerdeck.addcard(y)

for z in range(0,3):
    aa=card(suits[z],8)
    playerdeck.addcard(aa)
playerdeck.shuffle()

for bb in range(0,6):
    cc=card(suits[bb],9)
    dd=card(suits[bb],10)
    ee=card(suits[bb],11)
    ff=card(suits[bb],12)
    gg=card(suits[bb],13)
    hh=card(suits[bb],14)
    computerdeck.addcard(cc)
    computerdeck.addcard(dd)
    computerdeck.addcard(ee)
    computerdeck.addcard(ff)
    computerdeck.addcard(gg)
    computerdeck.addcard(hh)
for ii in range(3,6):
    jj=card(suits[ii],8)
    computerdeck.addcard(jj)
computerdeck.shuffle()
# playerdeck.shuffle()
# computerdeck.printdeck()
# print()
# playerdeck.printdeck()

while True:
    computerdeck.length()
    print(computerdeck.length())
    playerdeck.length()

    print(playerdeck.length())
    topcard=computerdeck.drawcard()
    lossingtopcard=playerdeck.drawcard()
    if topcard.value>lossingtopcard.value:
        computerdeck.addcard(lossingtopcard)
        computerdeck.addcard(topcard)
    elif topcard.value<lossingtopcard.value:
        playerdeck.addcard(lossingtopcard)
        playerdeck.addcard(topcard)
    elif topcard.value==lossingtopcard.value:
        while True:
            if playerdeck.length()==0:
                print("game over")
                print()
                print("you lose hahahahahahahahahaha")
                print()
                print("please play again")
                break
            if computerdeck.length()==0:
                print("gameover")
                print()
                print("how it was riged in my favor")
                print()
                print("please play again")
                break
            print("war")
            middledeck=deck()
            for kk in range(0,3):
                nn=computerdeck.drawcard()
                oo=playerdeck.drawcard()
                middledeck.addcard(nn)
                middledeck.addcard(oo)
            ll=computerdeck.drawcard()
            mm=playerdeck.drawcard()
            if ll.value<mm.value:
                for oo in range(0,8):
                    alsotopcard=middledeck.drawcard()
                    playerdeck.addcard(alsotopcard)
                playerdeck.addcard(ll)
                playerdeck.addcard(mm)
                break
            if ll.value<mm.value:
                for qq in range(0,8):
                    alsolossertopcard=middledeck.drawcard()
                    playerdeck.addcard(alsolossertopcard)
                playerdeck.addcard(ll)
                playerdeck.addcard(mm)
                break
    if playerdeck!=lossingtopcard:
        print("game over")
        print()
        print("you lose hahahahahahahahahaha")
        print()
        print("please play again")
        break
    if computerdeck!=topcard:
        print("gameover")
        print()
        print("how it was riged in my favor")
        print()
        print("please play again")
        break