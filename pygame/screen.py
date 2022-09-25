import pygame as pg 

pg.init()

W,H=640,480

WHITE=(255,255,255)

screen=pg.display.set_mode((W,H))
pg.display.set_caption("game")

# bg=pg.Surface(screen.get_size())
# bg=bg.convert()
# bg.fill((233,233,233))

# screen.blit(bg,(0,0))
# pg.display.update()

running=True

while running:
    for event in pg.event.get():
         if event.type==pg.QUIT:
            running=False
    screen.fill((WHITE))
    pg.display.update()

pg.quit()



