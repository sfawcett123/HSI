import pygame
import os
import application.components.component as component

class Dial( component.Component ):

    def __init__(self, pos=(0, 0) , size=(500, 500)):
        super(Dial, self).__init__( pos=pos , size=size , image_file='dial.jpg' )

