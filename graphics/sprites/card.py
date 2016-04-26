import pygame as pg
from graphics.constants import (
    CARD_DIM, CARD_INIT_POS, LEFT_SHIFT, RIGHT_SHIFT, DOWN_SHIFT, UP_SHIFT
)

class Card(pg.sprite.Sprite):

    def __init__(self, img):
        super(Card, self).__init__()
        self.image_path = img
        self.image = pg.transform.smoothscale(pg.image.load(img), CARD_DIM)
        self.img_rect = self.image.get_rect(center=CARD_INIT_POS)
        self.name = str(img)
        self.clicked = False

    def get_image_path(self):
        return self.image_path

    def shift_left(self):
        self.img_rect.move_ip(LEFT_SHIFT)

    def shift_right(self):
        self.img_rect.move_ip(RIGHT_SHIFT)

    def shift_up(self):
        self.img_rect.move_ip(UP_SHIFT)
        self.clicked = True

    def shift_down(self):
        self.img_rect.move_ip(DOWN_SHIFT)
        self.clicked = False

    def collide_point(self, pos):
        return self.img_rect.collidepoint(pos)
