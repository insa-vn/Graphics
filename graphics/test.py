import sys
import pygame as pg
import os
from pygame.locals import *  # import all constants (not good practice)
from bang_sprites import (Card, MyCards, Character)
from constants import (SCREEN_SIZE, BACKGROUND, ORIGIN, LEFT_MOUSE)
from sprites.card_overview import CardOverview

__CURDIR__ = os.path.dirname(os.path.realpath(__file__)) + '/'

def initialize():
    global window
    pg.init()
    window = pg.display.set_mode(SCREEN_SIZE)


def get_background():
    bg_img = pg.image.load(__CURDIR__ + BACKGROUND).convert()
    bg_img = pg.transform.smoothscale(bg_img, SCREEN_SIZE)
    return bg_img

def set_background():
    window.blit(bg_img, ORIGIN)


if __name__ == '__main__':

    initialize()
    bg_img = get_background()

    my_cards = MyCards()

    card1 = Card(__CURDIR__ + 'img/bang.png')
    card2 = Card(__CURDIR__ + 'img/beer.png')
    card3 = Card(__CURDIR__ + 'img/gatling.png')
    card4 = Card(__CURDIR__ + 'img/missed.png')
    card5 = Card(__CURDIR__ + 'img/Trang.png')

    overview_card = CardOverview(__CURDIR__ + 'img/card_highlight.png')

    my_cards.get_card(card1)
    my_cards.get_card(card2)
    my_cards.get_card(card3)
    my_cards.get_card(card4)
    my_cards.get_card(card5)

    char1 = Character(__CURDIR__ + 'img/molly_stark.png', 4)

    while True:
        set_background()
        char1.display_all(window)
        my_cards.display_all_cards(window)
        overview_card.reset_img(window)
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONUP and event.button == LEFT_MOUSE:
                my_cards.on_click(event.pos)
            elif event.type == MOUSEMOTION:
                target_card = my_cards.on_hover(event.pos)
                if target_card is not None:
                    overview_card.update_img(
                        target_card.get_image_path(), window)
                else:
                    if char1.is_hover(event.pos):
                        overview_card.update_img(
                            __CURDIR__ + 'img/molly_stark.png', window)

        pg.display.flip()
