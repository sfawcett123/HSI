import pygame
import os

RESOURCES = os.path.join( os.path.dirname( __file__ ) , 'resources' )

class Pointer(pygame.sprite.Sprite):

    def __init__(self, pos=(0, 0) , size=(500, 500)):
        super(Pointer, self).__init__()
        self.image_file = pygame.image.load( os.path.join( RESOURCES, 'pointer.png')) 
        self.original_image = None 
        self.angle = 0
        self.pos = pos

    def update(self):
        if self.original_image is None :
            self.original_image = self.image_file.convert()
            self.original_image = pygame.transform.rotozoom(self.image_file, 0, .1)
            self.rect = self.original_image.get_rect()
            self.rect.center = self.pos

        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.angle -= 1 
        if self.angle < 0 :
            self.angle = 360
        x, y = self.rect.center  # Save its current center.
        self.rect = self.image.get_rect()  # Replace old rect with new rect.
        self.rect.center = (x, y)  # Put the new rect's center at old center.
