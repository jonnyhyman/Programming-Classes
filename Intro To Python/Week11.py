
'''

    PyGame

'''

# Lots of imports here!
import pygame
import sys
import time
import random
from pygame.locals import *

# How many frames per second? Higher the number, faster the game
FPS = 5

# We are using a thing called pygame to do all the inputs and outputs
pygame.init()  # "init" is shorthand for "initialize" or start up / get ready

fpsClock=pygame.time.Clock()  # create a clock object to count time

# define the screen size
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480

# tell pygame what the screen should be like
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

# tell pygame we want a "surface" to draw pixels on
surface = pygame.Surface(screen.get_size())

# who knows what this does...?
surface = surface.convert()

# fill the surface with white (255,255,255) in the red,green,blue scale
surface.fill((255,255,255))

# create another clock for other reasons
clock = pygame.time.Clock()

# if you press a key, it will be repeated 40 times
pygame.key.set_repeat(1, 40)

# these variables IN ALL CAPS define IMPORTANT stuff for the game
GRIDSIZE=10 # how big is each pixel?
GRID_WIDTH = SCREEN_WIDTH / GRIDSIZE    # how many horizontal grid squares?
GRID_HEIGHT = SCREEN_HEIGHT / GRIDSIZE  # how many vertical grid squares?
UP    = (0, -1)  # which way is UP?  (x,y)
DOWN  = (0, 1)  # which way is DOWN?  (x,y)
LEFT  = (-1, 0) # ... you get the idea
RIGHT = (1, 0)

# puts the "surface" into the window at the position (0,0) (top left corner)
screen.blit(surface, (0,0))

def draw_box(surf, color, pos):
    r = pygame.Rect((pos[0], pos[1]), (GRIDSIZE, GRIDSIZE))
    pygame.draw.rect(surf, color, r)

class Snake(object):
    def __init__(self):
        self.lose()
        self.color = (0,0,0)

    def get_head_position(self):
        return self.positions[0]

    def lose(self):
        self.length = 1
        self.positions =  [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

    def point(self, pt):
        if self.length > 1 and (pt[0] * -1, pt[1] * -1) == self.direction:
            return
        else:
            self.direction = pt

    def move(self):
        cur = self.positions[0]
        x, y = self.direction
        new = (((cur[0]+(x*GRIDSIZE)) % SCREEN_WIDTH), (cur[1]+(y*GRIDSIZE)) % SCREEN_HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.lose()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def draw(self, surf):
        for p in self.positions:
            draw_box(surf, self.color, p)

class Apple(object):
    def __init__(self):
        self.position = (0,0)
        self.color = (255,0,0)
        self.randomize()

    def randomize(self):
        self.position = (random.randint(0, GRID_WIDTH-1) * GRIDSIZE, random.randint(0, GRID_HEIGHT-1) * GRIDSIZE)

    def draw(self, surf):
        draw_box(surf, self.color, self.position)

def check_eat(snake, apple):
    if snake.get_head_position() == apple.position:
        snake.length += 1
        apple.randomize()

if __name__ == '__main__':
    snake = Snake()
    apple = Apple()
    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    snake.point(UP)
                elif event.key == K_DOWN:
                    snake.point(DOWN)
                elif event.key == K_LEFT:
                    snake.point(LEFT)
                elif event.key == K_RIGHT:
                    snake.point(RIGHT)


        surface.fill((255,255,255))
        snake.move()
        check_eat(snake, apple)
        snake.draw(surface)
        apple.draw(surface)
        font = pygame.font.Font(None, 36)
        text = font.render(str(snake.length), 1, (10, 10, 10))
        textpos = text.get_rect()
        textpos.centerx = 20
        surface.blit(text, textpos)
        screen.blit(surface, (0,0))

        pygame.display.flip()
        pygame.display.update()
        fpsClock.tick(FPS + snake.length/3)
