import pygame
import sys                  #SYS??!??!?! MORE LIKE SUS!!!!!!!!!!

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Move the Red Ball")

ball_radius = 25
ball_x, ball_y = screen_width // 2, screen_height // 2
ball_speed = 20

clock = pygame.time.Clock()

while True:
    screen.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        ball_x -= ball_speed
    if keys[pygame.K_RIGHT]:
        ball_x += ball_speed
    if keys[pygame.K_UP]:
        ball_y -= ball_speed
    if keys[pygame.K_DOWN]:
        ball_y += ball_speed

    ball_x = max(ball_radius, min(ball_x, screen_width - ball_radius))
    ball_y = max(ball_radius, min(ball_y, screen_height - ball_radius))

    pygame.draw.circle(screen, ((255, 0, 0)), (ball_x, ball_y), ball_radius)
    pygame.display.flip()
    clock.tick(30)
