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

# @memoization
def check_win(state):
    """
        Function that checks the win status of a board.
        Input: 
            - state: the current board state.
        Output:
            - True/False/Draw: win status of the board.
    """
    lst = list(state.keys())
    n = int(sqrt(len(lst)))

    #check rows
    for i in range(n):
        for j in range(n-1):
            if state[f"({i},{j})"] == "—" or state[f"({i},{j+1})"] == "—" or state[f"({i},{j})"] != state[f"({i},{j+1})"]:
                break
        else:
            return True


    #check columns
    for j in range(n):
        for i in range(n-1):
            if state[f"({i},{j})"] == "—" or state[f"({i+1},{j})"] == "—" or state[f"({i},{j})"] != state[f"({i+1},{j})"]:
                break
        else:
            return True


    #check left diagonal
    for i in range(n-1):
        if state[f"({i},{i})"] == "—" or state[f"({i+1},{i+1})"] == "—" or state[f"({i},{i})"] != state[f"({i+1},{i+1})"]:
            break
    else:
        return True

    #check right diagonal
    for i in range(n -1):
        empty = state[f"({i},{n-i-1})"] == "—" or state[f"({i+1},{n-i-2})"] == "—"
        diff = state[f"({i},{n-i-1})"] != state[f"({i+1},{n-i-2})"]

        if empty or diff:
            break

    else:
        return True


    #draw 
    if "—" not in list(state.values()):
        return "Draw"

    # #continue game
    # elif "—" in list(state.values()):
    #     return None
    #no win 
    else:
        return False


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

    # print(f"\n\nOUTCOME - Winner:{winner} | Depth:{depth} | State:")
    # i = 0
    # mod = sqrt(len(state))

    # for item in state.items():
    #     if i % mod == 0:
    #         print("\n")
    #     print(f"| {item[1]} ", end="")
    #     i+= 1
    # print("\n")

    if winner == "X":
        return 10

    elif winner == "O":
        return -10

    elif winner == "—":
        return 0

    if attack:
        mx = alpha

        for key in state.keys():
            if state[key] == "—":
                state[key] = "X"
                score = minimax_abp(state, depth + 1, alpha, beta, False)
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
                score = minimax_abp(state, depth + 1, alpha, beta, True)
                state[key] = "—"

                mn = min(score, mn)
                beta = min(beta, score)

                if beta <= alpha:
                    break

        # print("MIN", mn, "\n\n")
        return mn


# Checks if the game has ended and returns the winner in each case
def _check_is_win(state):
    n = int(sqrt(len(state)))
    
    if not isinstance(state, list):
        temp = [[] for _ in range(n)]
        count = 0
        inx = 0

        for key, value in state.items():
            if count != 0 and count % n == 0:
                inx += 1

            temp[inx].append(value)
            count += 1

        state = temp

    # print("\nTEMP", temp)

    # Vertical win
    for i in range(n):
        if (state[0][i] != '—' and state[0][i] == state[1][i] and state[1][i] == state[2][i]):
            return state[0][i]

    # Horizontal win
    for i in range(n):
        if (state[i] == ['X', 'X', 'X']):
            return 'X'
        elif (state[i] == ['O', 'O', 'O']):
            return 'O'

    # Main diagonal win
    if (state[0][0] != '—' and
        state[0][0] == state[1][1] and
        state[0][0] == state[2][2]):
        return state[0][0]

    # Second diagonal win
    if (state[0][2] != '—' and state[0][2] == state[1][1] and state[0][2] == state[2][0]):
        return state[0][2]

    # Is whole board full?
    for i in range(n):
        for j in range(n):
            # There's an empty field, we continue the game
            if (state[i][j] == '—'):
                return "Continue"

    # It's a tie!
    return '—'
