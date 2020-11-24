import pygame
import os
import application.components.component as component

class Bezal( component.Component ):

    def __init__(self, listener=None, pos=(0, 0) , size=(500, 500)):
        super(Bezal, self).__init__( listener=listener , pos=pos , size=size , image_file='HeadingIndicator_Background.bmp'  )
