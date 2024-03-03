import random
import pygame
import os
from pygame.constants import QUIT, K_s, K_w, K_d, K_a

pygame.init()

FPS = pygame.time.Clock()

HEIGHT = 800
WIDTH = 1200

COLOR_WHITE = (255,255,255)
COLOR_BLACK = (0,0,0)
COLOR_BLUE = (0,0,255)
COLOR_PURPLE = (204,0,204)
FONT = pygame.font.SysFont('arial', 20)

main_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Goose')

bg = pygame.transform.scale(pygame.image.load("background.png"), (WIDTH, HEIGHT))
bg_X1 = 0
bg_X2 = bg.get_width()
bg_move = 3

IMAGE_PATH = 'Goose'
PLAYER_IMAGES = os.listdir(IMAGE_PATH)

spawnpoint = (0,350)

PLAYER_SIZE = (20,20)
player = pygame.Surface(PLAYER_SIZE)
player = pygame.image.load('player.png').convert_alpha()   #player.fill(COLOR_WHITE)
#player_speed = [1,1]
player_rect = player.get_rect().move(spawnpoint)
player_move_down = [0,4]
player_move_left = [-4,0]
player_move_right = [4,0]
player_move_up = [0,-4]

def create_enemy():
    enemy_size = (30,30)
    #enemy = pygame.Surface(enemy_size)
    enemy = pygame.image.load('enemy.png').convert_alpha()  #enemy.fill(COLOR_BLUE)
    enemy_rect = pygame.Rect(WIDTH, random.randint(200, 700), *enemy_size)
    enemy_move = [random.randint(-8, -4), 0]
    return [enemy, enemy_rect, enemy_move]

def create_bonus():
    bonus_size = (20, 20)
    bonus = pygame.transform.scale(pygame.image.load('bonus.png').convert_alpha(), (100, 180 )) #pygame.Surface(bonus_size)
    #bonus.fill(COLOR_PURPLE)
    bonus_rect = pygame.Rect(random.randint(200,600), -300, *bonus_size)
    bonus_move = [0, random.randint(4, 8)]
    return [bonus, bonus_rect, bonus_move]

CREATE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ENEMY, 1500)

CREATE_BONUS = pygame.USEREVENT + 2
pygame.time.set_timer(CREATE_BONUS, 2500)

CHANGE_IMAGE = pygame.USEREVENT + 3
pygame.time.set_timer(CHANGE_IMAGE, 200)

bonuscore = []
enemies = []

score = 0

image_index = 0

playing = True
while playing:
    FPS.tick(120)

    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False
        if event.type == CREATE_ENEMY:
            enemies.append(create_enemy())
        if event.type == CREATE_BONUS:
            bonuscore.append(create_bonus())
        if event.type == CHANGE_IMAGE:
            player = pygame.image.load(os.path.join(IMAGE_PATH, PLAYER_IMAGES[image_index]))
            image_index += 1
            if image_index >= len(PLAYER_IMAGES):
                image_index = 0
                if image_index >= len(PLAYER_IMAGES):
                    image_index = 0

    #main_display.fill(COLOR_BLACK)
                    
    bg_X1 -= bg_move
    bg_X2 -= bg_move

    if bg_X1 < -bg.get_width():
        bg_X1 = bg.get_width()

    if bg_X2 < -bg.get_width():
        bg_X2 = bg.get_width()

    main_display.blit(bg, (bg_X1, 0))
    main_display.blit(bg, (bg_X2, 0))

    keys = pygame.key.get_pressed()

    if keys[K_s] and player_rect.bottom < HEIGHT:
        player_rect = player_rect.move(player_move_down)

    if keys[K_d] and player_rect.right < WIDTH:
        player_rect = player_rect.move(player_move_right)

    if keys[K_w] and player_rect.top > 0:
        player_rect = player_rect.move(player_move_up)

    if keys[K_a] and player_rect.left > 0:
        player_rect = player_rect.move(player_move_left)

    for bonus in bonuscore:
        bonus[1] = bonus[1].move(bonus[2])
        main_display.blit(bonus[0], bonus[1])
        
        if player_rect.colliderect(bonus[1]):
            score += 1
            bonuscore.pop(bonuscore.index(bonus))
    
    for enemy in enemies:
        enemy[1] = enemy[1].move(enemy[2])
        main_display.blit(enemy[0], enemy[1])
        
        if player_rect.colliderect(enemy[1]):
            playing = False

    for enemy in enemies:
        if enemy[1].right < -300:
            enemies.pop(enemies.index(enemy))

    for bonus in bonuscore:
        if bonus[1].bottom > HEIGHT:
            bonuscore.pop(bonuscore.index(bonus))

    main_display.blit(FONT.render(str(score),True, COLOR_BLACK), (WIDTH-50,20))
    main_display.blit(player, player_rect)

    print(len(enemies))

    pygame.display.flip()