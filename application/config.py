import pygame
import logging
import application.components.bezal as bezal
import application.components.dial as dial
import application.components.pointer as pointer
import application.connectors.broadcast as broadcast

class Config:

    logging.basicConfig(level=logging.DEBUG)

    listener = broadcast.Broadcast()

    controls = [
         pointer.Pointer( pos=(150,150) , listener=listener ),
         dial.Dial(       pos=(150,150) , listener=listener) 
    ]

    def __init__(self):
        self.window = self.Window()
   
    class Window:  
       height = 400 
       width  = 640
       title = "Horizontal Situation Indicatior"
       background = pygame.Color(255, 255, 255)
   

 

