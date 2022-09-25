import pygame as pg

pg.init()
W,H=(640,480)
screen=pg.diplay.set_mode((W,H))
pg.display.set_caption("game")

bg=pg.Surface(screen.get_size())
bg=bg.convert()
bg.fill((255,255,255))

screen.blit(bg,(0,0))
pg.display.update()

running=True

while running:
     for event in pg.event.get():
         if event.type==pg.QUIT:
             running=False
pg.quit()