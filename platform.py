from typing import Union, Tuple

from pygame.sprite import Sprite
from pygame.math import Vector2
import pygame as pg

from constants import PLATFORM_SIZE, PLATFORM_COLOUR

# TODO: Make collision detection with its sides be using small 3 wide/high rects
# -- with 2 px sticking out so the collision works properly
# -- (collision detection funcs dont detect the 1px borders around the rect afaik)
class Platform(Sprite):
    def __init__(self, pos:Tuple[Union[int, float], Union[int, float]]):
        super().__init__()
        self.rect = pg.Rect(pos, PLATFORM_SIZE)
        self.pos = Vector2(self.rect.center)
        self.image = pg.Surface(PLATFORM_SIZE)
        self.image.fill(PLATFORM_COLOUR)
        self.image.convert()

    def draw(self, canvas):
        canvas.blit(self.image, self.pos)
