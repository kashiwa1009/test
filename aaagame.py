import pygame 
#it is the pygame test

WIDTH,HEIGHT=640,480

screen=pygame.display.set_mode((WIDTH,HEIGHT))
#set mode () <- 元祖

pygame.display.set_caption("game")
#SPRI

running=True
FPS=60
COLOR=(255,250,240)
#不會再去更動的用全大寫

pygame.init()
while running:
    clock.tick(FPS)
    #一秒鐘之內最多只能被執行60次
    #clock物件底下的函式tick  


    for event in pygame.event.get():
    #回傳現在發生的所有事件<-列表 

        
        if event.type==pygame.QUIT:
         #檢查事件如果是quit就跳出迴圈
             running=False
        
        
        screen.fill((COLOR))
         #RGB 0-255
         #screen的fill函式
        pygame.display.update()
        #畫面做更新
        clock=pygame.time.clock()
         #不同電腦運作速度不同 一秒跑while的速度

      

        
     
     


             
             
         
         
         

print("aaa")
pygame.quit
