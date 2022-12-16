from math import sqrt

def memoization(function):
    """
        A decorator function that memoizases win values and returns the cached 
        result rather than continuously recalculating it.
        Input:
            -function: a check win function
        Output:
            -memo[key]: win value
            -wrapper: a function
    """
    #initialize cache dictionary
    memo = {}
    
    def wrapper(*args):
        #make a hashable string
        key = str(args[0])
        
        #add new key if not in dict already
        if key not in memo:
            memo[key] = function(args[0])
            
        return memo[key]

    return wrapper

def check_win(state):
    """
        Function that checks the win status of a board to update frontend.
        Input: 
            - state: the current board state.
        Output:
            - True/False/Draw: win status of the board.
    """
    #get board nxn size
    n = int(sqrt(len(state)))
    
    #handle dict unpacking
    if not isinstance(state, list):
        temp = [[] for _ in range(n)]
        count = 0
        inx = 0

        for value in state.values():
            if count != 0 and count % n == 0:
                inx += 1

            temp[inx].append(value)
            count += 1

        state = temp

    #generate board cols, main, other
    cols = [ [row[i] for row in state] for i in range(n)]
    main = [ state[i][i] for i in range(n)]
    other =  [state[i][n-i-1] for i in range(n)]
    
    # print("\n\nSTATE", state, "\n\nCOLS", cols, "\n\nMAIN", main, "\n\nOTHER", other)

    #rows and cols
    for i in range(n):
        for j in range(n):
            #check col win
            if cols[i].count(cols[i][j]) == n and cols[i][j] != "—":
                #winner is X or O
                return True

            #check row win
            if state[i].count(state[i][j]) == n and state[i][j] != "—":
                #winner is X or O
                return True

        #main
        if main.count(main[i]) == n and main[i] != "—":
            #winner is X or O
            return True

        #other
        if other.count(other[i]) == n and other[i] != "—":
            #winner is X or O
            return True

    #check full board
    for i in range(n):
        for j in range(n):
            #empy spot means continue game
            if state[i][j] == '—':
                return False

    #draw
    return 'Draw'

def eval_function(state):
    """
        Function that evaluates a board in a non-terminal position
        Input:
            - state: current state of the board
        Output:
            - eval: a numeric value indicating utility
    """
    #initialize eval value
    eval_x, eval_o = 0, 0 
    
    #get board nxn size
    n = int(sqrt(len(state)))
    
    #handle dict unpacking
    if not isinstance(state, list):
        temp = [[] for _ in range(n)]
        count = 0
        inx = 0

        for value in state.values():
            if count != 0 and count % n == 0:
                inx += 1

            temp[inx].append(value)
            count += 1

        state = temp

    #generate board cols, main, other
    cols = [ [row[i] for row in state] for i in range(n)]
    main = [ state[i][i] for i in range(n)]
    other =  [state[i][n-i-1] for i in range(n)]
    
    # print(cols, main, other)
    # print("\n\nSTATE", state, "\n\nCOLS", cols, "\n\nMAIN", main, "\n\nOTHER", other)

    #rows and cols
    for i in range(n):
        # print("X", cols[i].count("X"), state[i].count("X"), eval_x)
        # print("O", cols[i].count("O"), state[i].count("O"), eval_o)

        #check cols, rows
        eval_x += cols[i].count("X") + state[i].count("X") 
        eval_o += cols[i].count("O") + state[i].count("O") 

    #check main, other
    eval_x += main.count("X") + other.count("X")
    eval_o += main.count("O") + other.count("O")

    return eval_x, eval_o, eval_x-eval_o

    
def medium_attack(state, alpha, beta, val):
    """
        Function that simulates AI attack using a faulty minimax alpha-beta prunning
    """
    # -1 loss 0 draw 1 win
    max_value = -2 
    n = len(state)
    x, y = None, None
    result = _check_is_win(state)
    # print("\n", "win-status-attack: ", result)

    if result == "X":
        return (-1, 0, 0)
    elif result == "O":
        # print("bug", result)
        return (1, 0, 0)
    elif result == "—":
        return (0, 0, 0)

    for i in range(n):
        for j in range(n):
            if state[i][j] == "—":
                state[i][j] = val
                (m, min_i, min_j) = medium_defend(state, alpha, beta, val)
                if m-1 > max_value:
                    max_value = m-1
                    x = i
                    y = j
                state[i][j] = "—"

                if max_value >= beta:
                    return (max_value, x, y)

                if max_value > alpha:
                    alpha = max_value

    return (max_value, x, y)


def medium_defend(state, alpha, beta, val):
    """
        Function that simulates AI defense using a faulty minimax alpha-beta prunning
    """
    # -1 loss 0 draw 1 win
    min_value = 2 
    n = len(state)
    x, y = None, None
    result = _check_is_win(state)
    # print("\n", "win-status-defend: ", result)

    if result == "X":
        return (-1, 0, 0)
    elif result == "O":
        print("bug", result)
        return (1, 0, 0)
    elif result == "—":
        return (0, 0, 0)

    for i in range(n):
        for j in range(n):
            if state[i][j] == "—":
                state[i][j] = val
                (m, max_i, max_j) = medium_attack(state, alpha, beta, val)
                if m-1 < min_value:
                    min_value = m-1
                    x = i
                    y = j
                state[i][j] = "—"

                if min_value <= alpha:
                    return (min_value, x, y)

                if min_value < beta:
                    beta = min_value

    return (min_value, x, y)



def hard_attack(state, val):
    """
        Function that simulates a hard AI mode attack.
        Strategy:
            - Hard: Use minimax with alpha beta prunning.
    """
    current = -800
    move = 0

    for key in state.keys():
        if state[key] == "—":
            state[key] = val
            score = minimax_abp(state, 0, -800, 800, False)
            state[key] = "—"

            if score > current:
                current = score
                move = key

    state[move] = val

    return state

def hard_defend(state, val):
    """
        Function that simulates a hard AI mode defend.
        Strategy:
            - Hard: Use minimax with alpha beta prunning.
    """
    current = 800
    move = 0

    for key in state.keys():
        if state[key] == "—":
            state[key] = val
            score = minimax_abp(state, 0, -800, 800, True)
            state[key] = "—"

            if score < current:
                current = score
                move = key

    state[move] = val

    return state

# @memoization
def minimax_abp(state, depth, alpha, beta, attack):
    """
        Function that simulates AI play using minimax alpha-beta prunning
    """
    winner = _check_is_win(state)

    if winner == "X":
        return 10

    elif winner == "O":
        return -10

    elif winner == "—":
        return 0

    # #optimization for non-terminal state
    # if depth > 9:
    #     return eval_function(state)

    if attack:
        mx = alpha

        for key in state.keys():
            if state[key] == "—":
                state[key] = "X"
                score = minimax_abp(state, depth + 1, alpha, beta, False) - (depth + 1)
                state[key] = "—"

                mx = max(score, mx)
                alpha = max(alpha, score)

                if beta <= alpha:
                    break

        # print("MAX", mx, "\n\n")

        return mx

    #minimize
    else:
        mn = beta

        for key in state.keys():
            if state[key] == "—":
                state[key] = "O"
                score = minimax_abp(state, depth + 1, alpha, beta, True) + (depth + 1)
                state[key] = "—"

                mn = min(score, mn)
                beta = min(beta, score)

                if beta <= alpha:
                    break

        # print("MIN", mn, "\n\n")

        return mn

# Checks if the game has ended and returns the winner in each case
def _check_is_win(state):
    """
        Internal use function that checks the win status of a board and return the winner.
        Input: 
            - state: the current board state.
        Output:
            - X/O/—/Continue: win status of the board.
    """
    #get board nxn size
    n = int(sqrt(len(state)))
    
    #handle dict unpacking
    if not isinstance(state, list):
        temp = [[] for _ in range(n)]
        count = 0
        inx = 0

        for value in state.values():
            if count != 0 and count % n == 0:
                inx += 1

            temp[inx].append(value)
            count += 1

        state = temp

    #generate board cols, main, other
    cols = [ [row[i] for row in state] for i in range(n)]
    main = [ state[i][i] for i in range(n)]
    other =  [state[i][n-i-1] for i in range(n)]
    
    # print("\n\nSTATE", state, "\n\nCOLS", cols, "\n\nMAIN", main, "\n\nOTHER", other)

    #rows and cols
    for i in range(n):
        for j in range(n):
            #check col win
            if cols[i].count(cols[i][j]) == n and cols[i][j] != "—":
                #winner is X or O
                return cols[i][j] 

            #check row win
            if state[i].count(state[i][j]) == n and state[i][j] != "—":
                #winner is X or O
                return state[i][j] 

        #main
        if main.count(main[i]) == n and main[i] != "—":
            #winner is X or O
            return main[i]

        #other
        if other.count(other[i]) == n and other[i] != "—":
            #winner is X or O
            return other[i]

    #check full board
    for i in range(n):
        for j in range(n):
            #empy spot
            if state[i][j] == '—':
                return "Continue"

    #draw
    return '—'

