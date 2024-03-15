import pygame

from . import PyGame


class Drawer:
    def __init__(self, screen: pygame.surface, border: int, header: int, color: str):
        self.screen: pygame.surface = screen
        self.border = border
        self.header = header
        self.color = color

    @property
    def max_height(self):
        return self.screen.get_height() - self.border * 2 - self.header

    @property
    def max_width(self):
        return self.screen.get_width() - self.border * 2

    def candle_width(self, index, value, length):
        width = self.max_width / length
        return width if not int(index * width) < int((index + 1) * width) else width + 1

    def candle_height(self, index, value, length):
        return self.max_height / length * value

    def candle_x(self, index, value, length):
        return self.border + self.max_width / length * index

    def candle_y(self, index, value, length):
        candle_height = self.candle_height(index, value, length)
        return self.max_height - candle_height + self.header + self.border

    def draw_list(self, arr, candles: dict):
        for item in enumerate(arr):
            pygame.draw.rect(
                self.screen,
                color=candles[item[0]] if item[0] in candles.keys() else self.color,
                rect=[
                    self.candle_x(*item, len(arr)),
                    self.candle_y(*item, len(arr)),
                    self.candle_width(*item, len(arr)),
                    self.candle_height(*item, len(arr))
                ]
            )

    def draw_text(self, text1, text2=None):
        font = pygame.font.SysFont(None, 30)
        img = font.render(text1, True, self.color)
        self.screen.blit(img, (self.border, self.border))

        if text2 is not None:
            img = font.render(text2, True, self.color)
            self.screen.blit(img, (self.border, self.border + 20))



