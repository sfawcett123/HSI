import pygame
import os


class Component(pygame.sprite.Sprite):

    RESOURCES = os.path.join( os.path.dirname( __file__ ) , 'resources' )

    def __init__(self, image_file="" , listener=None , angle=360 ,  pos=(0, 0) , size=(500, 500)):
        super(Component, self).__init__()
        self.image_file = pygame.image.load( os.path.join( self.RESOURCES, image_file)) 
        self.original_image = None 
        self.pos = pos
        self._angle  = angle 
        self._listener = listener

    def update(self , scale=.3 ):
        if self._listener is not None:
            self._listener.receive() 

        if self.original_image is None :
            self.original_image = self.image_file.convert()
            self.original_image = pygame.transform.rotozoom(self.image_file, 0, scale )
            self.image = self.original_image
            self.rect = self.original_image.get_rect()
            self.rect.center = self.pos

    @property
    def listener(self):
        return self._listener

    @property
    def angle(self):
        return self._angle

    @angle.setter
    def listener(self, value):
        self._listener = value

    @angle.setter
    def angle(self, value):
        self._angle = value

        if self._angle < 0 : self._angle = 360
        if self._angle > 360 : self._angle = 1

        if self.original_image is not None:
            self.image = pygame.transform.rotate(self.original_image, self._angle)
            x, y = self.rect.center  
            self.rect = self.image.get_rect()  
            self.rect.center = (x, y)  
