'''
AMARDEEP SINGH
BLACKJACK GAME
2019
'''
#-------------------------------------------------------------------------------
'''
Imports
Made a custom button class with undraw and setColor feature
'''
import random
import time
from graphics import*
from button import*
import winsound
#-------------------------------------------------------------------------------
'''
Card class
Gives each card a value and suit and name
Name used for gif files
'''
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
#-------------------------------------------------------------------------------
'''
Picks a card randomly
Adds it to the burn list
If the cards already in the burn list (x8) then picks a different card
'''

def pickCard(bList):

    hit=Card(random.randint(1,13), ((['c','d','h','s'])[(random.randrange(len(['c','d','h','s'])))]))
    hit1=str(hit)

    if (bList.count(hit1)) <= 8:
        bList.append(hit1)
    else:
        pickCard(bList)

    return(hit)
#-------------------------------------------------------------------------------
'''
Checks if player has an ace and called if over 21 will subtract 10
'''
def checkAcePlayer(playerlist,bjValue):
    if playerlist.count("Ace_of_Clubs.gif")>0:
        playerlist.remove("Ace_of_Clubs.gif")
        bjValue=bjValue-10
        playerlist.append("Ace spot holder")   # ADDS A FILLER TO KEEP LIST LENGTH

    if playerlist.count("Ace_of_Diamonds.gif")>0:
        playerlist.remove("Ace_of_Diamonds.gif")
        bjValue=bjValue-10
        playerlist.append("Ace spot holder")

    if playerlist.count("Ace_of_Hearts.gif")>0:
        playerlist.remove("Ace_of_Hearts.gif")
        bjValue=bjValue-10
        playerlist.append("Ace spot holder")

    if playerlist.count("Ace_of_Spades.gif")>0:
        playerlist.remove("Ace_of_Spades.gif")
        bjValue=bjValue-10
        playerlist.append("Ace spot holder")

    return bjValue
#-------------------------------------------------------------------------------
'''
Checks if dealer has an ace and called if over 21 will subtract 10
'''
def checkAceDealer(dealerlist,dealerbjValue):
    if dealerlist.count("Ace_of_Clubs.gif")>0:
        dealerlist.remove("Ace_of_Clubs.gif")
        dealerbjValue=dealerbjValue-10
        dealerlist.append("Ace spot holder") # ADDS A FILLER TO KEEP LIST LENGTH


    if dealerlist.count("Ace_of_Diamonds.gif")>0:
        dealerlist.remove("Ace_of_Diamonds.gif")
        dealerbjValue=dealerbjValue-10
        dealerlist.append("Ace spot holder")


    if dealerlist.count("Ace_of_Hearts.gif")>0:
        dealerlist.remove("Ace_of_Hearts.gif")
        dealerbjValue=dealerbjValue-10
        dealerlist.append("Ace spot holder")


    if dealerlist.count("Ace_of_Spades.gif")>0:
        dealerlist.remove("Ace_of_Spades.gif")
        dealerbjValue=dealerbjValue-10
        dealerlist.append("Ace spot holder")

    return dealerbjValue
#-------------------------------------------------------------------------------
'''
Creates test for all game ending scenarios
Creates game ending screen but still shows cards (nice)
'''
def gameEnding(dealerbjValue,bjValue,bet,win,bettxt,playerlist, dealerlist):

    winsound.PlaySound("BACKMUSIC.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )

    endtxt=Text(Point(85,10),("")).draw(win)

    cover=Rectangle(Point(0,-20),Point(70,20))  #COVERS THE MIDDLE PART FOR THE TEXT
    cover.setFill('light green')                #YOU CAN STILL SEE CARD (NICE)
    cover.draw(win)


    if dealerbjValue == bjValue:
        endtxt.setText("PUSH")
        txt=Text(Point(35,0),"PUSH")
        txt.setSize(30)
        txt.draw(win)

    elif dealerbjValue==21 or bjValue>21 or dealerbjValue<21 and dealerbjValue>bjValue:
        if dealerbjValue==21 and len(dealerlist)==2:
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
        if bjValue==21 and len(playerlist)==2:
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
#-------------------------------------------------------------------------------
'''
Creates a window with a nice background
Used in betting and intro
'''
def setWin():
    win=GraphWin("BLACKJACK",600,600)
    win.setCoords(-100, -100, 100, 100)
    win.setBackground('light green')
    (Image(Point(0,0),("BACKGROUND1.gif"))).draw(win) #NICE BACKGROUND

    return win
#-------------------------------------------------------------------------------
'''
Betting screen with max limit of 200
Buttons to +/- bet
Reactive buttons(if bet is 0 the - buttons grey out
                 if bet is 200 the + buttons grey out)
'''
def betWindow(win,bet):
    win=setWin()
    txt=Text(Point(0,50),"BET CAREFULLY")
    txt.setSize(30)
    txt.setTextColor('light green')
    txt.draw(win)

    txt=Text(Point(0,15),("BET: $"+str(bet)))
    txt.setTextColor('light green')
    txt.setSize(15)
    txt.draw(win)
    startButton = Button(win, Point(0,-45), 40, 10, "CONTINUE")
    startButton.setColor('light green')
    startButton.activate()

    up5 = Button(win, Point(40,0), 30, 10, "+ $5")
    up5.activate()
    down5 = Button(win, Point(-40,0), 30, 10, "- $5")
    down5.activate()

    up10 = Button(win, Point(40,-15), 30, 10, "+ $10")
    up10.activate()
    down10 = Button(win, Point(-40,-15), 30, 10, "- $10")
    down10.activate()

    up20 = Button(win, Point(40,-30), 30, 10, "+ $20")
    up20.activate()
    down20 = Button(win, Point(-40,-30), 30, 10, "- $20")
    down20.activate()

    continu=False
    while continu==False:


        if bet==0 or bet<0:
            down5.deactivate()
            down10.deactivate()
            down20.deactivate()

        elif bet==200 or bet>200:
            up5.deactivate()
            up10.deactivate()
            up20.deactivate()

        elif bet>0:
            down5.activate()
            down10.activate()
            down20.activate()

        if bet<200:
            up5.activate()
            up10.activate()
            up20.activate()

        click = win.getMouse()
        if startButton.clicked(click):
            winsound.PlaySound("CLICK.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
            up5.undraw()
            down5.undraw()
            txt.undraw()
            startButton.undraw()
            continu=True

        if up5.clicked(click):
            bet=bet+5
            txt.setText(("BET: $"+str(bet)))
            if bet>200:
                bet=200
                txt.setText(("BET: $"+str(bet)))
        if down5.clicked(click):
            bet=bet-5
            txt.setText(("BET: $"+str(bet)))
            if bet<0:
                bet=0
                txt.setText(("BET: $"+str(bet)))

        if up10.clicked(click):
            bet=bet+10
            txt.setText(("BET: $"+str(bet)))
            if bet>200:
                bet=200
                txt.setText(("BET: $"+str(bet)))
        if down10.clicked(click):
            bet=bet-10
            txt.setText(("BET: $"+str(bet)))
            if bet<0:
                bet=0
                txt.setText(("BET: $"+str(bet)))

        if up20.clicked(click):
            bet=bet+20
            txt.setText(("BET: $"+str(bet)))
            if bet>200:
                bet=200
                txt.setText(("BET: $"+str(bet)))
        if down20.clicked(click):
            bet=bet-20
            txt.setText(("BET: $"+str(bet)))
            if bet<0:
                bet=0
                txt.setText(("BET: $"+str(bet)))



    win.close()
    return bet
#-------------------------------------------------------------------------------
'''
Sets up the window for the game
Made a background to make it look nice (Playerside/Dealerside)
Rectangle on the right for game info
'''
def setTablewin():
    win=GraphWin("BLACKJACK",1200,600)
    win.setCoords(0,-100, 100, 100)
    win.setBackground('light green')
    (Image(Point(50,0),("BACKGROUND2.gif"))).draw(win)
    backgrnd=Rectangle(Point(70,-100),Point(100,100))
    backgrnd.setFill('white')
    backgrnd.draw(win)
    return win
#-------------------------------------------------------------------------------
'''
Sets up the starting turns
Gives each player 2 cards in turns
Waits in between giving out cards to make it more realistic
'''
def setCards(win,bList):
    playerlist=[]
    dealerlist=[]

    bjValue,dealerbjValue=0,0
    playervtxt=Text(Point(85,-50),("PLAYER HAND VALUE: "+str(bjValue))).draw(win)
    dealervtxt=Text(Point(85,50),("PLAYER HAND VALUE: "+str(dealerbjValue))).draw(win)

    time.sleep(.5)
    hit = pickCard(bList)
    bjValue=hit.bjValue()
    winsound.PlaySound("FLIP.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
    (Image(Point(10,-50),(str(hit)))).draw(win)
    playerlist.append(str(hit))
    playervtxt.setText(("PLAYER HAND VALUE: "+str(bjValue)))

    time.sleep(.5)
    hitd = pickCard(bList)
    dealerbjValue=hitd.bjValue()
    winsound.PlaySound("FLIP.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
    (Image(Point(10,50),(str(hitd)))).draw(win)
    dealerlist.append(str(hitd))
    dealervtxt.setText(("DEALER HAND VALUE: "+str(dealerbjValue)))

    time.sleep(.5)
    hit = pickCard(bList)
    bjValue=bjValue+hit.bjValue()
    winsound.PlaySound("FLIP.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
    (Image(Point(20,-50),(str(hit)))).draw(win)
    playerlist.append(str(hit))
    playervtxt.setText(("PLAYER HAND VALUE: "+str(bjValue)))

    time.sleep(.5)
    hitd = pickCard(bList)
    dealerbjValue= dealerbjValue +hitd.bjValue()
    winsound.PlaySound("FLIP.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
    (Image(Point(20,50),("BACK.gif"))).draw(win)
    dealerlist.append(str(hitd))

    if bjValue>21:
        bjValue=checkAcePlayer(playerlist,bjValue)
    if dealerbjValue>21:
        dealerbjValue=checkAceDealer(dealerlist,dealerbjValue)

    return playerlist, dealerlist, bjValue, dealerbjValue, hitd, playervtxt, dealervtxt
#-------------------------------------------------------------------------------
'''
Players turn
Hit and hold and double down
'''
def playerTurn(win,bjValue,bList,playerlist,playervtxt,bet):
    hitbutton = Button(win, Point(20,0), 10, 20, "HIT")
    hitbutton.setColor('light green')
    hitbutton.activate()
    holdbutton = Button(win, Point(50,0), 10, 20, "STAND")
    holdbutton.activate()
    holdbutton.setColor('light blue')
    ddbutton = Button(win, Point(35,0), 10, 20, "DOUBLE\nDOWN")
    ddbutton.activate()
    ddbutton.setColor('red')


    playerspot=20

    play=True

    while play == True:
        if bjValue==21:
            play=False
        else:
            n=True
            while n==True:
                click = win.getMouse()

                if holdbutton.clicked(click):
                    winsound.PlaySound("CLICK.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                    play=False
                    n=False

                if hitbutton.clicked(click):
                    winsound.PlaySound("CLICK.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                    ddbutton.deactivate()

                    hit = pickCard(bList)
                    playerspot=playerspot+10
                    winsound.PlaySound("FLIP.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                    (Image(Point(playerspot,-50),(str(hit)))).draw(win)
                    playerlist.append(str(hit))
                    value=hit.bjValue()
                    bjValue=bjValue+value
                    n=False


                if ddbutton.clicked(click):
                    bet=bet*2
                    hit = pickCard(bList)
                    playerspot=playerspot+10
                    winsound.PlaySound("FLIP.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                    (Image(Point(playerspot,-50),(str(hit)))).draw(win)
                    playerlist.append(str(hit))
                    value=hit.bjValue()
                    bjValue=bjValue+value
                    play=False
                    n=False




            if bjValue>21:
                bjValue=checkAcePlayer(playerlist,bjValue)

                if bjValue>21:
                    play=False
            if bjValue==21:
                play=False
            playervtxt.setText(("PLAYER HAND VALUE: "+str(bjValue)))

    hitbutton.setColor('light green')
    hitbutton.deactivate()

    holdbutton.setColor('light blue')
    holdbutton.deactivate()

    return bjValue,playerlist,bet
#-------------------------------------------------------------------------------
'''
Dealer picks a card
'''
def dealerPick(win,dealerspot,bList,dealerbjValue,dealervtxt,dealerlist):
    time.sleep(.5)
    dealerspot=dealerspot+10
    hitd = pickCard(bList)
    winsound.PlaySound("FLIP.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
    (Image(Point(dealerspot,50),((str(hitd))))).draw(win)
    dealerlist.append(str(hitd))
    valueD=hitd.bjValue()
    dealerbjValue=dealerbjValue+valueD
    dealervtxt.setText(("DEALER HAND VALUE: "+str(dealerbjValue)))
    return dealerbjValue,dealerspot
#-------------------------------------------------------------------------------
'''
Dealers turns
'''
def dealerTurn(win,bjValue,dealerbjValue,hitd,dealerlist,dealervtxt,bList):
    (Image(Point(20,50),(str(hitd)))).draw(win)

    dealerspot=20

    if bjValue<21:

        while int(dealerbjValue)<17:
            dealerbjValue,dealerspot=dealerPick(win,dealerspot,bList,dealerbjValue,dealervtxt,dealerlist)

        if dealerbjValue > 21:
            dealerbjValue=checkAceDealer(dealerlist,dealerbjValue)

        if dealerbjValue < 17:
            while int(dealerbjValue)< 17:
                dealerbjValue,dealerspot= dealerPick(win,dealerspot,bList,dealerbjValue,dealervtxt,dealerlist)

    dealervtxt.setText(("DEALER HAND VALUE: "+str(dealerbjValue)))

    return dealerbjValue,dealerlist
#-------------------------------------------------------------------------------
'''
Gets the bet
Gives 2 cards to each
Starts the players turn
Starts the dealers turn
Starts the ending screen
'''
def playTurn(win,bList,bet,redcard):

    bet=betWindow(win,bet)

    win=setTablewin()

    bettxt=Text(Point(85,-10),("BET: $"+str(bet))).draw(win)

    playerlist, dealerlist, bjValue, dealerbjValue, hitd, playervtxt, dealervtxt=setCards(win,bList)

    bjValue,playerlist,bet=playerTurn(win,bjValue,bList,playerlist,playervtxt,bet)

    dealerbjValue,dealerlist=dealerTurn(win,bjValue,dealerbjValue,hitd,dealerlist,dealervtxt,bList)

    bet=gameEnding(dealerbjValue,bjValue,bet,win,bettxt, playerlist, dealerlist)


    quitbutton = Button(win, Point(95,-95), 10, 10, "QUIT")
    quitbutton.setColor('red')
    quitbutton.activate()
    pabutton = Button(win, Point(75,-95), 10, 10, "PLAY AGAIN")
    pabutton.setColor('light green')
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

    playTurn(win,bList,bet,redcard)
#-------------------------------------------------------------------------------
'''
Sets up a title screen
with a button
'''
def titleScreen(win):
    txt=Text(Point(0,30),"BLACKJACK\nby Amardeep Singh")
    txt.setSize(30)
    txt.setStyle('bold')
    txt.setTextColor('light green')
    txt.draw(win)

    startButton = Button(win, Point(0,0), 40, 10, "START GAME")
    startButton.setColor('light green')
    startButton.activate()
    start=False
    while start==False:
        click = win.getMouse()
        if startButton.clicked(click):
            txt.undraw()
            startButton.deactivate()
            startButton.undraw()

            start=True
    win.close()
#-------------------------------------------------------------------------------
'''
Picks the shuffel card at random (40%-60%)
Starts the intro
Starts the turns
'''
def playGame(bList):

    redcard=167+ random.randrange(0,81)

    win=setWin()

    titleScreen(win)

    bet=0

    playTurn(win,bList,bet,redcard)
#-------------------------------------------------------------------------------
'''
Main function
Starts the background music
creates a burnlist that is used throughout the game
error handling
'''
def main():
    try:

        winsound.PlaySound("BACKMUSIC.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )

        bList=[]

        playGame(bList)

    except:
        winsound.PlaySound(None, winsound.SND_ASYNC)
        quit()

main()
#-------------------------------------------------------------------------------








