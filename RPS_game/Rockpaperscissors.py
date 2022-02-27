import pygame

pygame.init()
WIDTH, HEIGHT= 900,500
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Rock Paper Scissors")
london_bg=pygame.image.load("London-sunset.png")

def main():
    run =True
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
        #screen.blit(london_bg,(WIDTH,HEIGHT))
        WIN.fill(WHITE)
        pygame.display.update()
        
    pygame.quit()
    
    if __name__=="__main__":
        main()