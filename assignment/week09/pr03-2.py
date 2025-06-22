import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("랜덤 장애물 생성")
clock = pygame.time.Clock()

# 장애물 설정
targets = []
num_targets = 5

def create_target():
    size = random.randint(30, 50)
    x = random.randint(0, 800 - size)
    y = random.randint(0, 600 - size)
    return pygame.Rect(x, y, size, size)

# 초기 장애물 생성
for _ in range(num_targets):
    targets.append(create_target())

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 장애물 그리기
    for target in targets:
        pygame.draw.rect(screen, (255, 0, 0), target)  # 빨간 사각형

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()