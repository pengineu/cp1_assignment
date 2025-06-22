import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("마우스 슈팅 게임")
clock = pygame.time.Clock()

# 게임 상태
targets = []
num_targets = 5
score = 0

# 랜덤 타겟 생성 함수
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

        # 마우스 클릭
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            for target in targets[:]:
                if target.collidepoint(mouse_pos):
                    targets.remove(target)
                    targets.append(create_target())  # 새 타겟 추가
                    score += 1
                    print(f"Score: {score}")
                    break

    # 화면 그리기
    screen.fill((0, 0, 0))  # 배경
    for target in targets:
        pygame.draw.rect(screen, (255, 0, 0), target)  # 타겟

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()