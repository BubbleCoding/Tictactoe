import pygame
import sys
from tictactoe.helpers.constants import Constants
from tictactoe.helpers.keyboard_handler import KeyboardHandler
from tictactoe.tic_tac_toe import TicTacToe
from tictactoe.game_view import GameView
from tictactoe.player import Player
from tictactoe.human_player import HumanPlayer
from tictactoe.min_max_player import MinMaxPlayer


class Game:
    """
    Initialize PyGame and create a graphical surface to write. Similar
    to void setup() in Processing
    """
    def __init__(self):
        # init Pygame
        pygame.init()
        self.size = (Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT)
        self.screen = pygame.display.set_mode(self.size)
        self.keyboard_handler = KeyboardHandler()
        self.font = pygame.font.SysFont(pygame.font.get_fonts()[0], 64)
        self.time = pygame.time.get_ticks()

        # init TicTacToe
        self.player1 = HumanPlayer("Player1", "X")# Field.X)
        self.player2 = MinMaxPlayer("Player2", "O")#Field.O)
        self.game = TicTacToe(self.player1, self.player2)
        self.game_view = GameView(self.game, self.screen, self.font)

    """
    Method 'game_loop' will be executed every frame to drive
    the display and handling of events in the background. 
    In Processing this is done behind the screen. Don't 
    change this, unless you know what you are doing.
    """
    def game_loop(self):
        current_time = pygame.time.get_ticks()
        delta_time = current_time - self.time
        self.time = current_time
        self.handle_events()
        self.update_game(delta_time)
        self.draw_components()

    """
    Method 'update_game' is there to update the state of variables 
    and objects from frame to frame.
    """
    def update_game(self, dt):
        self.game.do_move()
        #pass

    """
    Method 'draw_components' is similar is meant to contain 
    everything that draws one frame. It is similar to method
    void draw() in Processing. Put all draw calls here. Leave all
    updates in method 'update'
    """
    def draw_components(self):
        self.screen.fill([255, 255, 255])
        self.game_view.draw_game()
        pygame.display.flip()

    def draw_score(self):
        text = self.font.render(str(self.score[0]) + ":" + str(self.score[1]), True, (255,255,255))
        self.screen.blit(text, (self.size[0]/2-64, 20))

    def reset(self):
        pass

    """
    Method 'handle_event' loop over all the event types and 
    handles them accordingly. 
    In Processing this is done behind the screen. Don't 
    change this, unless you know what you are doing.
    """
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self.handle_key_down(event)
            if event.type == pygame.KEYUP:
                self.handle_key_up(event)
            if event.type == pygame.MOUSEMOTION:
                self.handle_mouse_motion(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_mouse_pressed(event)
            if event.type == pygame.MOUSEBUTTONUP:
                self.handle_mouse_released(event)

    """
    This method will store a currently pressed buttons 
    in list 'keyboard_handler.pressed'.
    """
    def handle_key_down(self, event):
        self.keyboard_handler.key_pressed(event.key)

    """
    This method will remove a released button 
    from list 'keyboard_handler.pressed'.
    """
    def handle_key_up(self, event):
        self.keyboard_handler.key_released(event.key)

    """
    Similar to void mouseMoved() in Processing
    """
    def handle_mouse_motion(self, event):
        pass

    """
    Similar to void mousePressed() in Processing
    """
    def handle_mouse_pressed(self, event):
        self.game_view.on_mouse_clicked(pygame.mouse.get_pos())

    """
    Similar to void mouseReleased() in Processing
    """
    def handle_mouse_released(self, event):
        pass


if __name__ == "__main__":
    game = Game()
    while True:
        game.game_loop()