"""Powerball Win Checker

This program checks for winning Powerball lottery combinations:

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

Amounts and odds can be found at: https://www.powerball.net/prizes

"""
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

