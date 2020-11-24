import pygame
import os
import application.components.component as component

class Dial( component.Component ):

    def __init__(self, listener=None, pos=(0, 0) , size=(500, 500)):
        super(Dial, self).__init__( listener=listener , pos=pos , size=size , image_file='HeadingWheel.bmp'  )
