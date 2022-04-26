import copy
from tictactoe.player import Player
import sys

sys.setrecursionlimit(10000000)


class MinMaxPlayer(Player):
    def __init__(self, name, mark):
        Player.__init__(self, name, mark)
        self.board_dictionary = {}
        self.max_depth = 9

    def do_move(self, board):
        return self.calculate_next_move(board, self.mark)

    def calculate_next_move(self, current_board, mark):

        # for every possible move, add a pair of a min_max score and the move to a list scores.
        score_move_pairs = []
        for next_move in current_board.get_possible_moves():
            next_score = self.min_max(current_board, next_move, self.mark, 0)
            score_move_pairs.append((next_score, next_move))
        # if there is no score/move pair, return 0

        if not score_move_pairs:

            return 0
        # otherwise
        else:
            # compute the max score/move
            highest_score, best_move = max(score_move_pairs)
            # return the move
            return best_move

    def heuristics_row(self, next_board, mark):
        #  calculate a value for the heuristic value of the row
        score = 0
        for row in range(3):
            for column in range(3):
                if next_board.board[column + 3 * row] == mark:
                    score += 1
                elif next_board.board[column + 3 * row] == self.other_mark(mark):
                    score -= 2
        return self.heuristic_score(score)

    def heuristics_column(self, next_board, mark):
        #  calculate a value for the heuristic value of the  column
        score = 0
        for column in range(3):
            for row in range(3):
                if next_board.board[column + 3 * row] == mark:
                    score += 1
                elif next_board.board[column + 3 * row] == self.other_mark(mark):
                    score -= 2
        return self.heuristic_score(score)

    def heuristics_diagonal(self, next_board, mark):
        #  calculate a value for the heuristic value of the diagonal
        score = 0
        stop = 0
        while stop < 2:
            add = 2
            for j in range(2):
                for i in range(3):
                    if next_board.board[4 * i + add * j] == mark:
                        score += 1
                    elif next_board.board[4 * i + add * j] == self.other_mark(mark):
                        score -= 2
                    add -= 2
            stop += 1
        return self.heuristic_score(score)

    def heuristic_score(self, score):
        #  calculate the heuristic formula
        total = 0
        if score == 2:
            total += 3
        elif score == -4:
            total += -3
        elif score == 1:
            total += 1
        elif score == -1:
            total -= 1
        return total

    def min_max(self, current_board, move, mark, depth):
        depth += 1
        list_score = []
        next_board = copy.deepcopy(current_board)
        next_board.place_move(move, mark)
        # if tuple(next_board.board) in self.board_dictionary:  # check if board has already been calculated
        #     return self.board_dictionary.get(tuple(next_board.board))
        if depth >= self.max_depth:  # get the heuristics value of the board
            heuristic_score = 0
            heuristic_score += self.heuristics_column(next_board, mark)
            heuristic_score += self.heuristics_diagonal(next_board, mark)
            heuristic_score += self.heuristics_row(next_board, mark)
            self.board_dictionary[tuple(next_board.board)] = heuristic_score
            return heuristic_score
        else:
            if next_board.check_win(mark):  # check if this board is a win
                self.board_dictionary[tuple(next_board.board)] = 10
                return 10
            elif next_board.board_full():  # check if this board is a draw/full
                self.board_dictionary[tuple(next_board.board)] = 0
                return 0
            else:
                moves = next_board.get_possible_moves()
                for move in moves:  # Run minimax for all possible moves
                    score_rand = self.max_min(next_board, move, self.other_mark(mark), depth)
                    list_score.append((score_rand, move))
                score, best_move = min(list_score)
            return score

    def max_min(self, current_board, move, mark, depth):
        depth += 1
        list_score = []
        next_board = copy.deepcopy(current_board)
        next_board.place_move(move, mark)
        # if tuple(next_board.board) in self.board_dictionary:  # check if board has already been calculated
        #     return self.board_dictionary.get(tuple(next_board.board))
        if depth >= self.max_depth:  # get the heuristics value of the board
            heuristic_score = 0
            heuristic_score += self.heuristics_column(next_board, mark)
            heuristic_score += self.heuristics_diagonal(next_board, mark)
            heuristic_score += self.heuristics_row(next_board, mark)
            self.board_dictionary[tuple(next_board.board)] = heuristic_score
            return heuristic_score
        else:
            if next_board.check_win(mark):  # check if this board is a lose
                self.board_dictionary[tuple(next_board.board)] = -10
                return -10
            elif next_board.board_full():  # check if this board is a draw/full
                self.board_dictionary[tuple(next_board.board)] = 0
                return 0
            else:
                moves = next_board.get_possible_moves()
                for move in moves:  # Run minimax for all possible moves
                    score_rand = self.min_max(next_board, move, self.other_mark(mark), depth)
                    list_score.append((score_rand, move))
                score, best_move = max(list_score)
            return score

    def other_mark(self, mark):
        if mark == "X":
            return "O"
        else:
            return "X"
