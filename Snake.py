
import pygame 

pygame.init()

# Game Constants 
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
HEIGHT = 800
WIDTH = 800

# Game Variables 
score = 0
player_x = 50 
player_y = 580
y_change = 0
x_change = 0
obs = [400,400]
obs_speed = 1
active = False

screen = pygame.display.set_mode([HEIGHT,WIDTH])
pygame.display.set_caption('SNAKE')
background = blue 
fps = 60
font = pygame.font.Font('freesansbold.ttf', 16)
timer = pygame.time.Clock()

running = True

while running: 
    timer.tick(fps)
    screen.fill(background)
    pygame.display.flip() 
pygame.quit()
