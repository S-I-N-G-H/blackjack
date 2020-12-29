'''
AMARDEEP SINGH
BLACKJACK GAME
'''

'''
#-------------------------------------------------------------------------------
Amardeep Singh
****USES CUSTOM BUTTON CLASS****
#-------------------------------------------------------------------------------
'''

import random
import time
from graphics import*
from button import*
import winsound


class Card:

    def __init__(self, rank, suit):

        self.ranks={1:"Ace", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine", 10:"Ten", 11:"Jack", 12:"Queen", 13:"King"}
        self.rvalue = rank

        self.suits={'c':"Clubs", 'd':"Diamonds", 'h':"Hearts", 's':"Spades"}
        self.svalue = suit

    def getRank(self):

        return self.ranks[self.rvalue]

    def getSuit(self):

        return self.suits[self.svalue]

    def bjValue(self):

        if 13 >= self.rvalue > 10:
            return 10

        if 1 == self.rvalue:
            return 11

        else:
            return self.rvalue

    def __str__(self):

        name=(self.getRank())+"_of_"+(self.getSuit()+".gif")
        return name





def pickCard(bList):

    hit=Card(random.randint(1,13), ((['c','d','h','s'])[(random.randrange(len(['c','d','h','s'])))]))
    hit1=str(hit)

    if (bList.count(hit1)) <= 8:
        bList.append(hit1)
    else:
        pickCard(bList)

    return(hit)




def checkAcePlayer(playerlist,bjValue):
    if playerlist.count("Ace_of_Clubs")>0:
        playerlist.remove("Ace_of_Clubs")
        bjValue=bjValue-10

    if playerlist.count("Ace_of_Diamonds")>0:
        playerlist.remove("Ace_of_Diamonds")
        bjValue=bjValue-10

    if playerlist.count("Ace_of_Hearts")>0:
        playerlist.remove("Ace_of_Hearts")
        bjValue=bjValue-10

    if playerlist.count("Ace_of_Spades")>0:
        playerlist.remove("Ace_of_Spades")
        bjValue=bjValue-10

    return bjValue

def checkAceDealer(dealerlist,dealerbjValue):
    if dealerlist.count("Ace_of_Clubs")>0:
        dealerlist.remove("Ace_of_Clubs")
        dealerbjValue=dealerbjValue-10


    if dealerlist.count("Ace_of_Diamonds")>0:
        dealerlist.remove("Ace_of_Diamonds")
        dealerbjValue=dealerbjValue-10


    if dealerlist.count("Ace_of_Hearts")>0:
        dealerlist.remove("Ace_of_Hearts")
        dealerbjValue=dealerbjValue-10


    if dealerlist.count("Ace_of_Spades")>0:
        dealerlist.remove("Ace_of_Spades")
        dealerbjValue=dealerbjValue-10

    return dealerbjValue

def gameEnding(dealerbjValue,bjValue,bet,win,bettxt):


    endtxt=Text(Point(85,10),("")).draw(win)

    cover=Rectangle(Point(0,-20),Point(70,20))
    cover.setFill('light green')
    cover.draw(win)


    if dealerbjValue == bjValue:
        endtxt.setText("PUSH")



    elif (dealerbjValue >= bjValue and dealerbjValue<=21) or dealerbjValue==21 or bjValue>21:

        if dealerbjValue==21:
            endtxt.setText("YOU LOSE\nDEALER BLACKJACK")
        elif bjValue>21:
            endtxt.setText("YOU LOSE\nBUST")
        else:
            endtxt.setText("YOU LOSE")


        txt=Text(Point(35,0),"YOU LOSE")
        txt.setSize(30)
        txt.draw(win)

        bet=0
        bettxt.setText("BET: $"+str(bet))

    else:
        if bjValue==21:
            endtxt.setText("YOU WIN\nBLACKJACK!")
            bet=bet+bet*(3/2)
        elif dealerbjValue>21:
            endtxt.setText("YOU WIN\nDEALER BUST")
            bet=bet*2
        else:
            endtxt.setText("YOU WIN")
            bet=bet*2
        bettxt.setText("BET: $"+str(bet))
        txt=Text(Point(35,0),"YOU WIN")
        txt.setSize(30)
        txt.draw(win)

    return bet






def playTurn(bList,bet,redcard):

    win=GraphWin("BLACKJACK",1200,600)
    win.setCoords(0,-100, 100, 100)
    win.setBackground('light green')
    (Image(Point(50,0),("BACKGROUND2.gif"))).draw(win)
    backgrnd=Rectangle(Point(70,-100),Point(100,100))
    backgrnd.setFill('white')
    backgrnd.draw(win)

    bettxt=Text(Point(85,-10),("BET: $"+str(bet))).draw(win)

    playerlist=[]
    dealerlist=[]


    bjValue,dealerbjValue=0,0
    playervtxt=Text(Point(85,-50),("PLAYER HAND VALUE: "+str(bjValue))).draw(win)
    dealervtxt=Text(Point(85,50),("PLAYER HAND VALUE: "+str(dealerbjValue))).draw(win)

    hit = pickCard(bList)
    bjValue=hit.bjValue()
    (Image(Point(10,-50),(str(hit)))).draw(win)
    playerlist.append(str(hit))
    playervtxt.setText(("PLAYER HAND VALUE: "+str(bjValue)))

    time.sleep(.5)
    hitd = pickCard(bList)
    dealerbjValue=hitd.bjValue()
    (Image(Point(10,50),(str(hitd)))).draw(win)
    dealerlist.append(str(hitd))
    dealervtxt.setText(("DEALER HAND VALUE: "+str(dealerbjValue)))

    hit = pickCard(bList)
    bjValue=bjValue+hit.bjValue()
    (Image(Point(20,-50),(str(hit)))).draw(win)
    playerlist.append(str(hit))
    playervtxt.setText(("PLAYER HAND VALUE: "+str(bjValue)))

    time.sleep(.5)
    hitd = pickCard(bList)
    dealerbjValue= dealerbjValue +hitd.bjValue()
    (Image(Point(20,50),("BACK.gif"))).draw(win)
    dealerlist.append(str(hitd))

    if bjValue>21:
        bjValue=checkAcePlayer(playerlist,bjValue)
    if dealerbjValue>21:
        dealerbjValue=checkAceDealer(dealerlist,dealerbjValue)


    hitbutton = Button(win, Point(20,0), 10, 20, "HIT")
    hitbutton.activate()
    holdbutton = Button(win, Point(50,0), 10, 20, "STAND")
    holdbutton.activate()


    playerspot=20
    dealerspot=20



    play=True

    while play == True:
        if bjValue==21:
            play=False
        else:
            n=True
            while n==True:
                click = win.getMouse()

                if holdbutton.clicked(click):
                    play=False
                    n=False

                if hitbutton.clicked(click):

                    hit = pickCard(bList)
                    playerspot=playerspot+10
                    (Image(Point(playerspot,-50),(str(hit)))).draw(win)
                    playerlist.append(str(hit))
                    value=hit.bjValue()
                    bjValue=bjValue+value
                    n=False

            if bjValue>21:
                bjValue=checkAcePlayer(playerlist,bjValue)

                if bjValue>21:
                    play=False
            if bjValue==21:
                play=False
            playervtxt.setText(("PLAYER HAND VALUE: "+str(bjValue)))


    (Image(Point(20,50),(str(hitd)))).draw(win)

    if bjValue<21:

        while dealerbjValue<17:
            time.sleep(1)
            dealerspot=dealerspot+10
            hitd = pickCard(bList)
            (Image(Point(dealerspot,50),((str(hitd))))).draw(win)
            valueD=hitd.bjValue()
            dealerbjValue=dealerbjValue+valueD


            if dealerbjValue>21:
                dealerbjValue=checkAceDealer(dealerlist,dealerbjValue)
            dealervtxt.setText(("DEALER HAND VALUE: "+str(dealerbjValue)))

    dealervtxt.setText(("DEALER HAND VALUE: "+str(dealerbjValue)))


    bet=gameEnding(dealerbjValue,bjValue,bet,win,bettxt)

    quitbutton = Button(win, Point(95,-95), 10, 10, "QUIT")
    quitbutton.activate()
    pabutton = Button(win, Point(75,-95), 10, 10, "PLAY AGAIN")
    pabutton.activate()

    n=True
    while n==True:
        click = win.getMouse()
        if quitbutton.clicked(click):
            winsound.PlaySound(None, winsound.SND_ASYNC)
            win.close()
            quit()
        if pabutton.clicked(click):
            win.close()
            n=False

    if redcard<len(bList):
        bList=[]

    playTurn(bList,bet,redcard)




def playGame(bList):

    redcard=167+ random.randrange(0,81)

    win=GraphWin("BLACKJACK",600,600)
    win.setCoords(-100, -100, 100, 100)
    win.setBackground('light green')
    (Image(Point(0,0),("BACKGROUND1.gif"))).draw(win)

    txt=Text(Point(0,30),"BLACKJACK\nby Amardeep Singh")
    txt.setSize(30)
    txt.draw(win)
    startButton = Button(win, Point(0,0), 40, 10, "START GAME")
    startButton.activate()
    start=False
    while start==False:
        click = win.getMouse()
        if startButton.clicked(click):
            txt.undraw()
            startButton.deactivate()
            startButton.undraw()

            start=True


    bet=0
    txt=Text(Point(0,10),("BET: $"+str(bet)))
    txt.draw(win)
    startButton = Button(win, Point(0,-10), 40, 10, "CONTINUE")
    startButton.activate()
    up5 = Button(win, Point(40,0), 30, 10, "+ $5")
    up5.activate()
    down5 = Button(win, Point(-40,0), 30, 10, "- $5")
    down5.activate()
    continu=False
    while continu==False:


        if bet==0:
            down5.deactivate()
        elif bet==200:
            up5.deactivate()
        elif bet>0:
            down5.activate()
        if bet<200:
            up5.activate()


        click = win.getMouse()
        if startButton.clicked(click):
            up5.undraw()
            down5.undraw()
            txt.undraw()
            startButton.undraw()
            continu=True
        if up5.clicked(click):
            bet=bet+5
            txt.setText(("BET: $"+str(bet)))
        if down5.clicked(click):
            bet=bet-5
            txt.setText(("BET: $"+str(bet)))

    win.close()

    playTurn(bList,bet,redcard)









def main():

    winsound.PlaySound("BACKMUSIC.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
    winsound.SND_LOOP

    bList=[]

    playGame(bList)



main()









