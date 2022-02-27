import pygame

pygame.init()

WIDTH, HEIGHT= 900,500
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Rock Paper Scissors")


def main():
    gameRunning = True
    while gameRunning:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                print("QUIT")
                pygame.quit()
                gameRunning = False
                quit()
    
            
        
        WIN.fill((0,0,0))
        pygame.display.update()
        
    
    
    if __name__=="__main__":
        main()