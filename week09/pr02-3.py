import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("캐릭터 + 총알 + 타겟")
clock = pygame.time.Clock()

# 플레이어 속성
player = pygame.Rect(375, 550, 50, 30)
player_speed = 5

# 총알 리스트
bullets = []
bullet_speed = 7

# 타겟 속성
target = pygame.Rect(random.randint(0, 750), 50, 50, 30)
target_speed_x = 3
target_speed_y = 0.2  # 조금씩 내려옴

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    # 플레이어 좌우 이동
    if keys[pygame.K_LEFT]:
        player.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player.x += player_speed

    # 경계 체크
    player.left = max(player.left, 0)
    player.right = min(player.right, 800)

    # 총알 발사
    if keys[pygame.K_SPACE]:
        if not bullets or bullets[-1].y < player.y - 50:
            bullet = pygame.Rect(player.centerx - 5, player.y, 10, 20)
            bullets.append(bullet)

    # 총알 이동
    for bullet in bullets[:]:
        bullet.y -= bullet_speed
        if bullet.bottom < 0:
            bullets.remove(bullet)

    # 타겟 이동 (지그재그 + 서서히 하강)
    target.x += target_speed_x
    target.y += target_speed_y
    if target.right >= 800 or target.left <= 0:
        target_speed_x = -target_speed_x
        target.y += 20  # 방향 바꿀 때 더 내려옴

    # 화면 그리기
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 255, 0), player)  # 플레이어
    for bullet in bullets:
        pygame.draw.rect(screen, (255, 255, 0), bullet)  # 총알
    pygame.draw.rect(screen, (255, 0, 0), target)  # 타겟

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()