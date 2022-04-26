import random
from tictactoe.board import Board


class TicTacToe:
    def __init__(self, player1, player2):
        self.board = Board()
        self.players = [player1, player2]
        self.current_player = random.randrange(0, len(self.players))
        print("Player", self.players[self.current_player].get_mark(), "starts")

    def do_move(self):
        if not self.check_someone_won():
            move = self.players[self.current_player].do_move(self.board)
            if self.check_legal(move) and not self.board_full():
                self.board.place_move(move, self.players[self.current_player].get_mark())
                self.change_player()

    def check_someone_won(self):
        for player in self.players:
            if self.board.check_win(player.get_mark()):
                return True
        return False

    def check_legal(self, move):
        return self.board.move_is_legal(move)

    def check_win(self):
        marks = []
        for player in self.players:
            marks.append(player.getMark())
        win = self.board.check_win(marks)
        if win:
            self.update_table(self.board)
        return win

    def change_player(self):
        self.current_player = (self.current_player + 1) % len(self.players)

    def board_full(self):
        return self.board.board_full()

    def reset(self):
        self.board = Board()

    def get_board(self):
        return self.board.get_board()

    def row_length(self):
        return self.board.row_length

    def get_current_player(self):
        return self.current_player

    def game_ended(self):
        return self.check_win() or self.board_full()