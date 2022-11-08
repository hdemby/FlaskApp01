""" POWERBALL Lotto Sim

Plays a Powerball lotto game
Prize Level         Payout	    Odds

Match 5 + PB	    Jackpot	    1 in 292,201,338
Match 5	            $1,000,000	1 in 11,688,054
Match 4 + PB	    $50,000	    1 in 913,129
Match 4	            $100	    1 in 36,525
Match 3 + PB	    $100	    1 in 14,494
Match 3	            $7	        1 in 580
Match 2 + PB	    $7	        1 in 701
Match 1 + PB	    $4	        1 in 92
Match 0 + PB	    $4	        1 in 38

The overall odds of winning a Powerball prize are approximately 1 in 24.9

"""
#from lottoNumbers import *
#from chkLottoPick import *
import random

#-- PARAMETERS --
BALLS = 5
LO = 1
HI = 69
PBMAX = 26
PowerPlayCost = 1

JACKPOT = 1900000000
PAYOUTS = {
    (5, True): JACKPOT,
    (5, False): 1000000,
    (4, True): 50000,
    (4, False): 100,
    (3, True): 100,
    (3, False): 7,
    (2, True): 7,
    (1, True): 4,
    (0, True): 4,
    (2, False): 0,
    (1, False): 0,
    (0, False): 0,
}

##======================== No value changes beneath this line =====================
## --- MODEL ---
# These functions create and populate the objects for this program

def get_white_balls(balls = BALLS, lo = LO, hi = HI):
    "returns the number of requested random balls in the range specified"
    whiteBalls = set([])
    while len(whiteBalls) < balls:
        x = get_ball_value(lo, hi)
        try:
            whiteBalls.add(x)
            #print(x)
        except:
            pass
    return whiteBalls

def get_Powerball(lo = LO, hi = PBMAX):
    "return a powerball in the given range"
    return get_ball_value(lo, hi)

def getIntValue(query):
    "return an integer value for a request with rejection of no values entered"
    value = None
    while not value:
        value = True and 0 or input("%s: " % query)
    return int(value)

def getBoolValue(query):
    "return a boolean value for the request with 'False' returned for no entry"
    value = True and input(query).lower() in ['y', 'yes'] or False
    return value

## --- CONTROLLER ---
# these functions evaluate and manipulate user input

def chkJackpot(myTkt, winningTkt):
    "quick check for jackpot win"
    return myTkt == winningTkt

def chkPowerball(myball, powerball):
    "check for powerball match"
    return myball == powerball

def chkBallMatches(mypicks, whiteballs):
    "check ticket for ball matches"
    return mypicks[0].intersection(whiteballs[0])

def winnings(matches, powerball):
    "return results of matches"
    payouts = PAYOUTS
    return payouts[(matches, powerball)]

def getPicks(balls = BALLS, hi = HI):
    "return set # of ball values in defined range"
    picks = set()
    print(f"Pick {balls} numbers between 1 and {hi}: ")
    while len(picks) < balls:
        pick = getIntValue("?: ")
        if 1 <= pick <= hi:
            picks.add(pick)
            print(picks)
        else:
            print("Your value is not in the range 1 - %s. Please try again..." % hi)
    return picks

## --- VIEW ---
# These functions accept user input and display results
def getTicket(plays = 1):
    "generate a lottery ticket with number of plays"
    mypicks = []
    while plays:
        print("%s plays left.." % plays)
        picks = getPicks()
        pball = getIntValue("enter a powerball value between 1 and 26: ")
        mypicks.append([picks, pball])
        plays -= 1
    return mypicks

def showTkt(mypicks):
    "display current ticket"
    for play in mypicks:
        print("Balls:{:<20s} Powerball:{}".format(str(sorted(list(play[0]))), play[1]))
    return

def chk_ticket(myTkt, winningTkt):
    "return results of game drawing"
    payouts = PAYOUTS
    for pick in myTkt:
        if chkJackpot(pick, winningTkt):
            print("YOU WON THE JACKPOT")
            winnings = payouts[(5, True)]
        else:
            powerball = chkPowerball(pick, winningTkt[1])
            matches = chkBallMatches(pick, winningTkt)
            print(matches and "matches: %s, " % matches or "No matches, ", powerball and "Powerball, " or "No Powerball, ", \
              "winnings: $" + str(winnings(len(matches), powerball)))
            winnings = payouts[(len(matches), powerball)]
    return )

def main():
    "Play the game..."
    # Set game parameters:
    budget = getIntValue("How much money do you have to gamble? ")
    plays = getIntValue("How many games do you want to play?: ")
    powerplay = getBoolValue("Do you want to use the 'Powerplay'?: ") and 1 or 0
    # Play the game play budget supports it:
    While (playcost + powerplay) * plays < budget:
        # get a lottery ticket...
        myplays = getTicket(getIntValue("How many games would you like to play?: "))
        showTkt(myplays)
        # do the lottery drawing...
        winningTkt = set(get_white_balls()), get_Powerball()
        print("Drawing Result: ", winningTkt)
        # check ticket against drawing...
        winnings = chk_ticket(myplays, winningTkt)
        # report accounting ...
        budget += winnings - (playcost + powerplay) * plays
        if getBoolValue("You have {} dollars left. Keep Playing?: ".format(budget)):
            exit()
    return

if __name__ == "__main__":
    "play the Powerball Lottery"
    # -- Game Play --
    main()

## Lottery Game Simulation
----------------------------
# -- Game Play --
# set a budget ==> budget
# Create your tickets:
------------------------
#   get number of plays desired:
#   for each play:
#       enter your own numbers and powerball or generate random ticket:
#   calculate cost:
#       choose powerplay and number of drawings
#       cost = (costPerPlay + powerplay) * len(ticket) * drawings
#  budget -= cost
#
# While budget > 0:
#   winnings = 0
#   do drawing for winning ticket
#   for each play in ticket:
#      check ticket for jackpot
#      check ticket for powerball
#      add result to winnings
#
# report ticket and cost:
#    budget += winnings
#



