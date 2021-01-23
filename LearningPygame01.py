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
GAME_LOOP = pygame.mixer.Sound(os.path.join('Assets','gameloop2.wav'))
GAME_LOOP.play()
pygame.mixer.pause()
CAR_CRASH = pygame.mixer.Sound(os.path.join('Assets','gameover.wav'))
screen = pygame.display.set_mode((WIDTH, HEIGHT))
GREEN = (0, 255, 0)
OBSTACLE_X=[0,300,200]
pygame.display.set_caption("Racing Game")
LEFT_ROAD=pygame.image.load(os.path.join('Assets','left.png'))
RIGHT_ROAD  = pygame.image.load(os.path.join('Assets','right.png'))
LEFT_ROAD = pygame.transform.scale(LEFT_ROAD,(150,600))
RIGHT_ROAD = pygame.transform.scale(RIGHT_ROAD,(150,600))
INTRO_BG = pygame.image.load(os.path.join('Assets','intro_bg.jpg'))
INTRO_BG_SM = pygame.transform.scale(INTRO_BG,(WIDTH,HEIGHT))
CAR_IMAGE = pygame.image.load(os.path.join('Assets', 'car.png'))
CAR_IMAGE_SM = pygame.transform.scale(CAR_IMAGE, (400, 200))
ROAD_IMAGE = pygame.image.load(os.path.join('Assets', 'road.jpg'))
ROAD_IMAGE_SM = pygame.transform.scale(ROAD_IMAGE, (200, 600))
FPS = 60
WHITE = (255,255,255)
CAR_HIT = pygame.USEREVENT+1
OFFSET = 200
VEL=3
RED=(255,0,0)
SCORE_FONT = pygame.font.SysFont('consolas',36)
MUSIC_ENDED = pygame.USEREVENT+2
pygame.mixer.music.set_endevent(MUSIC_ENDED)


car = pygame.Rect(200, 450, 100, 100)
obstacle1 = pygame.Rect(0,-200,100,100)
obstacle2 = pygame.Rect(300,-100,100,100)
obstacle3 = pygame.Rect(200,-100,100,100)
all_obstacles=[obstacle1,obstacle2,obstacle3]
obstacle = random.choice(all_obstacles)

# screen.blit(ROAD_IMAGE_SM, (150, 0))
# screen.blit(ROAD_IMAGE_SM, (320, 0))
# screen.blit(ROAD_IMAGE_SM, (480, 0))

def handle_obstacle(keys_pressed,obstacle,car,SCORE):
    if obstacle.y-OFFSET>car.y:
        obstacle = random.choice(all_obstacles)
        obstacle.x = random.choice(OBSTACLE_X)
        obstacle.y = -100
        SCORE+=1
        # print(obstacle,SCORE)
        GAME_LOOP.play()
        return (obstacle,SCORE)
    else:
        return (obstacle,SCORE)

def handle_car_movement(keys_pressed, car,obs):
    if car.colliderect(obs):
        pygame.event.post(pygame.event.Event(CAR_HIT))
        # print("hit")
    else:
        # print(obs.x,obs.y,car.x,car.y,HEIGHT,WIDTH)
        if keys_pressed[pygame.K_a] and car.x <400:
            car.x += VEL
        if keys_pressed[pygame.K_w] and car.y <WIDTH:
            car.y += VEL
        if keys_pressed[pygame.K_w] and obs.y>HEIGHT//2:
            obs.y-=VEL/VEL
        if keys_pressed[pygame.K_s]:
            car.y -= VEL/VEL
        if keys_pressed[pygame.K_s] and obs.y<HEIGHT:
            obs.y+=VEL/VEL
        if keys_pressed[pygame.K_d] and car.x>0:
            car.x -= VEL
        # print(car.x,car.y)

def drawobs(car):
    # screen.fill(GREEN)
    # screen.blit(ROAD_IMAGE_SM, (150, 0))
    # screen.blit(ROAD_IMAGE_SM, (320, 0))
    # screen.blit(ROAD_IMAGE_SM, (480, 0))
    screen.blit(CAR_IMAGE_SM, (car.x, car.y))


def drawenv():
    screen.fill(GREEN)
    screen.blit(LEFT_ROAD,(0,0))
    screen.blit(RIGHT_ROAD,(680,0))
    screen.blit(ROAD_IMAGE_SM, (150, 0))
    screen.blit(ROAD_IMAGE_SM, (320, 0))
    screen.blit(ROAD_IMAGE_SM, (480, 0))

def draw(car):
    # screen.fill(GREEN)
    # screen.blit(ROAD_IMAGE_SM, (150, 0))
    # screen.blit(ROAD_IMAGE_SM, (320, 0))
    # screen.blit(ROAD_IMAGE_SM, (480, 0))
    screen.blit(CAR_IMAGE_SM, (car.x, car.y))
    # pygame.display.update()

def initial():
    obstacle1 = pygame.Rect(0,-200,100,100)
    obstacle2 = pygame.Rect(300,-100,100,100)
    obstacle3 = pygame.Rect(200,-100,100,100)


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
    obstacle1 = pygame.Rect(0,-200,100,100)
    obstacle2 = pygame.Rect(300,-100,100,100)
    obstacle3 = pygame.Rect(200,-100,100,100)
    all_obstacles=[obstacle1,obstacle2,obstacle3]
    obstacle = random.choice(all_obstacles)
    SCORE=0
    pygame.mixer.unpause()
    while letsplay:
        clock.tick(FPS)
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                letsplay = False
                pygame.quit()
        

        keys_pressed = pygame.key.get_pressed()
        handle_car_movement(keys_pressed,obstacle,car)
        obstacle,SCORE = handle_obstacle(keys_pressed,obstacle,car,SCORE)
        # print(obstacle)
        drawenv()
        draw(obstacle)
        draw(car)
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
