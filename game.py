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

from ai_engine import easy, medium, hard

class TicTacToe:
    def __init__(self, size):
        self.board = {}

        #create nxn board
        for i in range(size):
            for j in range(size):
                self.board[f"({i},{j})"] = "—"

    def board(self):
        """
            Function that returns the local board
        """
        return self.board

    def play_human(self, state, pos, move):
        """
            Function that simulates the user's move
            Input:
                - state: prod board state
                - pos: x, y coords
                - move: "X" or "O"
            Output:
                - state: simulated board
        """
        #switch case for local v. production use
        if state:
            pass
        else:
            state = self.board

        #generate a key from pos
        key = f"({pos[0]},{pos[1]})"

        if key in state.keys():
            state[key] = move
        
        # self.board["(1,1)"] = "O"
        return state
    
    def play_ai(self, state, val, strategy):
        """
            Function that simulates the AI's move
            Input:
                - state: prod board state
                - pos: x, y coords
                - move: "X" or "O"
            Output:
                - state: simulated board
        """
        #switch case for local v. production use
        if state:
            pass
        else:
            state = self.board

        #switch case strategy
        if strategy == "Hard":
            return hard(state, val)

        elif strategy == "Medium":
            return medium(state, val)

        else:
            return easy(state, val)


