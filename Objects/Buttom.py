from Objects.GameObject import GameObject
from Objects.TextObject import TextObject
import pygame


class Button(GameObject):
    def __init__(self,
                 x,
                 y,
                 w,
                 h,
                 text,
                 on_click=lambda: None,
                 padding=0):
        super().__init__(x, y, w, h)
        self.state = 'normal'
        self.on_click = on_click
        self.back_color = (0, 0, 0)
        self.text = TextObject(x + padding,
                               y + padding, lambda: text,
                               (225, 222, 0),
                               24)

    def draw(self, surface):
        pygame.draw.rect(surface,
                         self.back_color,
                         self.bounds)
        self.text.draw(surface)

    def update(self):
        pass

    def click(self, eventtype, pos):
        if self.left < pos[0] < self.right and self.top < pos[1] < self.bottom:
            self.on_click()
