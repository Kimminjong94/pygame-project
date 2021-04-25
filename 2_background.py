import pygame

pygame.init() # 초기화 작업

#화면 크기 설정
screen_width = 480 #
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("게임")

#배경이미지 불러오기
background = pygame.image.load("/Users/kimminjong/Documents/python workspace/work spaceses/pygame_basic/background.png")

#d이벤트 루프
running = True 
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가 ?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님


    screen.blit(background, (0, 0)) # 배경 그리기

    pygame.display.update() #게임 화면 다시 그리기 !!!

#게임 종료
pygame.quit()