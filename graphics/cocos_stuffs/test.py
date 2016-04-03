import cocos.euclid as eu
from hud import *
from cocos import actions, sprite, scene, text, collision_model as cm
from cocos.director import director


class MouseDisplay(Layer):

    is_event_handler = True

    def __init__(self):
        super(MouseDisplay, self).__init__()
        self.pos_x = 100
        self.pos_y = 200
        self.text = text.Label('No mouse events yet', font_size=18, x=self.pos_x, y=self.pos_y)
        self.add(self.text)

    def update_text(self, x, y):
        txt = 'Mouse at %d, %d' % (x, y)
        self.text.element.text = txt
        self.text.element.x = self.pos_x
        self.text.element.y = self.pos_y

    def on_mouse_motion(self, x, y, dx, dy):
        self.update_text(x, y)



class Actor(sprite.Sprite):
    def __init__(self, img, x, y):
        super(Actor, self).__init__(img, position=(x, y))
        self._cshape = cm.AARectShape(self.position, self.width/2, self.height/2)

    @property
    def get_cshape(self):
        self._cshape.center = eu.Vector2(self.x, self.y)
        return self._cshape


director.init(width=792, height=462)

bg_layer = BackgroundLayer('poker_font.jpg')
player_layer = Layer()

card = sprite.Sprite('bang.png', scale=0.5, position=(396, 60))

player_layer.add(card)

main_scene = scene.Scene(bg_layer, player_layer, MouseDisplay())

director.run(main_scene)

