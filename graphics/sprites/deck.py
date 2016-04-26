import pygame as pg

class Deck(pg.sprite.OrderedUpdates):

    def __init__(self):
        super(Deck, self).__init__()

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
    def on_click(self, pos):
        for i in xrange(len(self)):
            if self[i].collide_point(pos) and (i == len(self)-1 or not self[i+1].collide_point(pos)):
                self[i].shift_down() if self[i].clicked else self[i].shift_up()
            elif (not self[i].collide_point(pos) or self[i+1].collide_point(pos)) and self[i].clicked:
                self[i].shift_down()

    # this is for selecting card by pointing at it, using MOUSEMOTION event
    def on_hover(self, pos):
        for i in xrange(len(self)):
            if self[i].collide_point(pos) and (i == len(self)-1 or not self[i+1].collide_point(pos)):
                self[i].shift_up() if not self[i].clicked else None
                return self[i]
            elif (not self[i].collide_point(pos) or self[i+1].collide_point(pos)) and self[i].clicked:
                self[i].shift_down()
    def display_all_cards(self, surface):
        for i in iter(self):
            surface.blit(i.image, i.img_rect)

    def __getitem__(self, item):
        return self._spritelist[item]
