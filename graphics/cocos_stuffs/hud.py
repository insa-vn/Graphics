from cocos.layer import *

import pyglet
from pyglet.gl import *


class BackgroundLayer(Layer):

    def __init__(self, img):
        super(BackgroundLayer, self).__init__()
        self.bg_img = pyglet.resource.image(img)

    def draw(self):
        glPushMatrix()
        self.transform()
        self.bg_img.blit(0, 0)
        glPopMatrix()

