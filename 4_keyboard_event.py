import pygame

pygame.init() # 초기화 작업

#화면 크기 설정
screen_width = 480 #
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Nado Game")

#배경이미지 불러오기
background = pygame.image.load("/Users/kimminjong/Documents/python workspace/work spaceses/pygame_basic/background.png")

#캐릭터 불러오기
character = pygame.image.load("/Users/kimminjong/Documents/python workspace/work spaceses/pygame_basic/character.png")
character_size = character.get_rect().size # 이미지 크기를 구해옴
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)#화면 가로의 절반 크기에 해당하는 위치(가로)
character_y_pos = screen_height - character_height#화면 세로크기 가장 아래에(세로)


#이동할 좧표
to_x = 0
to_y = 0

#d이벤트 루프
running = True 
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가 ?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= 5 # to
            elif event.key == pygame.K_RIGHT:
                to_x += 5
            elif event.key == pygame.K_UP:
                to_y -= 5
            elif event.key == pygame.K_DOWN:
                to_y += 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key ==pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key ==pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x
    character_y_pos += to_y

#가로 경걔값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

#세로 경계값처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    screen.blit(background, (0, 0)) # 배경 그리기

    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update() #게임 화면 다시 그리기 !!!

#게임 종료
pygame.quit()