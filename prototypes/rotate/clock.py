import pygame

class Dial(pygame.sprite.Sprite):

    def __init__(self, pos=(0, 0), size=(500, 500)):
        super(Dial, self).__init__()
        self.original_image = pygame.image.load('resources/dial.jpg').convert()
        self.original_image = pygame.transform.rotozoom(self.original_image, 0, .3)
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.angle = 0

class Pointer(pygame.sprite.Sprite):

    def __init__(self, pos=(0, 0), size=(500, 500)):
        super(Pointer, self).__init__()
        self.original_image = pygame.image.load('resources/POINTER.png').convert()
        self.original_image = pygame.transform.rotozoom(self.original_image, 0, .1) 
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.angle = 0

    def update(self):
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.angle -= 1 
        if self.angle < 0 :
            self.angle = 360
        x, y = self.rect.center  # Save its current center.
        self.rect = self.image.get_rect()  # Replace old rect with new rect.
        self.rect.center = (x, y)  # Put the new rect's center at old center.


def main():
    clock=pygame.time.Clock()
    pointer = Pointer(pos=(200, 200))
    dial    = Dial(pos=(200, 200))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit

        pointer.update()

        screen.fill((255, 255, 255))
        screen.blit(dial.image, dial.rect)
        screen.blit(pointer.image, pointer.rect)
        pygame.display.update()
        clock.tick(20)

if __name__ == '__main__':
    pygame.init()
    infoObject = pygame.display.Info()
    screen = pygame.display.set_mode(( infoObject.current_w, infoObject.current_h ) ,  pygame.DOUBLEBUF | pygame.RESIZABLE)
    main()
