import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("캐릭터 + 총알 발사")
clock = pygame.time.Clock()

# 플레이어 속성
player = pygame.Rect(375, 550, 50, 30)
player_speed = 5

# 총알 리스트
bullets = []
bullet_speed = 7

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
    if player.left < 0:
        player.left = 0
    if player.right > 800:
        player.right = 800

    # 총알 발사 (스페이스바 누르면)
    if keys[pygame.K_SPACE]:
        # 연속 발사 방지를 위해 최근 총알 위치로 제한 (옵션)
        if not bullets or bullets[-1].y < player.y - 50:
            bullet = pygame.Rect(player.centerx - 5, player.y, 10, 20)
            bullets.append(bullet)

    # 총알 이동
    for bullet in bullets[:]:
        bullet.y -= bullet_speed
        if bullet.bottom < 0:
            bullets.remove(bullet)

    # 화면 그리기
    screen.fill((0, 0, 0))  # 배경
    pygame.draw.rect(screen, (0, 255, 0), player)  # 플레이어
    for bullet in bullets:
        pygame.draw.rect(screen, (255, 255, 0), bullet)  # 총알

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()