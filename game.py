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

from queue import PriorityQueue
from collections import deque
from copy import deepcopy
# import numpy as np
import itertools
from math import sqrt

from ai_engine import easy, medium, hard
from utils import _check_is_win, eval_function

class TicTacToe:
    """
    Class TicTacToe: Provides a structure for performing search
    Input:
        -size: int value of n, the nxn size of the board
        -create_PD: optional settting to create pattern database, default False
    """
    #class variable accessible to all instances of PuzzleNode
    pattern_database = None

    def __init__(self, size, create_PD=False):
        self.board = {}

        #create nxn board
        for i in range(size):
            for j in range(size):
                self.board[f"({i},{j})"] = "—"

        #creating database once for all instances
        if TicTacToe.pattern_database is None and create_PD:
            TicTacToe.pattern_database = self.create_database(size)

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

    def get_best_next(self, state, val, strategy):
        """
            A function that simulates the next best move given current board
            Input:
                -state: board state
                -strategy: AI algorithm to use
            Output:
                -state: simulated board of next best move
        """
        return self.play_ai(state, val, strategy)
    
    def create_database(self, size=3):
        """
            A function that creates the pattern database
            Input: 
                -None
            Output:
                -entries: a dictionary of permutations that gradually updates
        """
        # Generate start configuration
        start = {}
        
        #create nxn size board
        for i in range(size):
            for j in range(size):
                start[f"({i},{j})"] = "—"

        #opt-next move is always opening center
        temp = deepcopy(start)
        next_move = self.get_best_next(temp, "X", "Hard")

        # Initialize queue with start value
        queue = deque([[start, next_move]])
        
        # Initialize pattern database
        entries = {}
        
        # Initialize helper to track visited nodes
        visited = set()

        # Print UX updates
        print("\nGenerating database...")
        print("Collecting entries...\n")

        attack = True

        while queue:
            #pop first item from queue
            entry = queue.popleft()

            #initialize state and next state
            state, next_state = entry[0], entry[1]

            #update PD
            print("Current == Next:", state==next_state)
    
            if not str(state) in visited:
                entries[str(state)] = next_state
                visited.add(str(state))

            #check if game over
            winner = _check_is_win(state)

            if winner != "Continue":
                break

            #DEBUG PRINTS -> Shows len, state, next state
            print(f"\n\nRound {len(entries)}:")

            #switch player
            attack = not attack

            #switch case strategy
            if attack:
                player = "X"
            else:
                player = "O"

            #generate children, i.e, simulate game
            temp1 = deepcopy(next_state)
            next_move = self.get_best_next(temp1, player, "Hard")
            queue.append([next_state, next_move])

            # Print progress for every 10000 entries in visited.
            if len(entries) % 10000 == 0:
                print("Entries collected: " + str(len(entries)))

            #9!/2 = 181440 possible permutations, hence stop when all found
            if len(entries) >= 181440:
                break

        print("\nDatabase Size", len(entries), "\n")

        return entries

