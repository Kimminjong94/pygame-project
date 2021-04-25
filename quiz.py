import random
import pygame
##########################################################################
#기본 초기화
pygame.init() # 초기화 작업

#화면 크기 설정
screen_width = 480 
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("민whd quiz")

#fps
clock = pygame.time.Clock()

##########################################################################

#1. 사용자 게임 초기화 (배경화면, 게임이미지, 좌표, 폰트 등 )

background = pygame.image.load("/Users/kimminjong/Documents/python workspace/work spaceses/pygame_basic/background.png")

#캐릭터 만들기
character = pygame.image.load("/Users/kimminjong/Documents/python workspace/work spaceses/pygame_basic/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height


#이동 위치
to_x = 0
character_speed = 10


#똥만들기 
ddong = pygame.image.load("/Users/kimminjong/Documents/python workspace/work spaceses/pygame_basic/enemy.png")
ddong_size = ddong.get_rect().size
ddong_width = ddong_size[0]
ddong_height = ddong_size[1]
ddong_x_pos = random.randint(0, screen_width - ddong_width)
ddong_y_pos = 0
ddong_speed = 20


#d이벤트 루프
running = True 
while running:
    dt = clock.tick(30) #게임화면의 초당 프레임술를 설정 


    #2. 이벤트 처리(키보드 마우스 등)
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가 ?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    #3. 게임캐릭터 위치 처리
    character_x_pos += to_x


    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width


    ddong_y_pos += ddong_speed


    if ddong_y_pos > screen_height:
        ddong_y_pos = 0
        ddong_x_pos = random.randint(0, screen_width - ddong_width)

    #4. 충돌처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    ddong_rect = ddong.get_rect()
    ddong_rect.left = ddong_x_pos
    ddong_rect.top = ddong_y_pos

    if character_rect.colliderect(ddong_rect):
        print("충돌했어요")
        running = False

    #5. 화면에 그리기
    screen.blit(background, (0,0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(ddong, (ddong_x_pos, ddong_y_pos))


    #타이머 집어 넣기
    #경과시간계산
    #경과시간을 1000으로 나누어서 초단위로 표시

    #만약 시간이 0이하이면 게임 종료
 

    pygame.display.update() #게임 화면 다시 그리기 !!
    
pygame.time.delay(2000)

#게임 종료
pygame.quit()