import pygame as pg
from pygame.sprite import *
from constants import *


class Card(Sprite):

    def __init__(self, img):
        super(Card, self).__init__()
        self.image = pg.transform.smoothscale(pg.image.load(img), CARD_DIM)
        self.img_rect = self.image.get_rect(center=CARD_INIT_POS)
        self.name = str(img)
        self.clicked = False

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


class MyCards(OrderedUpdates):

    def __init__(self):
        super(MyCards, self).__init__()

    def get_card(self, card):
        for i in iter(self):
            i.shift_left()
        self.add(card)

    def discard_card(self, card):
        for i in iter(self):
            if i != card:
                i.shift_right()
            else:
                self.remove(card)
                break

    # this is for selecting card by clicking, using MOUSEBUTTONUP event
    def select_card(self, pos):
        for i in xrange(len(self)):
            if self[i].collide_point(pos) and (i == len(self)-1 or not self[i+1].collide_point(pos)):
                self[i].shift_down() if self[i].clicked else self[i].shift_up()
            elif (not self[i].collide_point(pos) or self[i+1].collide_point(pos)) and self[i].clicked:
                self[i].shift_down()

    # this is for selecting card by pointing at it, using MOUSEMOTION event
    def select_card_2(self, pos):
        for i in xrange(len(self)):
            if self[i].collide_point(pos) and (i == len(self)-1 or not self[i+1].collide_point(pos)):
                self[i].shift_up() if not self[i].clicked else None
            elif (not self[i].collide_point(pos) or self[i+1].collide_point(pos)) and self[i].clicked:
                self[i].shift_down()

    def display_all_cards(self, surface):
        for i in iter(self):
            surface.blit(i.image, i.img_rect)

    def __getitem__(self, item):
        return self._spritelist[item]


class Character(Sprite):

    def __init__(self, img, hp):
        super(Character, self).__init__()
        self.image = pg.transform.smoothscale(pg.image.load(img), CARD_DIM)
        self.img_hp = pg.transform.smoothscale(pg.image.load(HP), HP_DIM)
        self.hp = hp

    def display_all(self, surface):
        surface.blit(self.image, CHAR_INIT_POS)
        for i in xrange(self.hp):
            surface.blit(self.img_hp, (850, 500+i*30))


