import pygame
import math
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("PyGame 차량 시뮬레이션 (충돌 차단)")
clock = pygame.time.Clock()

# 차량 상태
x, y = 400, 300
angle = 0
speed = 0
max_speed = 5
acceleration = 0.2
rotation_speed = 5

car_width, car_height = 50, 30

# 장애물 리스트
obstacles = [
    pygame.Rect(200, 150, 100, 50),
    pygame.Rect(500, 400, 120, 60),
    pygame.Rect(300, 250, 80, 80)
]

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
        speed *= 0.95

    # 현재 위치 저장 (복구용)
    old_x, old_y = x, y

    # 이동 계산
    radians = math.radians(angle)
    x += math.cos(radians) * speed
    y += math.sin(radians) * speed

    # 자동차 rect 계산 (회전 포함 외접 사각형)
    car_surface = pygame.Surface((car_width, car_height), pygame.SRCALPHA)
    pygame.draw.rect(car_surface, (150, 200, 255), (0, 0, car_width, car_height))
    rotated_surface = pygame.transform.rotate(car_surface, -angle)
    car_rect = rotated_surface.get_rect(center=(x, y))

    # 충돌 검사 → 충돌 시 위치 복구 + 속도 정지
    for obs in obstacles:
        if car_rect.colliderect(obs):
            x, y = old_x, old_y
            speed = 0
            break

    # 화면 그리기
    screen.fill((30, 30, 30))
    for obs in obstacles:
        pygame.draw.rect(screen, (200, 50, 50), obs)

    screen.blit(rotated_surface, car_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()