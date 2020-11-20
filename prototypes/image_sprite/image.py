import sys
import sdl2, sdl2.ext , sdl2.sdlgfx
import random
from sdl2 import *

RESOURCES = sdl2.ext.Resources(__file__, "resources")

class Velocity(object):
    def __init__(self):
        super(Velocity, self).__init__()
        self.vx = 0
        self.vy = 0

class Ball(sdl2.ext.Entity):
    def __init__(self, world, sprite, posx=0, posy=0):
        self.sprite = sprite
        self.sprite.position = posx, posy
        self.velocity = Velocity()

class CollisionSystem(sdl2.ext.Applicator):
    def __init__(self, minx, miny, maxx, maxy):
        super(CollisionSystem, self).__init__()
        self.componenttypes = Velocity, sdl2.ext.Sprite
        self.ball = None
        self.minx = minx
        self.miny = miny
        self.maxx = maxx
        self.maxy = maxy

    def _overlap(self, item):
        pos, sprite = item
        if sprite == self.ball.sprite:
            return False

        left, top, right, bottom = sprite.area
        bleft, btop, bright, bbottom = self.ball.sprite.area 

        return (bleft < right and bright > left and
                btop < bottom and bbottom > top )

    def process(self, world, componentsets):
       collitems = [comp for comp in componentsets if self._overlap(comp)]
       if collitems:
          sprite = collitems[0][1]
          ballcentery = self.ball.sprite.y + self.ball.sprite.size[1] // 2
          halfheight = sprite.size[1] // 2
          stepsize = halfheight // 10
          degrees = random.uniform(0, 1)
          collided_with = sprite.y + halfheight

          if ballcentery < collided_with:
              factor = (collided_with - ballcentery) // stepsize
              self.ball.velocity.vy = -int(round(factor * degrees))
              self.ball.velocity.vx = -int(round(factor * degrees))
          elif ballcentery > collided_with:
              factor = (ballcentery - collided_with) // stepsize
              self.ball.velocity.vy = int(round(factor * degrees))
              self.ball.velocity.vx = int(round(factor * degrees))

       if self.ball.sprite.y <= self.miny :
              self.ball.velocity.vy = - self.ball.velocity.vy

       if self.ball.sprite.y + self.ball.sprite.size[1] >= self.maxy:
              self.ball.velocity.vy = - self.ball.velocity.vy

       if self.ball.sprite.x <= self.minx :
              self.ball.velocity.vx = - self.ball.velocity.vx

       if self.ball.sprite.x + self.ball.sprite.size[0] >= self.maxx:
              self.ball.velocity.vx = - self.ball.velocity.vx


class MovementSystem(sdl2.ext.Applicator):
    def __init__(self, minx, miny, maxx, maxy):
        super(MovementSystem, self).__init__()
        self.componenttypes = Velocity, sdl2.ext.Sprite
        self.minx = minx
        self.miny = miny
        self.maxx = maxx
        self.maxy = maxy

    def process(self, world, componentsets):
        for velocity, sprite in componentsets:
            swidth, sheight = sprite.size
            sprite.x += velocity.vx
            sprite.y += velocity.vy

            sprite.x = max(self.minx, sprite.x)
            sprite.y = max(self.miny, sprite.y)

            pmaxx = sprite.x + swidth
            pmaxy = sprite.y + sheight
            if pmaxx > self.maxx:
                sprite.x = self.maxx - swidth
            if pmaxy > self.maxy:
                sprite.y = self.maxy - sheight

class SoftwareRenderer(sdl2.ext.SoftwareSpriteRenderSystem):
    def __init__(self, window):
        super(SoftwareRenderer, self).__init__(window)

    def render(self, components):
        sdl2.ext.fill(self.surface, sdl2.ext.Color(0, 77, 0))
        super(SoftwareRenderer, self).render(components)

def run():
    sdl2.ext.init()
    window = sdl2.ext.Window("Image Sprites", size=(800, 600))

    window.show()
    world = sdl2.ext.World()

    spriterenderer = SoftwareRenderer(window)
    world.add_system(spriterenderer)

    movement = MovementSystem(0, 0, 800, 600)
    world.add_system(movement)


    factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)
    tmp = sdl2.ext.load_image(RESOURCES.get_path("RED_BALL.png"))
    t1 = sdlgfx.zoomSurface(tmp, .06, .06, sdlgfx.SMOOTHING_ON)

    collision = []
    for number in range(3):
         sp_ball = factory.from_surface( t1.contents )
         ball  = Ball(world, sp_ball, 800, 300)
         collision.append(  CollisionSystem(0, 0, 800, 600))
         world.add_system(collision[number])
         ball.velocity.vx = 5 * ( number + 1) 
         ball.velocity.vy = 5 * number 
         collision[number].ball = ball

    running = True
    while running:
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                running = False
                break
        sdl2.SDL_Delay(20) 
        world.process()

if __name__ == "__main__":
    sys.exit(run())
