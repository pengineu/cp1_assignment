import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("타겟 클릭 감지")
clock = pygame.time.Clock()

# 타겟 설정
targets = []
num_targets = 5

def create_target():
    size = random.randint(30, 50)
    x = random.randint(0, 800 - size)
    y = random.randint(0, 600 - size)
    return pygame.Rect(x, y, size, size)

# 초기 타겟 생성
for _ in range(num_targets):
    targets.append(create_target())

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 마우스 클릭 감지
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            for target in targets:
                if target.collidepoint(mouse_pos):
                    print("타겟 클릭됨")
                    break  # 여러 개 중 첫 번째만 감지

    # 타겟 그리기
    for target in targets:
        pygame.draw.rect(screen, (255, 0, 0), target)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()