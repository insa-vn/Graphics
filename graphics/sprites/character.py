import pygame as pg
from graphics.constants import (CARD_DIM, CHAR_INIT_POS, HP_DIM, HP)

import os

__CURDIR__ = os.path.dirname(os.path.realpath(__file__)) + '/../'

class Character(pg.sprite.Sprite):

    def __init__(self, img, hp):
        super(Character, self).__init__()
        self.image = pg.transform.smoothscale(pg.image.load(img), CARD_DIM)
        self.img_rect = self.image.get_rect(center=CHAR_INIT_POS)
        self.img_hp = pg.transform.smoothscale(pg.image.load(__CURDIR__ + HP), HP_DIM)
        self.hp = hp

    def display_all(self, surface):
        surface.blit(self.image, CHAR_INIT_POS)
        for i in xrange(self.hp):
            surface.blit(self.img_hp, (850, 500+i*30))

    def is_hover(self, pos):
        if self.img_rect.collidepoint(pos):
            return True
        else:
            return False
