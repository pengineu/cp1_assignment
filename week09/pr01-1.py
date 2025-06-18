import pygame
import math
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("PyGame 차량 시뮬레이션")
clock = pygame.time.Clock()

# 차량 상태
x, y = 400, 300
angle = 0
speed = 0
max_speed = 5
acceleration = 0.2
rotation_speed = 5

car_width, car_height = 50, 30

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        angle -= rotation_speed
    if keys[pygame.K_RIGHT]:
        angle += rotation_speed
    if keys[pygame.K_UP]:
        speed = min(speed + acceleration, max_speed)
    elif keys[pygame.K_DOWN]:
        speed = max(speed - acceleration, -max_speed)
    else:
        speed *= 0.95  # 마찰

    # 이동 계산
    radians = math.radians(angle)
    x += math.cos(radians) * speed
    y += math.sin(radians) * speed

    # 화면 그리기
    screen.fill((30, 30, 30))

    # 자동차 그리기
    car_surface = pygame.Surface((car_width, car_height), pygame.SRCALPHA)
    pygame.draw.rect(car_surface, (150, 200, 255), (0, 0, car_width, car_height))
    rotated_surface = pygame.transform.rotate(car_surface, -angle)
    rect = rotated_surface.get_rect(center=(x, y))
    screen.blit(rotated_surface, rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()