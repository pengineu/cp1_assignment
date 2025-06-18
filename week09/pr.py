import pygame
import sys

# pygame 초기화
pygame.init()

# 화면 생성
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("pygame 기본 예제")

# 메인 루프
running = True
while running:
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 마우스 이벤트
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(f"Mouse Button Down at {event.pos}, Button: {event.button}")
        if event.type == pygame.MOUSEMOTION:
            print(f"Mouse Move at {event.pos}")
        if event.type == pygame.MOUSEBUTTONUP:
            print(f"Mouse Button Up at {event.pos}, Button: {event.button}")

        # 키보드 이벤트
        if event.type == pygame.KEYDOWN:
            print(f"Key Down: {pygame.key.name(event.key)}")
        if event.type == pygame.KEYUP:
            print(f"Key Up: {pygame.key.name(event.key)}")

    # 화면 배경색 (흰색)
    screen.fill((255, 255, 255))

    # 화면 업데이트
    pygame.display.flip()

# pygame 종료
pygame.quit()
sys.exit()