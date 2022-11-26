from math import sqrt
from random import choice 
from utils import medium_attack, medium_defend, hard_attack, hard_defend

def easy(state, val):
    """
        Function that simulates an easy AI mode.
        Strategy:
            - Easy: Pick an empty position at random.
    """
    temp = []

    for key, value in state.items():
        if value == "—":
            temp.append(key)

    if len(temp) > 0:
        play = choice(temp)
        state[play] = val

    return state



def medium(state, val):
    """
        Function that simulates a medium AI mode.
        Strategy:
            - Medium: Use a faulty minimax with alpha beta prunning.
    """
    n = int(sqrt(len(state)))
    count = 0 
    inx = 0
    temp = [[] for i in range(n)]

    #generate list of lists for board state
    for key, value in state.items():
        if count != 0 and count % n == 0:
            inx += 1
        
        temp[inx].append(value)

        count += 1

    if len(temp) > 0:
        if val == "X":
            play = medium_attack(temp, -2, 2, val)
            # print("\n ATTACK", val, play )
        else:
            play = medium_defend(temp, -2, 2, val)
            # print("\n DEFEND", val, play )

        key = f"({play[1]},{play[2]})"
        state[key] = val

    return state

# @memoization
def hard(state, val):
    """
        Function that simulates a hard AI mode.
        Strategy:
            - Hard: Use minimax with alpha beta prunning.
    """
    if val == "X":
        return hard_attack(state, val)
    else:
        return hard_defend(state, val)