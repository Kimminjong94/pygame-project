import pygame
##########################################################################
#기본 초기화
pygame.init() # 초기화 작업

#화면 크기 설정
screen_width = 480 
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("민종 게임")

#fps
clock = pygame.time.Clock()

##########################################################################

#1. 사용자 게임 초기화 (배경화면, 게임이미지, 좌표, 폰트 등 )






#d이벤트 루프
running = True 
while running:
    dt = clock.tick(30) #게임화면의 초당 프레임술를 설정 


    #2. 이벤트 처리(키보드 마우스 등)
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가 ?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님

    #3. 게임캐릭터 위치 처리
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    #4. 충돌처리


    screen.blit(background, (0, 0)) # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos)) #캐릭터 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) #적 그리기


    #타이머 집어 넣기
    #경과시간계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 
    #경과시간을 1000으로 나누어서 초단위로 표시

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))
    screen.blit(timer, (10, 10))

    #만약 시간이 0이하이면 게임 종료
    if total_time - elapsed_time <=0:
        print("타임아웃")
        running = False

    pygame.display.update() #게임 화면 다시 그리기 !!
    
pygame.time.delay(2000)

#게임 종료
pygame.quit()