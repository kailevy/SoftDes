""" A Collaboratively-Coded Clone of Flappy Bird """

import pygame
import random
import time

class DrawableSurface():
    """ A class that wraps a pygame.Surface and a pygame.Rect """
    def __init__(self, surface, rect):
        """ Initialize the drawable surface """
        self.surface = surface
        self.rect = rect

    def get_surface(self):
        """ Get the surface """
        return self.surface

    def get_rect(self):
        """ Get the rect """
        return self.rect

class Background():
    """Represents the background or something"""
    def __init__(self,width,height):
        self.image = pygame.image.load('images/plant_tile.png')
        self.height = height
        self.width = width

    def get_drawables(self):
        w,h = self.image.get_size()
        drawables = []
        for i in range(100):
            drawables.append(DrawableSurface(self.image,
                pygame.Rect(0 + w * i,self.height - 
                    h,w,h)))   
        return drawables

class Player():
    """Visually represent the character"""
    def __init__(self,x_pos,y_pos):
        self.image = pygame.image.load('images/olin_o.png')
        self.image.set_colorkey((255,255,255))
        self.x = x_pos
        self.y = y_pos
        self.vel_y = 0

    def update(self):
        self.x += .1
        self.y += self.vel_y
        self.vel_y += .01

    def flap(self):
        self.vel_y -= .1

    def get_drawables(self):
        w,h = self.image.get_size()
        return [DrawableSurface(self.image,
            pygame.Rect(self.x,self.y,w,h))]

class FlappyModel():
    """ Represents the game state of our Flappy bird clone """
    def __init__(self, width, height):
        """ Initialize the flappy model """
        self.width = width
        self.height = height
        self.background = Background(width,height)
        self.player = Player(0,200)

    def get_drawables(self):
        """ Return a list of DrawableSurfaces for the model """
        return self.background.get_drawables() + self.player.get_drawables()

    def update(self):
        """ Updates the model and its constituent parts """
        self.player.update()

class FlappyView():
    def __init__(self, model, width, height):
        """ Initialize the view for Flappy Bird.  The input model
            is necessary to find the position of relevant objects
            to draw. """
        pygame.init()
        # to retrieve width and height use screen.get_size()
        self.screen = pygame.display.set_mode((width, height))
        # this is used for figuring out where to draw stuff
        self.model = model

    def draw(self):
        """ Redraw the full game window """
        self.screen.fill((0,51,102))
        # get the new drawables
        self.drawables = self.model.get_drawables()
        for d in self.drawables:
            rect = d.get_rect()
            surf = d.get_surface()
            self.screen.blit(surf, rect)
        pygame.display.update()


class FlappyBirdController():
    def __init__(self, model):
        self.model = model
        self.space_pressed = False

    def process_events(self):
        """ process keyboard events.  This must be called periodically
            in order for the controller to have any effect on the game """
        pygame.event.pump()
        if not(pygame.key.get_pressed()[pygame.K_SPACE]):
            self.space_pressed = False
        elif not(self.space_pressed):
            self.space_pressed = True
            self.model.player.flap()

class FlappyBird():
    """ The main Flappy Bird class """

    def __init__(self):
        """ Initialize the flappy bird game.  Use FlappyBird.run to
            start the game """
        self.model = FlappyModel(640, 480)
        self.view = FlappyView(self.model, 640, 480)
        self.controller = FlappyBirdController(self.model)

    def run(self):
        """ the main runloop... loop until death """
        last_update_time = time.time()
        while True:
            self.view.draw()
            self.model.update()
            self.controller.process_events()
            last_update_time = time.time()

if __name__ == '__main__':
    flappy = FlappyBird()
    flappy.run()