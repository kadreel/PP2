import pygame
import time

pygame.init()

pygame.display.set_caption("That's a surprise tool that can help us later")

W = 600
H = 600
screen = pygame.display.set_mode((W, H))
arrow = pygame.image.load("lab 7/mickey o'clock/Hand.png")
vermin = pygame.image.load("lab 7/mickey o'clock/Vermin.png")
ring = pygame.image.load("lab 7/mickey o'clock/Ring.png")
clock = pygame.time.Clock()

arrow_rect = arrow.get_rect(center=(W/2, H/2))
vermin_rect = vermin.get_rect(center=(W/2, H/2))
ring_rect = vermin.get_rect(center=(W/2, H/2))

while True:
    screen.fill((0, 0, 0))

    seconds = int(time.time()) % 60
    minutes = int(time.time()) // 60 % 60
    angle1 = seconds * -6 - 270
    angle2 = minutes * -6 - 90

    flip_arrow = pygame.transform.flip(arrow, True, False)

    seconds_arrow = pygame.transform.rotate(flip_arrow, angle1)
    seconds_rect = seconds_arrow.get_rect(center=arrow_rect.center)
    
    minutes_arrow = pygame.transform.rotate(arrow, angle2)
    minutes_rect = minutes_arrow.get_rect(center=arrow_rect.center)

    vermin_rect = vermin.get_rect(center=vermin_rect.center)
    ring_rect = ring.get_rect(center=ring_rect.center)
    
    screen.blit(seconds_arrow, seconds_rect)
    screen.blit(minutes_arrow, minutes_rect)
    screen.blit(vermin, vermin_rect)
    screen.blit(ring, ring_rect)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    clock.tick(60)