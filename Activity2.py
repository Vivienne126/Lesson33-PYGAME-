import pygame
pygame.init()
window= pygame.display.set_mode((400,300))
window.fill((255,255,255))
BLUE=(0,0,255)
pygame.draw.circle(window,BLUE,(300,300) , 50)
pygame.draw.circle(window,BLUE,(100,100) , 50 , 3)
pygame.display.update()
done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True 
pygame.quit()