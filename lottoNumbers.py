import random

BALLS = 5
LO = 1
HI = 69
PBMAX = 26

def get_ball_value(lo = LO, hi = HI):
    "return a random number in the specified range"
    return random.randint(lo, hi)

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

if __name__ == "__main__":
    "run the code"
    mypicks = get_white_balls(), get_Powerball()
    print(mypicks)


