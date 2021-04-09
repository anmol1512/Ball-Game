import pygame
pygame.init()
width=height=700
win=pygame.display.set_mode((width,height))
pygame.display.set_caption('BALL GAME')
run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
pygame.quit()