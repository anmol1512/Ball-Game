import pygame
pygame.init()
width=height=700
win=pygame.display.set_mode((width,height))
pygame.display.set_caption('BALL GAME')
run=True
x=y=100
radius=50
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    pygame.draw.circle(win,(150,0,0),(x,y),50)
    pygame.display.update()
pygame.quit()