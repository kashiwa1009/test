import pygame 
#it is the pygame test
pygame.init()

width,heigth=640,480

screen=pygame.display.set_mode((width,heigth))
pygame.display.set_caption("game")

running=True

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
             running=False


print("aaa")
pygame.quit
