import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("슈팅 게임 - 점수 추가")
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
target_speed_y = 0.2

# 점수
score = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player.x += player_speed

    player.left = max(player.left, 0)
    player.right = min(player.right, 800)

    if keys[pygame.K_SPACE]:
        if not bullets or bullets[-1].y < player.y - 50:
            bullet = pygame.Rect(player.centerx - 5, player.y, 10, 20)
            bullets.append(bullet)

    # 총알 이동
    for bullet in bullets[:]:
        bullet.y -= bullet_speed
        if bullet.bottom < 0:
            bullets.remove(bullet)

    # 타겟 이동
    target.x += target_speed_x
    target.y += target_speed_y
    if target.right >= 800 or target.left <= 0:
        target_speed_x = -target_speed_x
        target.y += 20

    # 총알과 타겟 충돌 검사
    for bullet in bullets[:]:
        if target.colliderect(bullet):
            bullets.remove(bullet)
            target = pygame.Rect(random.randint(0, 750), 50, 50, 30)
            target_speed_x = random.choice([-3, 3])
            score += 1
            print(f"Score: {score}")
            break

    # 화면 그리기
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 255, 0), player)
    for bullet in bullets:
        pygame.draw.rect(screen, (255, 255, 0), bullet)
    pygame.draw.rect(screen, (255, 0, 0), target)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()