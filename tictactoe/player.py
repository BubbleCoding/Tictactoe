import random as rnd


class Player:

    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def do_move(self, board):
        """
        int(input("Where do you want to place your move"))
        """
        rnd.seed()
        return int(rnd.random() * 9)

    def set_result(self):
        pass

    def get_name(self):
        return self.name

    def get_mark(self):
        return self.mark

    def set_mark(self, mark):
        self.mark = mark

    def set_move(self, move):
        pass
