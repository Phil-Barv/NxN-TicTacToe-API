from game import TicTacToe
from utils import _check_is_win
import matplotlib.pyplot as plt

def play_game(attack, AI):
    """
        Function that simulates AI vs AI game. Returns win, loss, draw
    """
    a = TicTacToe(3)
    board = a.board
    status = _check_is_win(board)

    while status == "Continue":
        if attack:
            player = "X"
        else:
            player = "O"

        #make next move
        board = a.get_best_next(board, player, AI)

        #change player after turn
        attack = not attack

        #update status
        status = _check_is_win(board)

    return status

def stats(lst):
    wins = lst.count("X")
    loss = lst.count("O")
    draws = lst.count("—")
    return wins, loss, draws


def evaluate_AI(trials, AI):
    """
        Function that simulates AI v AI trials such that 50% trials are defend.
    """

    results_AI1 = []
    results_AI2 = []
    tests = [i for i in range(trials)]

    print("\nLoading AI")

    print("\nRunning simulation, please wait...")

    for i in range(trials):
        if i % 2 == 0:
            results_AI1.append(play_game(True, AI))
        if i % 2 == 1:
            results_AI2.append(play_game(False, AI))

    print("\nSimulation completed.")

    #generate stats
    ai1 = stats(results_AI1)
    ai2 = stats(results_AI2)

    print(f"\nAI1 had {ai1[0]} wins, {ai1[1]} losses and {ai1[2]} draws.")
    print(f"\nAI2 had {ai2[0]} wins, {ai2[1]} losses and {ai2[2]} draws.\n")

    return results_AI1, results_AI2

#run sim
if __name__ == "__main__":
    #insert trials, strat: Hard, Medium, Easy
    print(evaluate_AI(10, "Hard"))
    
