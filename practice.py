balls = [1,2,3,4]
weapons = [11,22,3,44]

for ball_idx, ball_val in enumerate(balls):
    print("ball :", ball_val)
    for weapon_idx, weapon_val in enumerate(weapons):
        print("weapon :", weapon_val)
        if ball_val == weapon_val:
            print("공과 무기가 충돌")
            break
    else:
        continue
    print("바깥 for ㅜㄴ break")
    break
