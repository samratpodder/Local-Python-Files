import pygame
import os
import random
import time
import sys


# sys.setrecursionlimit(999999999)
WIDTH=800
HEIGHT=600
pygame.font.init()
pygame.init()
pygame.mixer.init()
BG_IMAGE_POSX = 0
GAME_LOOP = pygame.mixer.Sound(os.path.join('Assets','gameloop2.wav'))
GAME_LOOP.play()
pygame.mixer.pause()
CAR_CRASH = pygame.mixer.Sound(os.path.join('Assets','gameover.wav'))
screen = pygame.display.set_mode((WIDTH, HEIGHT))
GREEN = (0, 255, 0)
OBSTACLE_X=[120,300,200,150,350,250,400,450,460]
pygame.display.set_caption("Racing Game")
LEFT_ROAD=pygame.image.load(os.path.join('Assets','left.png'))
RIGHT_ROAD  = pygame.image.load(os.path.join('Assets','right.png'))
LEFT_ROAD = pygame.transform.scale(LEFT_ROAD,(150,600))
RIGHT_ROAD = pygame.transform.scale(RIGHT_ROAD,(150,600))
INTRO_BG = pygame.image.load(os.path.join('Assets','intro_bg.jpg'))
INTRO_BG_SM = pygame.transform.scale(INTRO_BG,(WIDTH,HEIGHT))
CAR_IMAGE = pygame.image.load(os.path.join('Assets', 'car.png'))
CAR_IMAGE_SM = pygame.transform.scale(CAR_IMAGE, (180, 140))
OBSTACLE_IM = pygame.image.load(os.path.join('Assets', 'obstacle.png'))
OBSTACLE_IM_SM = pygame.transform.scale(OBSTACLE_IM, (180, 140))
ROAD_IMAGE = pygame.image.load(os.path.join('Assets', 'road.jpg'))
ROAD_IMAGE_SM = pygame.transform.scale(ROAD_IMAGE, (200, 600))
FPS = 60
WHITE = (255,255,255)
CAR_HIT = pygame.USEREVENT+1
OFFSET = 200
VEL=3
OBSTACLE_VEL=random.choice([3,4,5])
RED=(255,0,0)
SCORE_FONT = pygame.font.SysFont('consolas',30)
MUSIC_ENDED = pygame.USEREVENT+2
pygame.mixer.music.set_endevent(MUSIC_ENDED)


car = pygame.Rect(200, 450, 180, 140)
obstacle1 = pygame.Rect(120,-200,100,100)
obstacle2 = pygame.Rect(300,-100,100,100)
obstacle3 = pygame.Rect(200,-100,100,100)
all_obstacles=[obstacle1,obstacle2,obstacle3]
obstacle = random.choice(all_obstacles)

# screen.blit(ROAD_IMAGE_SM, (150, 0))
# screen.blit(ROAD_IMAGE_SM, (320, 0))
# screen.blit(ROAD_IMAGE_SM, (480, 0))

def handle_obstacle(obstacle,car_y,SCORE):
    if obstacle.y-OFFSET>car_y:
        obstacle = random.choice(all_obstacles)
        obstacle.x = random.choice(OBSTACLE_X)
        obstacle.y = -100
        SCORE+=1
        # print(obstacle,SCORE)
        GAME_LOOP.play()
        global OBSTACLE_VEL
        OBSTACLE_VEL = random.choice([3,4,5,6,7,8])
        return (obstacle,SCORE)
    else:
        return (obstacle,SCORE)

def handle_car_movement(keys_pressed, obs,car):
    obs.y+=OBSTACLE_VEL
    # car.y+=1
    if car.colliderect(obs):
        pygame.event.post(pygame.event.Event(CAR_HIT))
        # print("hit")
    else:
        if keys_pressed[pygame.K_w] and obs.y>HEIGHT//2:
            car.y-=VEL
        if keys_pressed[pygame.K_a] and car.x>120:
            car.x-=VEL
        if keys_pressed[pygame.K_s] and car.y<HEIGHT:
            car.y+=VEL/VEL
        if keys_pressed[pygame.K_d] :
            car.x+=VEL
        # print(car.x,car.y)

def drawobs(car):
    # screen.fill(GREEN)
    # screen.blit(ROAD_IMAGE_SM, (150, 0))
    # screen.blit(ROAD_IMAGE_SM, (320, 0))
    # screen.blit(ROAD_IMAGE_SM, (480, 0))
    screen.blit(OBSTACLE_IM_SM, (car.x, car.y))


def drawenv():
    screen.fill(GREEN)
    screen.blit(LEFT_ROAD,(0,0))
    screen.blit(RIGHT_ROAD,(680,0))
    if BG_IMAGE_POSX < HEIGHT:
        screen.blit(ROAD_IMAGE_SM, (150, BG_IMAGE_POSX-HEIGHT))
        screen.blit(ROAD_IMAGE_SM, (320, BG_IMAGE_POSX-HEIGHT))
        screen.blit(ROAD_IMAGE_SM, (480, BG_IMAGE_POSX-HEIGHT))
    screen.blit(ROAD_IMAGE_SM, (150, BG_IMAGE_POSX))
    screen.blit(ROAD_IMAGE_SM, (320, BG_IMAGE_POSX))
    screen.blit(ROAD_IMAGE_SM, (480, BG_IMAGE_POSX))

def draw(car):
    # screen.fill(GREEN)
    # screen.blit(ROAD_IMAGE_SM, (150, 0))
    # screen.blit(ROAD_IMAGE_SM, (320, 0))
    # screen.blit(ROAD_IMAGE_SM, (480, 0))
    screen.blit(CAR_IMAGE_SM, (car.x, car.y))
    # pygame.display.update()

def initial():
    obstacle1 = pygame.Rect(0,-200,350, 230)
    obstacle2 = pygame.Rect(300,-100,350, 230)
    obstacle3 = pygame.Rect(200,-100,350, 230)


def game_intro():
    for j in range(5):
        screen.blit(INTRO_BG_SM,(0,0))
        start_text = SCORE_FONT.render('Car Dodge Racing',1,GREEN)
        screen.blit(start_text,(200,500))
        start_text = SCORE_FONT.render('Loading....'+str(5-j),1,GREEN)
        screen.blit(start_text,(225,550))
        pygame.display.update()
        time.sleep(0.5)
        for i in range(1):
            i+=1
            pygame.display.update()
            time.sleep(0.5)
            
    main()

        
def main():
    initial()
    clock = pygame.time.Clock()
    letsplay = True
    car = pygame.Rect(200, 450, 100, 100)
    obstacle1 = pygame.Rect(120,-200,100,100)
    obstacle2 = pygame.Rect(300,-100,100,100)
    obstacle3 = pygame.Rect(200,-100,100,100)
    all_obstacles=[obstacle1,obstacle2,obstacle3]
    obstacle = random.choice(all_obstacles)
    SCORE=0
    pygame.mixer.unpause()
    while letsplay:
        # if obstacle.y>car.y:
            # print(car.x,car.y)
        print(OBSTACLE_VEL,car.x,car.y,obstacle.x,obstacle.y)
        if car.x>500:
            car.x=500
        if car.y<HEIGHT//2:
            car.y=HEIGHT//2
        clock.tick(FPS)
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                letsplay = False
                pygame.quit()
        
        # keys_pressed = pygame.key.get_pressed()
        # handle_car_movement(keys_pressed,obstacle,car)
        # obstacle,SCORE = handle_obstacle(obstacle,car.y,SCORE)
        # print(obstacle)
        global BG_IMAGE_POSX
        BG_IMAGE_POSX+=1
        BG_IMAGE_POSX=BG_IMAGE_POSX % HEIGHT
        # if BG_IMAGE_POSX < HEIGHT:
        #     screen.blit(ROAD_IMAGE_SM, (150, BG_IMAGE_POSX-HEIGHT))
        #     screen.blit(ROAD_IMAGE_SM, (320, BG_IMAGE_POSX-HEIGHT))
        #     screen.blit(ROAD_IMAGE_SM, (480, BG_IMAGE_POSX-HEIGHT))
        drawenv()
        draw(obstacle)
        draw(car)
        keys_pressed = pygame.key.get_pressed()
        handle_car_movement(keys_pressed,obstacle,car)
        obstacle,SCORE = handle_obstacle(obstacle,car.y,SCORE)
        score_text = SCORE_FONT.render("Score: "+str(SCORE),1,WHITE)
        screen.blit(score_text,(0,0))
        pygame.display.update()


        for event in pygame.event.get():
            if event.type == MUSIC_ENDED:
                GAME_LOOP.play()
            if(event.type == CAR_HIT):
                crash()
                time.sleep(3)
                respawn()
                game_intro()
                main()

def respawn():
    
    for i in range(3):
        screen.fill((50,50,50))
        text = SCORE_FONT.render("Respawning in ......."+str(3-i),1,RED)
        screen.blit(text,(150,300))
        pygame.display.update()
        time.sleep(1)


def crash():
    screen.fill((50,50,50))
    crash_text = SCORE_FONT.render("CRASHED",1,RED)
    pygame.mixer.pause()
    CAR_CRASH.play()
    screen.blit(crash_text,(300,300))
    pygame.display.update()

if __name__ == '__main__':
    game_intro()
    main()
