from game import TicTacToe
from utils import _check_is_win

import unittest

class TestTicTacToeAI(unittest.TestCase):
    def test_generate_board_success(self):
        """
            Check board generaed successfully
        """
        test_board = TicTacToe(3).board
        board = {
                "(0,0)": "\u2014",
                "(0,1)": "\u2014",
                "(0,2)": "\u2014",
                "(1,0)": "\u2014",
                "(1,1)": "\u2014",
                "(1,2)": "\u2014",
                "(2,0)": "\u2014",
                "(2,1)": "\u2014",
                "(2,2)": "\u2014"
            }
        return self.assertEqual(test_board, board, "Wrong board generated")

    
    def test_check_win_for_win_row1(self):
        """
            Test correct win detection for row1 diagonal
        """
        board = {
                "(0,0)": "X",
                "(0,1)": "X",
                "(0,2)": "X",
                "(1,0)": "\u2014",
                "(1,1)": "\u2014",
                "(1,2)": "\u2014",
                "(2,0)": "\u2014",
                "(2,1)": "\u2014",
                "(2,2)": "\u2014",
            }
        return self.assertEqual("X", _check_is_win(board))
        

    def test_check_win_for_win_row2(self):
        """
            Test correct win detection for row2 diagonal
        """
        board = {
                "(0,0)": "\u2014",
                "(0,1)": "\u2014",
                "(0,2)": "\u2014",
                "(1,0)": "X",
                "(1,1)": "X",
                "(1,2)": "X",
                "(2,0)": "\u2014",
                "(2,1)": "\u2014",
                "(2,2)": "\u2014",
            }
        return self.assertEqual("X", _check_is_win(board))
        
    
    def test_check_win_for_win_row3(self):
        """
            Test correct win detection for row3 diagonal
        """
        board = {
                "(0,0)": "\u2014",
                "(0,1)": "\u2014",
                "(0,2)": "\u2014",
                "(1,0)": "\u2014",
                "(1,1)": "\u2014",
                "(1,2)": "\u2014",
                "(2,0)": "X",
                "(2,1)": "X",
                "(2,2)": "X",
            }
        return self.assertEqual("X", _check_is_win(board))
        
    def test_check_win_for_win_col1(self):
        """
            Test correct win detection for col1 diagonal
        """
        board = {
                "(0,0)": "X",
                "(0,1)": "\u2014",
                "(0,2)": "\u2014",
                "(1,0)": "X",
                "(1,1)": "\u2014",
                "(1,2)": "\u2014",
                "(2,0)": "X",
                "(2,1)": "\u2014",
                "(2,2)": "\u2014",
            }
        return self.assertEqual("X", _check_is_win(board))


    def test_check_win_for_win_col2(self):
        """
            Test correct win detection for col2 diagonal
        """
        board = {
                "(0,0)": "\u2014",
                "(0,1)": "X",
                "(0,2)": "\u2014",
                "(1,0)": "\u2014",
                "(1,1)": "X",
                "(1,2)": "\u2014",
                "(2,0)": "\u2014",
                "(2,1)": "X",
                "(2,2)": "\u2014",
            }
        return self.assertEqual("X", _check_is_win(board))

    def test_check_win_for_win_col3(self):
        """
            Test correct win detection for col3 diagonal
        """
        board = {
                "(0,0)": "\u2014",
                "(0,1)": "\u2014",
                "(0,2)": "X",
                "(1,0)": "\u2014",
                "(1,1)": "\u2014",
                "(1,2)": "X",
                "(2,0)": "\u2014",
                "(2,1)": "\u2014",
                "(2,2)": "X",
            }
        return self.assertEqual("X", _check_is_win(board))
        

    def test_check_win_for_win_main_diagonal(self):
        """
            Test correct win detection for main diagonal
        """
        board = {
                "(0,0)": "X",
                "(0,1)": "\u2014",
                "(0,2)": "\u2014",
                "(1,0)": "\u2014",
                "(1,1)": "X",
                "(1,2)": "\u2014",
                "(2,0)": "\u2014",
                "(2,1)": "\u2014",
                "(2,2)": "X",
            }
        return self.assertEqual("X", _check_is_win(board))
        

    def test_check_win_for_win_other_diagonal(self):
        """
            Test correct win detection for other diagonal
        """
        board = {
                "(0,0)": "\u2014",
                "(0,1)": "\u2014",
                "(0,2)": "X",
                "(1,0)": "\u2014",
                "(1,1)": "X",
                "(1,2)": "\u2014",
                "(2,0)": "X",
                "(2,1)": "\u2014",
                "(2,2)": "\u2014",
            }
        return self.assertEqual("X", _check_is_win(board))
        

    def test_check_win_for_O_player(self):
        """
            Test correct win detection for other player on other diagonal
        """
        board = {
                "(0,0)": "\u2014",
                "(0,1)": "\u2014",
                "(0,2)": "O",
                "(1,0)": "\u2014",
                "(1,1)": "O",
                "(1,2)": "\u2014",
                "(2,0)": "O",
                "(2,1)": "\u2014",
                "(2,2)": "\u2014",
            }
        return self.assertEqual("O", _check_is_win(board))


    def test_check_win_for_no_player(self):
        """
            Test correct win detection for no winner
        """
        board = {
                "(0,0)": "\u2014",
                "(0,1)": "\u2014",
                "(0,2)": "O",
                "(1,0)": "\u2014",
                "(1,1)": "O",
                "(1,2)": "\u2014",
                "(2,0)": "X",
                "(2,1)": "\u2014",
                "(2,2)": "\u2014",
            }
        return self.assertEqual("Continue", _check_is_win(board))
    
    def test_ai_defends_from_losing_position(self):
        """
            Test next move correct: Defends from losing postion
        """
        a = TicTacToe(3)

        board = {
                "(0,0)": "\u2014",
                "(0,1)": "\u2014",
                "(0,2)": "X",
                "(1,0)": "\u2014",
                "(1,1)": "X",
                "(1,2)": "\u2014",
                "(2,0)": "\u2014",
                "(2,1)": "\u2014",
                "(2,2)": "O",
            }

        a.board = board

        goal = {
                "(0,0)": "\u2014",
                "(0,1)": "\u2014",
                "(0,2)": "X",
                "(1,0)": "\u2014",
                "(1,1)": "X",
                "(1,2)": "\u2014",
                "(2,0)": "O",
                "(2,1)": "\u2014",
                "(2,2)": "O",
            }

        next_move = a.get_best_next(board, "O", "Hard")

        return self.assertEqual(next_move, goal)

    def test_ai_draws_from_losing_position(self):
        """
            Test next move correct: Gets draw from losing postion
        """
        a = TicTacToe(3)

        board = {
                "(0,0)": "\u2014",
                "(0,1)": "\u2014",
                "(0,2)": "X",
                "(1,0)": "\u2014",
                "(1,1)": "X",
                "(1,2)": "\u2014",
                "(2,0)": "O",
                "(2,1)": "\u2014",
                "(2,2)": "O",
            }

        a.board = board

        goal = {
                "(0,0)": "\u2014",
                "(0,1)": "\u2014",
                "(0,2)": "X",
                "(1,0)": "\u2014",
                "(1,1)": "X",
                "(1,2)": "\u2014",
                "(2,0)": "O",
                "(2,1)": "X",
                "(2,2)": "O",
            }

        next_move = a.get_best_next(board, "X", "Hard")

        return self.assertEqual(next_move, goal)


#run tests
if __name__ == "__main__":
    unittest.main()