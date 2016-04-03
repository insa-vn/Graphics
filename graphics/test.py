import sys
from pygame.locals import *  # import all constants
from bang_sprites import *


def initialize():
    global window
    pg.init()
    window = pg.display.set_mode(SCREEN_SIZE)


def get_background():
    global bg_img
    bg_img = pg.image.load(BACKGROUND).convert()
    bg_img = pg.transform.smoothscale(bg_img, SCREEN_SIZE)


def set_background():
    window.blit(bg_img, ORIGIN)


if __name__ == '__main__':

    initialize()
    get_background()

    my_cards = MyCards()

    card1 = Card('img/bang.png')
    card2 = Card('img/beer.png')
    card3 = Card('img/gatling.png')
    card4 = Card('img/missed.png')
    card5 = Card('img/Trang.png')

    my_cards.get_card(card1)
    my_cards.get_card(card2)
    my_cards.get_card(card3)
    my_cards.get_card(card4)
    my_cards.get_card(card5)

    char1 = Character('img/molly_stark.png', 4)

    while True:
        set_background()
        char1.display_all(window)
        my_cards.display_all_cards(window)
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            # elif event.type == MOUSEBUTTONUP and event.button == LEFT_MOUSE:
            elif event.type == MOUSEMOTION:
                my_cards.select_card_2(event.pos)

        pg.display.flip()
