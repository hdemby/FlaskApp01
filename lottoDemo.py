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
from lottoNumbers import *
from chkLottoPick import *

def getTicket(plays = 5):
    "generate a lottery ticket; default 5 plays"
    mypicks = []
    plays = 5
    while plays:
        print("%s plays left.." % plays)
        picks = input("enter list of 5 non-repeating numbers between 1 and 69: ")
        picks = picks and set(eval(picks)) or get_white_balls()
        pball = input("enter a powerball value between 1 and 26: ")
        pball = pball and int(pball) or get_Powerball()
        mypicks.append([picks, pball])
        plays -= 1
    return mypicks

def showTkt(mypicks):
    "display current ticket"
    for play in mypicks:
        print(play)
    return

def chk_ticket(myTkt, winningTkt):
    "return results of game drawing"
    for pick in myTkt:
        chkJackpot(pick, winningTkt)
        powerball = chkPowerball(pick, winningTkt[1])
        matches = chkBallMatches(pick, winningTkt)
        print(matches and "matches: %s, " % matches or "No matches, ", powerball and "Powerball, " or "No Powerball, ", \
              "winnings: $" + str(winnings(len(matches), powerball)))
    return

if __name__ == "__main__":
    "play the Powerball Lottery"
    myplays = getTicket()
    showTkt(myplays)
    winningTkt = set(get_white_balls()), get_Powerball()
    print("Drawing Result: ", winningTkt)
    chk_ticket(myplays, winningTkt)

## Lottery Game Simulation
----------------------------
# -- Parameters --:
# RandomBallRange ==> 1-69
# NumberBalls ==> 5
# PowerBallRange == 1-26
# PowerPlayCost ==> 1
#
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



