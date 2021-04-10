import pygame
pygame.init()
width=height=700
win=pygame.display.set_mode((width,height))
pygame.display.set_caption('BALL GAME')
run=True
x=y=100
radius=50
vel=1
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    key=pygame.key.get_pressed()
    if key[pygame.K_w] and y>radius:
        y-=vel
    if key[pygame.K_s] and y<height-radius:
        y+=vel
    if key[pygame.K_a] and x>radius:
        x-=vel
    if key[pygame.K_d] and x<width-radius:
        x+=vel
    win.fill((0,0,0),rect=None)
    pygame.draw.circle(win,(150,0,0),(x,y),radius)
    pygame.display.update()
pygame.quit()