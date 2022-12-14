import random

sel = ['가위', '바위', '보']
result = {0: '승리했습니다.', 1: '패배했습니다.', 2: '비겼습니다.'}


def checkWin(user, com):
    if not user in sel:
        print('잘못입력하였습니다. 다시 입력하세요.')
        return False

    print(f'사용자 ( {user} vs {com} ) 컴퓨터')
    if user == com:
        state = 2
    elif user == '가위' and com == '바위':
        state = 1
    elif user == '바위' and com == '보':
        state = 1
    elif user == '보' and com == '가위':
        state = 1
    else:
        state = 0
    print(result[state])
    return True, state


def continueComfirm():
    while True:
        user = input("다시 하시겠습까? : 예, 아니오")
        if user == '예':
            return True
        elif user == '아니요':
            return False
        else:
            print("예 또는 아니요를 입력하세요.")


print('\n-------------------------------------------')
round_count = 1
user_hp = 0
com_hp = 0
while True:
    print(round_count, "번째 Round")
    user = input("가위, 바위, 보 : ")
    com = sel[random.randint(0, 2)]
    check, ret = checkWin(user, com)  # 잘못된 값인지와 결과값을 가져온다.
    if check == True:
        if ret == 1:  # 결과 값에 따라 점수를 누적한다.
            com_hp += 2
        if ret == 0:
            user_hp += 2

        print("\n유저 HP : ", user_hp, " ,컴퓨터 HP : ", com_hp)
        round_count += 1
        if (round_count > 3):  # 라운드를 카운트 한다.
            print("종료합니다")
            break
print('-------------------------------------------\n')
