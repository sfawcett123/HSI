import pygame
import os
import logging
import application.components.component as component

class Pointer( component.Component ):

    def __init__(self, listener=None, pos=(0, 0) , size=(500, 500)):
        super(Pointer, self).__init__( listener=listener , pos=pos , size=size , image_file='HeadingIndicator_Aircraft.bmp' )

    def update(self):
        self.angle = self.listener.data.get('heading') 
        super().update()
