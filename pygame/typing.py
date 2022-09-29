import pygame as pg 
running=True
pg.init()
W,H=640,480
screen=pg.display.set_mode((W,H))
bg=pg.Surface(screen.get_size())
bg=bg.convert()
bg.fill((255,255,243))

screen.blit(bg,(0,0))
pg.display.update()


class Cube:
     def __init__(self):
          self.image=pg.Surface((50,50))
          self.image.fill((0,0,0))

print("slef.image.fill the last integer is the first integer")

while running:
      for event in pg.event.get():
           if event.type==pg.QUIT:
                running=False
pg.quit