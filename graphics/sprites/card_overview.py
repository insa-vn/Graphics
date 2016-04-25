import pygame as pg

import os

__CURDIR__ = os.path.dirname(os.path.realpath(__file__)) + '/'

INIT_POST = (80, 580)
DIMENSIONS = (160, 210)
class CardOverview(pg.sprite.Sprite):

    def __init__(self, img):
        super(CardOverview, self).__init__()
        self.image = pg.transform.smoothscale(pg.image.load(img), DIMENSIONS)
        self.img_rect = self.image.get_rect(center=INIT_POST)
        self.name = str(img)
        self.new_image_path = img

    def update_img(self, img, surface):
        if img == self.new_image_path:
            return
        self.image_path = img
        self.image = pg.transform.smoothscale(pg.image.load(img), DIMENSIONS)
        self.img_rect = self.image.get_rect(center=INIT_POST)
        # surface.blit(self.new_image, self.new_img_rect)

    def reset_img(self, surface):
        surface.blit(self.image, self.img_rect)
