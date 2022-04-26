import math
import copy


class Board:

    def __init__(self):
        self.board = [" "] * 9
        self.row_length = int(math.sqrt(len(self.board)))

    def move_is_legal(self, move):
        return self.check_move_in_board(move) and self.board[move] == " "

    def place_move(self, move, mark):
        self.board[move] = mark

    def check_win(self, marks):
        win = False
        # check for all marks if there is a 3 in a row in a diagnol, row, or column
        for mark in marks:
            win = self.winDiagnol(mark) or self.win_row(mark) or self.win_column(mark)
            if win:
                return win
                print(mark, "diagnol", self.winDiagnol(mark))
                print(mark, "row", self.winRow(mark))
                print(mark, "column", self.winColumn(mark))
            '''
            if win:
                print(str(self.winDiagnol(mark)) + " " + str(self.winRow(mark)) + " " + str(
                    self.winColumn(mark)))
                print("Player " + mark + " is the winner!")
            '''
        return win

    def check_move_in_board(self, move):
        try:
            move = int(move)
            if not (-1 < move < 10):
                raise ValueError
        except:
            return False
        return True

    '''
      -   -   - 
    | 0 | 1 | 2 |
      -   -   -
    | 3 | 4 | 5 |
      -   -   -
    | 6 | 7 | 8 |
      -   -   -
    '''
    '''
    Ensure board is squared 
    '''

    def winDiagnol(self, mark):
        diagnol_Left = True
        diagnol_Right = True
        for i in range(0, self.row_length):
            if self.board[i + i * self.row_length] != mark:
                diagnol_Left = False
            if self.board[len(self.board) - 1 - (self.row_length - 1) * (i + 1)] != mark:
                diagnol_Right = False
        return diagnol_Right or diagnol_Left

    def win_row(self, mark):
        for i in range(0, self.row_length):
            win = True
            for j in range(0, self.row_length):
                if self.board[j + i * self.row_length] != mark:
                    win = False
                    break
            if win:
                return win
        return win

    def win_column(self, mark):
        for i in range(0, self.row_length):
            win = True
            for j in range(0, self.row_length):
                if self.board[i + j * self.row_length] != mark:
                    win = False
                    break
            if win:
                return win
        return win

    def board_full(self):
        # if not (" " in self.board):
        #     print("Board is full")
        return not (" " in self.board)

    def get_board(self):
        return self.board

    def get_possible_moves(self):
        moves = []
        for i in range(len(self.board)):
            if self.board[i] == " ":
                moves.append(i)
        return moves

    def create_board(self):
        self.board = [" "] * 9

    def board_to_string(self):
        field = self.get_board()
        print("\n---------------------------")
        for i in range(len(field)):
            if i % 3 == 0:
                print(" ")
            print("|" + field[i] + "|", end='')

    def deep_copy(self):
        return copy.deepcopy(self)