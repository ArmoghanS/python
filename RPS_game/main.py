import pygame
import os


WIDTH, HEIGHT= 900,500
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Rock Paper Scissors")


def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if running == False:
                pygame.quit()
    
            
        
        WIN.fill(0,0,0)
        pygame.display.update()
        
    pygame.quit()
    
    if __name__=="__main__":
        main()