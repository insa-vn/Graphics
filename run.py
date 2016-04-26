import sys
import pygame as pg
import os
from pygame.locals import *  # import all constants (not good practice)
from graphics.sprites.card import Card
from graphics.sprites.deck import Deck
from graphics.sprites.character import Character
from graphics.constants import (SCREEN_SIZE, BACKGROUND, ORIGIN, LEFT_MOUSE)
from graphics.sprites.card_overview import CardOverview

__CURDIR__ = os.path.dirname(os.path.realpath(__file__)) + '/'
__GRAPHICSDIR__ = __CURDIR__ + '/graphics/'
def initialize():
    global window
    pg.init()
    window = pg.display.set_mode(SCREEN_SIZE)


def get_background():
    bg_img = pg.image.load(__GRAPHICSDIR__ + BACKGROUND).convert()
    bg_img = pg.transform.smoothscale(bg_img, SCREEN_SIZE)
    return bg_img

def set_background():
    window.blit(bg_img, ORIGIN)


if __name__ == '__main__':

    initialize()
    bg_img = get_background()

    my_deck = Deck()

    card1 = Card(__GRAPHICSDIR__ + 'img/bang.png')
    card2 = Card(__GRAPHICSDIR__ + 'img/beer.png')
    card3 = Card(__GRAPHICSDIR__ + 'img/gatling.png')
    card4 = Card(__GRAPHICSDIR__ + 'img/missed.png')
    card5 = Card(__GRAPHICSDIR__ + 'img/Trang.png')

    overview_card = CardOverview(__GRAPHICSDIR__ + 'img/card_highlight.png')

    my_deck.get_card(card1)
    my_deck.get_card(card2)
    my_deck.get_card(card3)
    my_deck.get_card(card4)
    my_deck.get_card(card5)

    char1 = Character(__GRAPHICSDIR__ + 'img/molly_stark.png', 4)

    while True:
        set_background()
        char1.display_all(window)
        my_deck.display_all_cards(window)
        overview_card.reset_img(window)
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONUP and event.button == LEFT_MOUSE:
                my_deck.on_click(event.pos)
            elif event.type == MOUSEMOTION:
                target_card = my_deck.on_hover(event.pos)
                if target_card is not None:
                    overview_card.update_img(
                        target_card.get_image_path(), window)
                else:
                    if char1.is_hover(event.pos):
                        overview_card.update_img(
                            __GRAPHICSDIR__ + 'img/molly_stark.png', window)

        pg.display.flip()
