import pygame
import os
import logging

class Component(pygame.sprite.Sprite):

    RESOURCES = os.path.join( os.path.dirname( __file__ ) , 'resources' )

    def __init__(self, image_file="" , listener=None , angle=360 ,  pos=(0, 0) , size=(500, 500)):
        super(Component, self).__init__()
        self.image_file = pygame.image.load( os.path.join( self.RESOURCES, image_file))
        self.image = None
        self._pos = pos
        self._required_angle  = angle 
        self._current_angle  = angle 
        self._listener = listener
        self._surface = None

    def blitRotateCenter(self, surf, image , angle):
        self.image = pygame.transform.rotate(image, angle)
        self._rect = self.image.get_rect(center = image.get_rect( center = self._pos ).center)
        surf.blit(self.image, self._rect.topleft)

    def rotation( self ,  current , required ):
        v=( current - required ) % 360
        if v == 0: return  0
        if v > 180: return  1
        return -1

    def update(self , scale=1 ):
        if self._listener is not None:
            self._listener.receive() 

        transColor = self.image_file.get_at((0,0))
        self.image_file.set_colorkey(transColor)

        if self._current_angle != self._required_angle:
           self._current_angle += self.rotation(self._current_angle , self._required_angle ) 

        if self._surface is not None:
             self.blitRotateCenter(self._surface, self.image_file ,  self._current_angle) 

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
        return self._required_angle

    @pos.setter
    def pos( self , value ):
        self._pos = value

    @surface.setter
    def surface( self , value ):
        self._surface = value

    @listener.setter
    def listener(self, value):
        logging.debug( "Listener set to {value}".format( value=value ) )
        self._listener = value

    @angle.setter
    def angle(self, value):
        if value is None:
            value = 0

        self._required_angle = 360 - value
        self._required_angle = self._required_angle % 360
