import pygame

pygame.init()

WIDTH, HEIGHT= 900,500
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Rock Paper Scissors")

#Asset import
bg_img=pygame.image.load('Rps_game/Assets/London-sunset-.png')
bg_img=pygame.transform.scale(bg_img,(WIDTH,HEIGHT))
rock_img=pygame.transform.scale(pygame.image.load('RPS_game/Assets/Rock.png'),(100,100))
paper_img=pygame.transform.scale(pygame.image.load('RPS_game/Assets/Paper.png'),(100,100))
scissors_img=pygame.transform.scale(pygame.image.load('RPS_game/Assets/scissors.png'),(100,100))




#############################    BUTTON CLASS        ##################
class Button():
    def __init__(self,x,y,image):
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
    
    def draw(self):
        WIN.blit(self.image,(self.rect.x,self.rect.y))

################################ END BUTTON CLASS ################################

#Button initialization
rock=Button(150,200,rock_img)
paper=Button(400,200,paper_img)
scissors=Button(650,200,scissors_img)

FPS=60
def game():
    #rock=pygame.Rect(150,200,100,100)
    #paper=pygame.Rect(400,200,100,100)
    #scissors=pygame.Rect(650,200,100,100)
    
    
    
    clock=pygame.time.Clock()
    gameRunning = True
    while gameRunning:
        clock.tick(FPS)
        bg_update()
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                print("QUIT")
                gameRunning = False

    
    pygame.quit()
    quit()


#Drawing thigns onto screen
def bg_update():
    WIN.blit(bg_img,(0,0))
    #WIN.blit(rock_img,(150,200))
    #WIN.blit(paper_img,(400,200))
    #WIN.blit(scissors_img,(650,200))
    rock.draw()
    paper.draw()
    scissors.draw()
    pygame.display.update()   
            
        

        
    
    
game()