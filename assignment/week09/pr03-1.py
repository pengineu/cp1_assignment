import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("마우스 클릭 좌표 출력")
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 마우스 클릭 이벤트
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(f"Mouse clicked at: {event.pos}")

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()