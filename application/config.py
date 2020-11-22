import pygame
import application.components.dial as dial
import application.components.pointer as pointer

class Config:

    controls = [
         dial.Dial( pos=(200, 200)) ,
         pointer.Pointer( pos=(200, 200))
    ]

    def __init__(self):
        self.window = self.Window()

   
    class Window:  
       height = 400 
       width  = 640
       title = "Horizontal Situation Indicatior"
       background = pygame.Color(255, 255, 255)
   

 

