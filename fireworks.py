import math
import random
import pygame

from pygame.locals import *
pygame.init()

# Overview
# Simulator
#   run
#   addObject
#   removeObject
#   simulateTime
#   updateScreen
#   mapWorldToPixel
#
# Projectile
#   simulateTime
#   getPixelLocation
#
# Firework
#   simulateTime
#   explode
#   draw
#
# Particle
#  simulateTime
#  draw

class Simulator(object):

    def __init__(self):
        self.physicsObjects = []
        self.screen = pygame.display.set_mode((800,600))

        self.clock = pygame.time.Clock()
        self.gravity = -9.8 # m/s

    def run(self):
        while self.physicsObjects:
            dt = self.clock.tick(60)/1000.0 # dt is measured in seconds.
            self.simulateTime(dt)
            self.updateScreen()


    def addObject(self, obj):
        print("Add", obj)
        self.physicsObjects.append(obj)

    def removeObject(self, obj):
        print("Remove", obj)
        self.physicsObjects.remove(obj)

    def simulateTime(self, dt):
        for obj in self.physicsObjects:
            obj.simulateTime(dt)

    def updateScreen(self):
        self.screen.fill((0,0,0))
        for obj in self.physicsObjects:
            obj.draw(self.screen)
        pygame.display.flip()

    def mapWorldToPixel(self, x, y):
        # Given a point in the universe, where is that on the screen
        # The area of the simulator we want to look at is say x=-300 to 300
        # and y = 0 to 600.

        # Y pixels are 0 at top and 800 at bottom. so 600-worldY = pixel's y
        py = 600-y

        # X pixels are left to right but start at 0. So 400 + worldY = pixels y
        # (when world x = -400, we want px=0. when worldx = 400 we want px=800)
        px = 400+x
        return (px, py)

# We need an environment to hold all our physics stuff
# and run the simulation.
universe = Simulator()


class Projectile(object):
    def __init__(self, x=0, y=0, dx=0, dy=0):
        self.x=x
        self.y=y
        self.dx=dx
        self.dy=dy

    def simulateTime(self, dt):
        self.x += self.dx * dt
        self.y += self.dy * dt
        self.dy += universe.gravity * dt

    def getPixelLocation(self):
        px, py = universe.mapWorldToPixel(self.x, self.y)
        # Convert it to ints, because pixel locations are integers
        return (int(px), int(py))

class Firework(Projectile):
    def __init__(self, x=0, angle=math.pi/2, velocity=70):
        super(Firework, self).__init__(
            x = x,
            y = 0,
            dx = math.cos(angle) * velocity,
            dy = math.sin(angle) * velocity)

    def simulateTime(self, dt):
        super(Firework, self).simulateTime(dt)
        if self.dy < 0: # We have started heading back down
            self.explode()

    def explode(self):
        for i in range(50):
            universe.addObject(Particle(self))
        universe.removeObject(self)

    def draw(self, surface):
        pygame.draw.circle(surface, (255,0,0), self.getPixelLocation(), 4)


class Particle(Projectile):
    # Create a particle that comes shoots out from where the firework is.
    def __init__(self, firework):
        velocity = 15 + random.random() * 10
        direction = random.random() * math.pi * 2
        super(Particle, self).__init__(
                x=firework.x,
                y=firework.y,
                dx=math.cos(direction) * velocity,
                dy=math.sin(direction) * velocity)

    def simulateTime(self, dt):
        super(Particle, self).simulateTime(dt)
        if self.y < 0: # particles die when they touch the ground
            universe.removeObject(self)

    def draw(self, surface):
        pygame.draw.circle(surface, (255,255,0), self.getPixelLocation(), 2)


universe.addObject(Firework())
universe.run()