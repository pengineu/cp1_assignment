import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("좌우 이동 캐릭터")
clock = pygame.time.Clock()

# 플레이어 속성
player = pygame.Rect(375, 550, 50, 30)  # (x, y, width, height)
player_speed = 5

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

    # 화면 경계 체크
    if player.left < 0:
        player.left = 0
    if player.right > 800:
        player.right = 800

    # 화면 그리기
    screen.fill((0, 0, 0))  # 배경: 검은색
    pygame.draw.rect(screen, (0, 255, 0), player)  # 플레이어: 초록색

    pygame.display.flip()
    clock.tick(60)  # 60 FPS

pygame.quit()
sys.exit()