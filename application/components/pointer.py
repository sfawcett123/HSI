import pygame
import os
import application.components.component as component

class Pointer( component.Component ):

    def __init__(self, pos=(0, 0) , size=(500, 500)):
        super(Pointer, self).__init__( pos=pos , size=size , image_file='pointer.png' )

    def update(self):
        self.angle -= 1
        super(Pointer, self).update( scale=.1 )
