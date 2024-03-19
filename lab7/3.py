import pygame
pygame.init()

width = height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('Circle')

x = y = 25
v = 20
radius = 25
color = (255, 0, 0)
doo = 1
clock = pygame.time.Clock()

while doo:
    win.fill((255, 255, 255))
    for event in pygame.event.get():
                if event.type == pygame.QUIT: doo = 0

    keys = pygame.key.get_pressed()
    if(keys[pygame.K_LEFT] and x-radius>=v): x-=v 
    if(keys[pygame.K_RIGHT] and x+radius+v <= width): x+=v 
    if(keys[pygame.K_UP] and y>=v+radius): y-=v 
    if(keys[pygame.K_DOWN] and y+radius+v <= height): y+=v 

    pygame.draw.circle(win, color, (x, y), radius)

    pygame.display.flip()
    clock.tick(60)