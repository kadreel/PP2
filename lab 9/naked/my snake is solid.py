import pygame, sys, random
from pygame.locals import *

pygame.init()

frame_size_x = 600
frame_size_y = 400
speed = 25

lastFood = 0

pygame.display.set_caption('Metal gear, here?!')
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)

fps_controller = pygame.time.Clock()        #SPEED, hardcaps the position of the snake into the grid to align with food. Just changing speed and moving +- 10 breaks everything

font = pygame.font.SysFont('consolas', 20)

snake_pos = [100, 50]
snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]

food_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
food_spawn = True

direction = 'RIGHT'                                                                                         #START with right turn
change_to = direction

score = 0
deathCountSession = 0

def game_over():                                                                                            #DIE
    global deathCountSession, change_to, snake_pos, snake_body, food_pos, food_spawn, direction, score, lastFood
    snake_pos = [100, 50]
    snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]
    food_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
    food_spawn = True
    direction = 'RIGHT'                                             #RESETS DEFAULT DIRECTION TO RIGHT, both change_to (valid turn check) and direction (actual direction)
    change_to = 'RIGHT'
    lastFood = 0
    score = 0
    deathCountSession += 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:                                                                       #DIE - except the game dies, not you
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:                                                                  #CHANGE DIRECTIONS - later going to be checked if it's valid
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    game_window.fill(black)
    score_text = font.render(f'Score: {score} (+{lastFood})', True, white)                  #SCORE
    game_window.blit(score_text, (10, 10))

    if change_to == 'UP' and direction != 'DOWN':                                   #TURN, BUT NOT IN THE OPPOSITE DIRECTION
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    if direction == 'UP':                                                           #ACTUALLY MOVE
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:                 #body collision with food
        lastFood = random.randint(1, 3)                                             #random food value (does not affect size cuz unfun)
        score += lastFood
        food_spawn = False
    else:
        snake_body.pop()                                                            #remove tail. Doesn't remove tail if it eats food, thus increasing size by one as it moves forward but doesn't delete the tail

    if not food_spawn:                                                              #feast
        food_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
    food_spawn = True

    for pos in snake_body:                                                          #for each sin point of gluttony, it draws a rectangle
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(game_window, white, pygame.Rect(food_pos[0], food_pos[1], 10, 10)) #this draws a rectangle - except food

    if snake_pos[0] < 0 or snake_pos[0] > frame_size_x-10:                          #death conditions
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > frame_size_y-10:
        game_over()
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()

    pygame.display.update()
    fps_controller.tick(speed)


"""
IF YOU WANT TO MAKE IT DIFFICULT SO RANDOM FOOD CAN INCREASE SIZE BY MORE THAN 1 AT A TIME:

if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:  # body collision with food
    lastFood = random.randint(1, 3)
    score += lastFood
    for i in range(lastFood):
        snake_body.append(snake_body[-1])
    food_spawn = False
"""