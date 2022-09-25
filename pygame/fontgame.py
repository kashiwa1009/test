
import pygame



running=True
pygame.init()
screen=pygame.display.set_mode((640,480))

#print(pygame.font.get_fonts()) 可以使用此方法來獲得系統當前所有可用字型

font=pygame.font.SysFont("",40)
text_surface=font.render("Hello",True,(0,0,233))

x=0
y=(480-text_surface.get_height())/2


while running:
    for event in pygame.event.get():
         if event.type==pygame.QUIT:
             running=False
         
    screen.fill((233,232,232))    
    # x-=0.05
    # if x<-text_surface.get_width():
    #      x=640-text_surface.get_width()

    screen.blit(text_surface,(x,y))

    pygame.display.update()

pygame.quit