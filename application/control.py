import pygame
import application.config as CONFIG
from pygame.locals import *

class Control:
    def __init__(self):
        self.config = CONFIG.Config()
        self._running = True
        self._display_surf = None
        self._debug = True

    def on_init(self):
        pygame.init()
        infoObject = pygame.display.Info()
        size = self.config.window.width , self.config.window.height
        self._display_surf = pygame.display.set_mode( size , pygame.HWSURFACE | pygame.DOUBLEBUF)
        for item in self.config.controls:
             item.surface = self._display_surf 

        pygame.display.set_caption( self.config.window.title )
        self._display_surf.fill( self.config.window.background )
        pygame.display.flip()
        self._running = True
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        self._display_surf.fill( self.config.window.background )
        for item in self.config.controls:
            item.update()
        pygame.display.flip()

    def on_render(self):
        self.clock.tick(100)

    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        self.clock=pygame.time.Clock()

        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
