import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, pos=(0, 0), size=(500, 500)):
        super(Player, self).__init__()
        self.original_image = pygame.image.load('resources/POINTER.png').convert()
        self.original_image = pygame.transform.rotozoom(self.original_image, 0, .1) 
        pygame.draw.line(self.original_image, (255, 0, 255), (size[0] / 2, 0), (size[0] / 2, size[1]), 3)
        pygame.draw.line(self.original_image, (0, 255, 255), (size[1], 0), (0, size[1]), 3)
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
    player = Player(pos=(200, 200))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit

        player.update()
        screen.fill((255, 255, 255))
        screen.blit(player.image, player.rect)
        pygame.display.update()
        pygame.time.wait(100)

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    main()
