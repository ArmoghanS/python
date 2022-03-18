import random
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
start_img=pygame.transform.scale(pygame.image.load('RPS_game/Assets/start.png'),(120,80))
exit_img=pygame.transform.scale(pygame.image.load('RPS_game/Assets/exit.png'),(120,80))



#############################    BUTTON CLASS        ##################
class Button():
    def __init__(self,x,y,image):
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
        self.clicked=False
    
    def draw(self):
        action=False
        pos = pygame.mouse.get_pos()
        
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == True and self.clicked==False:
                self.clicked=True
                action=True
                
            if pygame.mouse.get_pressed()[0]==False:
                self.clicked=False
        
        WIN.blit(self.image,(self.rect.x,self.rect.y))
        return action

################################ END BUTTON CLASS ################################

#Button initialization
rock=Button(150,200,rock_img)
paper=Button(400,200,paper_img)
scissors=Button(650,200,scissors_img)
start_btn=Button(450,400,start_img)
exit_btn=Button(700,20,exit_img)


#Variables
FPS=60
player=""
computer=random.choice(['r','p','s'])



def game():   
    
    
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
    global player
    WIN.blit(bg_img,(0,0)) #Draws Background
    if rock.draw():
        print("You've Chosen Rock")
        player='r'
    if paper.draw():
        print("You've Chosen Paper")
        player='p'
    if scissors.draw():
        print("You've Chosen Scissors")
        player='s'
    if exit_btn.draw():
        pygame.quit()
        quit()
    if start_btn.draw():
        if play(player,computer):
            print("You've won")
            
        if play(player,computer)==False:
            print("You Lose")
            
    pygame.display.update()   
            
def play(player,opponent):
    
    if (player== 'r' and opponent=='s') or(player=='s' and opponent=='p') or (player=='p'and opponent=='r'):
        return True        
    if player==opponent:
        print("Tie")
        pygame.quit()
        quit()
    if (opponent== 'r' and player=='s') or(opponent=='s' and player=='p') or (opponent=='p'and player=='r'):
        return False

        
     
    
game()