import pygame

from utils import Board


class Game:
    def __init__(self):
        pygame.init()

        #  Initialising all variables for later use

        self.WIDTH = 640  # Width of the screen
        self.HEIGHT = 640  # Height of the screen

        self.display = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        pygame.display.set_caption("Chess")

        self.run_app = True  # Boolean responsible for running the whole app

        self.ESC = False

    def run_game(self):

        self.board = Board()

        while self.run_app:

            self.board.draw_board(self.display)
            self.window.blit(self.display, (0, 0))
            pygame.display.update()
            self.check_event()

    def draw_text(self, text: str, size: int, x: int, y: int):
        self.font = pygame.font.SysFont("Arial", size)
        text_surface = self.font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)

    def draw_image(self, image, x, y):
        image_rect = image.get_rect()
        image_rect.move_ip(x, y)
        self.display.blit(image, image_rect)

    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.close_app()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.close_app()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.board.click(pygame.mouse.get_pos())

    def close_app(self):
        self.run_app = False


def main():
    game = Game()
    game.run_game()


if __name__ == "__main__":
    main()
