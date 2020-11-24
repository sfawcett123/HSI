import pygame
import os


class Component(pygame.sprite.Sprite):

    RESOURCES = os.path.join( os.path.dirname( __file__ ) , 'resources' )

    def __init__(self, image_file="" , listener=None , angle=360 ,  pos=(0, 0) , size=(500, 500)):
        super(Component, self).__init__()
        self.image_file = pygame.image.load( os.path.join( self.RESOURCES, image_file))
        self.image = None
        self._pos = pos
        self._angle  = angle 
        self._listener = listener
        self._surface = None

    def blitRotateCenter(self, surf, image , angle):
        self.image = pygame.transform.rotate(image, angle)
        self._rect = self.image.get_rect(center = image.get_rect( center = self._pos ).center)
        surf.blit(self.image, self._rect.topleft)

    def update(self , scale=1 ):
        if self._listener is not None:
            self._listener.receive() 

        transColor = self.image_file.get_at((0,0))
        self.image_file.set_colorkey(transColor)

        if self._surface is not None:
             self.blitRotateCenter(self._surface, self.image_file ,  self._angle) 

    @property
    def pos(self):
        return self._pos

    @property
    def surface(self):
        return self._surface

    @property
    def listener(self):
        return self._listener

    @property
    def angle(self):
        return self._angle

    @pos.setter
    def pos( self , value ):
        self._pos = value

    @surface.setter
    def surface( self , value ):
        self._surface = value

    @angle.setter
    def listener(self, value):
        self._listener = value

    @angle.setter
    def angle(self, value):
        self._angle = value

        if self._angle < 0 : self._angle = 360
        if self._angle > 360 : self._angle = 1
