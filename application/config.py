import pygame
import application.components.dial as dial
import application.components.pointer as pointer
import application.connectors.broadcast as broadcast

class Config:

    listener = broadcast.Broadcast()

    controls = [
         dial.Dial( pos=(200, 200)       , listener=listener) ,
         pointer.Pointer( pos=(200, 200) , listener=listener)
    ]


    def __init__(self):
        self.window = self.Window()
   
    class Window:  
       height = 400 
       width  = 640
       title = "Horizontal Situation Indicatior"
       background = pygame.Color(255, 255, 255)
   

 

