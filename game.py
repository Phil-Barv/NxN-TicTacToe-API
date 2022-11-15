# class Cell:
#     def __init__(self, val, i, j):
#         #either an X, O, or -
#         self.value = val

#         #the (i, j) position in the board
#         self.position = (i, j)

#     # def __repr__(self):
#     #     return f"Cell({self.position}, {self.value})"

#     def same(self, other):
#         return self.value == other.value
from random import choice
from math import sqrt

class TicTacToe:
    def __init__(self, size):
        self.board = {}

        for i in range(size):
            for j in range(size):
                self.board[f"({i},{j})"] = "—"

    def board(self):
        return self.board

    def play_human(self, pos, move):
        key = f"({pos[0]},{pos[1]})"

        if key in self.board.keys():
            self.board[key] = move
        
        # self.board["(1,1)"] = "O"
        return self.board

    def play_ai(self, state, val):

        temp = []

        for key, value in state.items():
            if value == "—":
                temp.append(key)

        if len(temp) > 0:
            play = choice(temp)
            state[play] = val

        return state

    def check_win(self, state):
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

        #no win 
        return False



